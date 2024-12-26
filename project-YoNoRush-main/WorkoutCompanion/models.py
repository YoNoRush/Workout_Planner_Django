from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

class WorkoutCompanion(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    GOAL_CHOICES = [
        ('Lose Weight', 'Lose Weight'),
        ('Gain Weight', 'Gain Weight'),
        ('Gain Muscle', 'Gain Muscle'),
    ]

    user_first_name = models.CharField(max_length=30)
    user_last_name = models.CharField(max_length=30)
    user_age = models.IntegerField()
    user_gender = models.CharField(max_length=6, choices=GENDER_CHOICES)
    user_weight = models.FloatField()
    user_height = models.FloatField()
    user_workout_choice = models.CharField(max_length=12, choices=GOAL_CHOICES)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        if self.user:
            return f"Workout Companion for {self.user.username}"
        return "Workout Companion with no user"