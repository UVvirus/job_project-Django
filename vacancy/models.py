from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class VacancyModel(models.Model):
    Author=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.CharField(max_length=200)
    