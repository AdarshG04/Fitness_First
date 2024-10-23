from django.urls import path
from . import views

app_name = 'diet'

urlpatterns = [
    path('user-diet-plan/', views.user_diet_plan, name='user_diet_plan'),
]