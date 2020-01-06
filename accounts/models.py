from django.db import models

# Create your models here.
class Profile(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    username = models.CharField(max_length=20)
    email = models.EmailField()
    pic = models.ImageField(upload_to='user_pics')

