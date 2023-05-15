

from django.db import models

class User(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(max_length=255, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

#class scope1Stationari(models.Model):
          #facilityId = models.CharField(max_length=255)
          #year = models.CharField(max_length=255, unique=True)
          #customEmission = models.CharField(auto_now_add=True)
          #fuel = models.CharField(max_length=255)
          #amountFuel = models.CharField(max_length=255, unique=True)
          #unit = models.CharField(auto_now_add=True)

#class scope1Movil(models.Model):
          #year = models.CharField(max_length=255, unique=True)
          #facilityId = models.CharField(max_length=255)
          #activityType=models.CharField(auto_now_add=True) 
          #fuelSource = models.CharField(max_length=255, unique=True)
          #vehicleType = models.CharField(max_length=255, unique=True)
          #acticityAmount = models.CharField(auto_now_add=True)
          #unitFuel = models.CharField(auto_now_add=True)


#class scope1Refrigerants(models.Model):
          #year = models.CharField(max_length=255, unique=True)
          #facilityId = models.CharField(max_length=255)
          #refrigerantUsed = models.CharField(max_length=255, unique=True)         
          #c = models.CharField(max_length=255)
          #d = models.CharField(max_length=255, unique=True)
          #e = models.CharField(max_length=255)
          #f = models.CharField(max_length=255, unique=True)
          #g = models.CharField(auto_now_add=True)
          #h = models.CharField(max_length=255)
          #i = models.CharField(max_length=255, unique=True)
          #j = models.CharField(auto_now_add=True)
          #k = models.CharField(auto_now_add=True)
          #l = models.CharField(max_length=255)
          #x = models.CharField(max_length=255, unique=True)
          #y = models.CharField(auto_now_add=True)
          #z = models.CharField(auto_now_add=True)



#class scope1Movil(models.Model):
          #facilityId = models.CharField(max_length=255)
          #year = models.CharField(max_length=255, unique=True)
          #activityType=models.CharField(auto_now_add=True) 
          #vehicleType = models.CharField(max_length=255, unique=True)
          #acticityAmount = models.CharField(auto_now_add=True)
          #unitFuel = models.CharField(auto_now_add=True)


#class scope1Refrigerants(models.Model):
          #facilityId = models.CharField(max_length=255)
          #year = models.CharField(max_length=255, unique=True)
          #typeAirConditRefrigEquip = models.CharField(max_length=255)
          #refrigerantUsed = models.CharField(max_length=255, unique=True)
          #refrigerantInventory = models.CharField(max_length=255)
          #RefrigerpurProdDistributors = models.CharField(max_length=255, unique=True)
          #customEmission = models.CharField(auto_now_add=True)
          #fuel = models.CharField(max_length=255)
          #amountFuel = models.CharField(max_length=255, unique=True)
          #unit = models.CharField(auto_now_add=True)
