from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

# Create your models here.

User = get_user_model()

class Bmi(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.FloatField()
    height = models.FloatField()
    bmi = models.FloatField()
    trackDate = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    def status(self):
        if self.bmi < 0.16:
            state = "Sever Thinness"
            return state
        elif self.bmi >= 0.16 and self.bmi < 0.18:
            state = "Mild Thinness"
            return state
        elif self.bmi >= 0.18 and self.bmi < 0.25:
            state = "Normal"
            return state
        elif self.bmi >= 0.25 and self.bmi < 0.30:
            state = "Overweight"
            return state
        elif self.bmi >= 0.30 and self.bmi < 0.35:
            state = "Obese Class I"
            return state
        elif self.bmi >= 0.35 and self.bmi < 0.40:
            state = "Obese Class II"
            return state
        elif self.bmi >= 0.40:
            state = "Obese Class III"
            return state
