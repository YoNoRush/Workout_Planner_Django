from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .models import WorkoutCompanion
from .forms import UserInputForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm



def index(request):
    WorkoutCompanions = WorkoutCompanion.objects.all()
    return render(request, 'index.html', {'WorkoutCompanions': WorkoutCompanions})

def user_input(request):
    try:
        workout_info = request.user.workoutcompanion
    except WorkoutCompanion.DoesNotExist:
        workout_info = None

    if request.method == 'POST':
        form = UserInputForm(request.POST, request.FILES, instance=workout_info)
        if form.is_valid():
            companion = form.save(commit=False)
            companion.user = request.user
            companion.save()
            return redirect('login')
    else:
        form = UserInputForm(instance=workout_info)

    return render(request, 'user_input.html', {'form': form})

def sign_up(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('user_input')
    else:
        form = CustomUserCreationForm()
    return render(request, 'signup.html', {'form': form})

def log_in(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('view_workout_info')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})


@login_required
def view_workout_info(request):
    try:
        workout_info = request.user.workoutcompanion
    except WorkoutCompanion.DoesNotExist:
        workout_info = None
    user = request.user
    caloric_intake = round(caloric_calculator(user))
    return render(request, 'view_workout_info.html', {'workout_info': workout_info, 'caloric_intake': caloric_intake })

@login_required
def logginOut(request):
    logout(request)
    return redirect('index')

def caloric_calculator(user):

    if user.workoutcompanion.user_gender == 'Male':
        Total_Daily_Energy_Expend = (10 * user.workoutcompanion.user_weight + 6.25 * user.workoutcompanion.user_height - 5
               * user.workoutcompanion.user_age + 5) * 1.425
        if user.workoutcompanion.user_workout_choice == 'Lose Weight':
            return Total_Daily_Energy_Expend - 500
        else:
            return Total_Daily_Energy_Expend + 500


    elif user.workoutcompanion.user_gender == 'Female':
        Total_Daily_Energy_Expend = (10 * user.workoutcompanion.user_weight + 6.25 * user.workoutcompanion.user_height - 5
               * user.workoutcompanion.user_age - 161) * 1.425
        if user.workoutcompanion.user_workout_choice == 'Lose Weight':
            return Total_Daily_Energy_Expend - 500
        else:
            return Total_Daily_Energy_Expend + 500