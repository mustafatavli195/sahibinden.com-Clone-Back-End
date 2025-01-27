from django.contrib import admin
from django.urls import path

from api.views import LoginUserView , RegisterUserView , CarView , RealEstateView , Search , EstateDetail , CarDetail , Products , GetCarById , GetEstateById , ProductCar , ProductEstate , ProductDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    
    #USER
    
    path("api/user/login/" , LoginUserView.as_view() , name="login"),
    path("api/user/register/" , RegisterUserView.as_view() , name="register"),
    
    #CAR
    
    path("api/user/car/" , CarView.as_view() , name="car"),
    path("api/user/car/<int:car_id>/" , CarView.as_view() , name="car-update-delete"),
    
    
    #ESTATE
    
    path("api/user/estate/", RealEstateView.as_view(), name="estate"),
    path("api/user/estate/<int:estate_id>/", RealEstateView.as_view(), name="estate-update-delete"),
    
    
    # Search
    
    path("api/search/" , Search.as_view() , name="search") , 
    
    path("api/estate/<int:estate_id>", EstateDetail.as_view(), name="estate-detail") , 

    path("api/car/<int:car_id>", CarDetail.as_view(), name="car-detail"),
    
    #All Products
    
    path("api/products/", Products.as_view() , name="products" ),
    
    #Get By Id
    
    path("api/car-id/<int:car_id>/", GetCarById.as_view(), name="get-car-by-id"),
    path("api/estate-id/<int:estate_id>/", GetEstateById.as_view(), name="get-estate-by-id"),
    
    #Product Categori
    
    path("api/products/car/" , ProductCar.as_view() ,name="product-car"),
    path("api/products/estate/" , ProductEstate.as_view() , name="estate-car"),
    
    path("api/products/<int:product_id>" , ProductDetail.as_view() , name="product_detail")
]