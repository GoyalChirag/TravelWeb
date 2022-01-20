from django.db import models

# Create your models here.
class Destination(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    name= models.CharField(max_length=100)
    email= models.EmailField(max_length=100,unique=True)

    def __str__(self):
        return self.email