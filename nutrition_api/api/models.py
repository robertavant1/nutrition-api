from django.db import models
from django.contrib.auth.models import User

class FoodLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=30)
    calories = models.IntegerField(default = 0)
    protein = models.IntegerField(default = 0)
    carbs = models.IntegerField(default = 0)
    
