from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ToDo(models.Model):
    userCreater= models.ForeignKey(User,on_delete=models.CASCADE)
    
    title = models.CharField(max_length=120)
    memo = models.TextField(blank=True)
    created=models.DateTimeField(auto_now_add= True)
    date_completed= models.DateTimeField(null=True,blank=True) #when someone hits complete it wil fill
    important = models.BooleanField(default=False)
    
    
    def __str__(self):
        return self.title