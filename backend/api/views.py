from django.contrib.auth import authenticate
from .serializers import UserSerializer , CarDetailSerializer , RealEstateDetailSerializer , CarProductSerializer , EstateProductSerializer

# DRF imports
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny , IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

#JWT imports
from rest_framework_simplejwt.tokens import RefreshToken

# Models
from .models import Car , RealEstate

# Filtering

from django_filters.rest_framework import DjangoFilterBackend

#Pagination

from rest_framework.pagination import PageNumberPagination

#Chain
from itertools import chain
from operator import attrgetter

#Search
from django.db.models import Q

class LoginUserView(APIView):
    permission_classes = [AllowAny]
    
    def post(self , request):
        email = request.data.get("email")
        password = request.data.get("password")
        
        if not email or not password:
            return Response({
                "detail": "Email and password are required."
            }, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(email=email , password=password)
        
        if user is not None:
            refresh = RefreshToken.for_user(user)
            
            token_data = {
                "access" : str(refresh.access_token)
            }
            user_data= {
                "username" : user.username,
                "email" : user.email
            }
            return Response([token_data , user_data])
        else:
            return Response({
                "detail":"Invalid credentials"
            } , status=status.HTTP_401_UNAUTHORIZED)
            
class RegisterUserView(APIView):
    permission_classes= [AllowAny]
    
    def post(self , request  , *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            
            return Response({
                "message":"User created successfully",
                "User": UserSerializer(user).data
            } , status=status.HTTP_201_CREATED)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
    
class CarView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request):
        cars = Car.objects.filter(user=request.user)
        serializer = CarDetailSerializer(cars , many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = CarDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self ,request , *args, **kwargs):
        car_id = kwargs.get("car_id")
        
        try:
            car = Car.objects.get(id=car_id , user=request.user)
        except Car.DoesNotExist:
            return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)

        
        serializer = CarDetailSerializer(car , data=request.data , partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self , request , *args, **kwargs):
        car_id = kwargs.get("car_id")
        
        try:
            car = Car.objects.get(id=car_id , user=request.user)
        except Car.DoesNotExist:
            return Response({"error" : "Car not found."} , status=status.HTTP_404_NOT_FOUND)
        car.delete()
        return Response({"message":"Car deleted successfully."} , status=status.HTTP_204_NO_CONTENT)
    
class RealEstateView(APIView):
    permission_classes = [IsAuthenticated]
    
    def get(self , request):
        realEstate = RealEstate.objects.filter(user=request.user)
        serializer = RealEstateDetailSerializer(realEstate , many = True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = RealEstateDetailSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def put(self , request , *args, **kwargs):
        estate_id = kwargs.get("estate_id")
        try:
            estate = RealEstate.objects.get(id=estate_id , user= request.user)
        except RealEstate.DoesNotExist:
                return Response({"error": "Real Estate not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = RealEstateDetailSerializer(estate , data=request.data , partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST)

    def delete(self , request , *args, **kwargs):
        estate_id = kwargs.get("estate_id")
        
        try:
            estate = RealEstate.objects.get(id=estate_id , user = request.user)
        except RealEstate.DoesNotExist:
            return Response({"message" : "Real Estate not found"} , status=status.HTTP_404_NOT_FOUND)
        estate.delete()
        return Response({"message" : "Real Estate deleted successfully"} , status=status.HTTP_204_NO_CONTENT)

class CustomPagination(PageNumberPagination):
    page_size = 14
    page_size_query_param = 'page_size'
    max_page_size = 100 
   
class EstateDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self, request , estate_id):
        try:
            estate = RealEstate.objects.get(id=estate_id , user=request.user)
        except RealEstate.DoesNotExist:
            return Response({
                "error" : "Estate not found"
            } , status=status.HTTP_404_NOT_FOUND)
            
        serializer = RealEstateDetailSerializer(estate)
        return Response(serializer.data)
    
class CarDetail(APIView):
    permission_classes = [AllowAny]
    
    def get(self , request , car_id):
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return Response({
                "error" : "Car not Found"
            } , status=status.HTTP_404_NOT_FOUND)
        
        serializer = CarDetailSerializer(car)
        return Response(serializer.data)
            
            
def normalize_query(query):
    char_map = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")
    return query.translate(char_map)
        
class Search(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        search_query = request.query_params.get('q', '').strip()
        
        if not search_query:
            estates = RealEstate.objects.all()
            cars = Car.objects.all()
        else:
           
            search_query_normalized = normalize_query(search_query)

        
            estates = RealEstate.objects.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(location__icontains=search_query) |
                Q(title__icontains=search_query_normalized) |
                Q(description__icontains=search_query_normalized) |
                Q(location__icontains=search_query_normalized)
            )

            cars = Car.objects.filter(
                Q(title__icontains=search_query) |
                Q(description__icontains=search_query) |
                Q(brand__icontains=search_query) |
                Q(model__icontains=search_query) |
                Q(title__icontains=search_query_normalized) |
                Q(description__icontains=search_query_normalized) |
                Q(brand__icontains=search_query_normalized) |
                Q(model__icontains=search_query_normalized)
            )
        
        combined = sorted(
            chain(estates, cars), key=attrgetter("created_at"), reverse=True
        )
        
        result = []
        for item in combined:
            serializer_class = (
                RealEstateDetailSerializer if isinstance(item, RealEstate) else CarDetailSerializer
            )
            serializer = serializer_class(item)
            result.append(serializer.data)
        
        return Response({"products": result})
    
class Products(APIView):
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination 
    
    def get(self , request):
        estates = RealEstate.objects.all()
        cars = Car.objects.all()
        
        combined = sorted(
            chain(estates, cars), key=attrgetter("created_at"), reverse=True
        )

        paginator = self.pagination_class()
        paginator.page_size = 28
        
        result = []
        for item in combined:
            if isinstance(item, RealEstate):
                serializer = EstateProductSerializer(item)
            elif isinstance(item, Car):
                serializer = CarProductSerializer(item)
            result.append(serializer.data)
        
        try:
            page = paginator.paginate_queryset(result , request)
            if page is not None:
                return paginator.get_paginated_response({"products" : page})
        except Exception as e:
            return Response({"detail: " :str(e)} , status=status.HTTP_404_NOT_FOUND)

        return paginator.get_paginated_resonse({
            "products" : result
        })

class GetCarById(APIView):
    permission_classes = [AllowAny]
    
    def get(self , request , *args, **kwargs):
        car_id = kwargs.get("car_id")
        
        try:
            car = Car.objects.get(id=car_id)
        except Car.DoesNotExist:
            return Response({"error": "Car not found."}, status=status.HTTP_404_NOT_FOUND)
        serializer = CarDetailSerializer(car)
        
        return Response(serializer.data)

class GetEstateById(APIView):
    permission_classes = [AllowAny]
    
    def get(self , request , *args, **kwargs):
        estate_id = kwargs.get("estate_id")
        try:
            estate = RealEstate.objects.get(id=estate_id)
        except RealEstate.DoesNotExist:
            return Response({"error" : "Estate not found"} , status=status.HTTP_404_NOT_FOUND)
        serializer = RealEstateDetailSerializer(estate)
        return Response(serializer.data)

class ProductCar(APIView):
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination 
    
    def get(self , request):
        cars = Car.objects.all()
        serializer = CarProductSerializer(cars , many=True)
        
        paginator = self.pagination_class()
        paginator.page_size = 28
        
        try:
            page = paginator.paginate_queryset(serializer.data, request)
            if page is not None:
                return paginator.get_paginated_response({"products" : page})
        except Exception as e:
            return Response({"detail" : str(e)} , status=status.HTTP_404_NOT_FOUND)
        
        return paginator.get_paginated_response({
            "products" : serializer.data
        })
        
class ProductEstate(APIView):
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination 
    
    def get(self , request):
        estates = RealEstate.objects.all()
        serializer = EstateProductSerializer(estates , many=True)
        
        paginator = self.pagination_class()
        paginator.page_size = 28
        
        try:
            page = paginator.paginate_queryset(serializer.data, request)
            if page is not None:
                return paginator.get_paginated_response({"products" : page})
        except Exception as e:
            return Response({"detail" : str(e)} , status=status.HTTP_404_NOT_FOUND)
        
        return paginator.get_paginated_response({
            "products" : serializer.data
        })
        
class ProductDetail(APIView):
    permission_classes = [AllowAny]

    def get(self, request, product_id):
        try:
            car = Car.objects.get(id=product_id)
            serializer = CarDetailSerializer(car) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except Car.DoesNotExist:
            pass

        try:
            estate = RealEstate.objects.get(id=product_id)
            serializer = RealEstateDetailSerializer(estate) 
            return Response(serializer.data, status=status.HTTP_200_OK)
        except RealEstate.DoesNotExist:
            pass

        return Response({"error": "Product not found."}, status=status.HTTP_404_NOT_FOUND)