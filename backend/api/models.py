from django.db import models
from django.contrib.auth.models import User 


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        abstract = True
    
    def __str__(self):
        return self.title
    
    
class Car(Product):
    
    type = models.CharField(max_length=10 , editable=False , default="car")
    
    brand = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.PositiveIntegerField()
    
    category = models.CharField(max_length=100  , default="Otomobil")
    fuel = models.CharField(max_length=100 , default="Benzin")
    gear = models.CharField(max_length=100,default="Manual")
    condition = models.CharField(max_length=20,default="Sıfır")
    mileage = models.CharField(max_length=100, default="0 km")
    bodyType = models.CharField(max_length=100, default="Sedan")
    enginePower = models.CharField(max_length=100, default="100 HP")
    engineVolume = models.CharField(max_length=100, default="1.6 L")
    traction = models.CharField(max_length=100 ,default="FWD")
    color = models.CharField(max_length=100, default="White")
    warranty = models.BooleanField(default=False)
    heavyDamage = models.BooleanField(default=False)
    plate = models.CharField(max_length=100, default="Unknown")
    seller = models.CharField(max_length=100, default="Owner")
    swap = models.BooleanField(default=False)
    
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} - {self.brand} {self.model} ({self.year})"

class RealEstate(Product):
    
    type = models.CharField(max_length=10 , editable=False , default="estate") 

    
    location = models.CharField(max_length=255)
    property_type = models.CharField(max_length=50  , default="Apartment")
    
    grossArea = models.PositiveIntegerField(default=0)
    netArea = models.PositiveIntegerField(default=0)
    roomCount = models.PositiveIntegerField(default=0)
    buildingAge = models.PositiveIntegerField(default=0)
    floor = models.PositiveIntegerField(default=0)
    totalFloors = models.PositiveIntegerField(default=0)
    
    heating = models.CharField(max_length=255  , default="Central")
    
    bathrooms = models.PositiveIntegerField(default=1)
    kitchen = models.PositiveIntegerField(default=1)
    balcony = models.PositiveIntegerField(default=0)
    
    elevator = models.BooleanField(default=False)
    category = models.CharField(max_length=100  , default="Konut")
    parking = models.BooleanField(default=False)
    insideSite = models.BooleanField(default=False)
    dues = models.PositiveIntegerField(default=0) 
    deposit = models.PositiveIntegerField(default=0)
    
    seller = models.CharField(max_length=50 , default="Sahibinden" )
    
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self): 
        return f"{self.title} - {self.property_type} ({self.location})"

