from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=120)
    longitude = models.CharField(max_length=120)
    latitude = models.CharField(max_length=120)

    def __str__(self):
        return self.name

class User(models.Model):
    name_User = models.CharField(max_length=120)
    username = models.CharField(max_length=120)
    password = models.CharField(max_length=120)

    def __str__(self):
        return self.name_User


class Station(models.Model):
    name_Station = models.CharField(max_length=120)
    quantityBike = models.IntegerField()
    quantityElecBike = models.IntegerField()
    quantityElecMoto = models.IntegerField()
    totalVehicle = models.IntegerField()
    remainVehicle = models.IntegerField()
    longitude = models.CharField(max_length=120)
    latitude = models.CharField(max_length=120)

    def __str__(self):
        return self.name_Station

class ElecBike(models.Model):
    ID_EBike = models.CharField(primary_key = True, max_length=120)
    Belong_Station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_EBike

class Bike(models.Model):
    ID_Bike = models.CharField(primary_key = True, max_length=120)
    Belong_Station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_Bike

class ElecMoto(models.Model):
    ID_EMoto = models.CharField(primary_key = True, max_length=120)
    Belong_Station = models.ForeignKey(Station, on_delete=models.CASCADE)

    def __str__(self):
        return self.ID_EMoto

class Rent_Detail(models.Model):
    date = models.DateField(auto_now_add=True)
    timeDepart = models.TimeField()
    timeArrive = models.TimeField()
    stationDepart = models.ForeignKey(Station, related_name = 'rentdetail_stationArrive', on_delete=models.CASCADE)
    stationArrive = models.ForeignKey(Station, related_name = 'rentdetail_stationDepart', on_delete=models.CASCADE)
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __date__(self):
        return self