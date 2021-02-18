from django.db import models
from django.contrib.auth.models import User


# class Capitan(models.Model):
#     name = models.CharField(max_length = 200)
#     serial = models.CharField(max_length = 10)
#     history = Mission.location.sol_date#(plus time played, plus rest phase)
#     user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
#     #capitan FK

#     def __str__(self):
#         return self.title

# class Mission(models.Model):
#     location = #use data from nasa api for route point at end of last mission/ or initial landing sight
#     scape = #use image from api at location #updates the map on the dashboard and the appropriate window view
#     sol_date = #use data from api at location to start/ Capitan history to continue
#     earth_date = 
    
#     def __str__(self):
#         return self.location

# class Tasks(models.Model):


