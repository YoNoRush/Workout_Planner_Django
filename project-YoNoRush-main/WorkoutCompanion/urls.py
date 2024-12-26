from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('input/', views.user_input, name='user_input'),
    path('sign-up/', views.sign_up, name='signup'),
    path('log-in/', views.log_in, name='login'),
    path('view-workout-info/', views.view_workout_info, name='view_workout_info'),
    path('logout/', views.logginOut, name='logout'),
]



