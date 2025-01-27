from django.contrib.auth.models import User
from .models import Car , RealEstate
from rest_framework import serializers

import re


#USER SERIALIZER

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id" , "username" , "password" , "email"]
        extra_kwargs = {"password":{"write_only":True}}
        
    def validate_username(self , value):
        if len(value)<6 or len(value)>15:
            raise Exception("Username must be between 6 and 15 characters")
        if not value.isalnum():
            raise serializers.ValidationError("Username can only contain letters and numbers.")
        return value
    
    def validate_password(self, value):
        if len(value) < 6 or len(value)>15:
            raise serializers.ValidationError("Password must be between 6 and 15 characters.")
        
        if not any(char.isdigit() for char in value):
            raise serializers.ValidationError("Password must contain at least one number.")
        return value
    
    def validate_email(self , value):
        email_regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_regex , value):
            raise serializers.ValidationError("Invalid email address.")
        if User.objects.filter(email=value).exists():
            raise serializers.ValidationError("This email is already in use.")
        return value
            
    def create(self , validated_data):
        user = User.objects.create_user(
            email= validated_data["email"],
            username=validated_data["username"],
            password=validated_data["password"]
        )
        return user


#DETAİL SERIALIZER

class CarDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') 
    class Meta:
        model = Car
        fields = "__all__"
        
        
class RealEstateDetailSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source='user.username') 
    class Meta:
        model = RealEstate
        fields = "__all__"
                
    
#PRODUCT SERIALIZER

class EstateProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = "user.username")
    class Meta:
        model = RealEstate
        fields = ["id" , "title" , "created_at" , "updated_at" , "user" , "type"]
        
class CarProductSerializer(serializers.ModelSerializer):
    user = serializers.ReadOnlyField(source = "user.username")
    class Meta:
        model = Car
        fields = ["id" , "title" , "created_at" , "updated_at" , "user" , "type"]
        