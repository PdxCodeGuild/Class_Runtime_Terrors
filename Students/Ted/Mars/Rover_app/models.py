from django.db import models
from django.contrib.auth.models import User

#sign-in in Capitan app 

# class Greeting(models.Model):
#     location = models.ForeignKey(Capitan_app/views.location)
#     tasks_done = models.ForeignKey(Capitan_app/models.tasks.done)
#     todo = models.ForeignKey(views.tasks.todo)

# class Image(models.Model):#change to class Mission
#     sol = models.IntegerField()#change to capitan= models...
#     rover_name = models.TextField(max_length = 500)#cange to serial
#     image_link = models.TextField(max_length = 500)
#     camera_name = models.TextField(max_length = 500)
#     user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
#     #capitan FK

#     def __str__(self):
#         return self.rover_name

class MediaModel(models.Model):
    my_image = models.ImageField(upload_to='images/')

class Image(models.Model):
    sol = models.IntegerField()
    image_link = models.TextField(max_length = 500)
    
    def __str__(self):
        return str(self.sol)

#class location in Capitan app
 #return sol, rover name, image source, camera-names 

#class capitan
