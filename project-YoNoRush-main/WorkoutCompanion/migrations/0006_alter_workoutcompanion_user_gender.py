# Generated by Django 5.1.3 on 2024-12-10 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WorkoutCompanion', '0005_alter_workoutcompanion_user_workout_choice'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workoutcompanion',
            name='user_gender',
            field=models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], max_length=6),
        ),
    ]