from django.db import models
from django.contrib.auth.models import User

#sign-in in Capitan app 

# class Greeting(models.Model):
#     location = models.ForeignKey(Capitan_app/views.location)
#     tasks_done = models.ForeignKey(Capitan_app/models.tasks.done)
#     todo = models.ForeignKey(views.tasks.todo)

class Blog(models.Model):#change to class Mission
    title = models.CharField(max_length = 200)#change to capitan= models...
    text = models.TextField(max_length = 500)#change to serial
    pub_date = models.DateField()
    user = models.ForeignKey(User, on_delete = models.CASCADE, null=True, blank=True)
    #capitan FK

    def __str__(self):
        return self.title

#class location in Capitan app
   

#class capitan
