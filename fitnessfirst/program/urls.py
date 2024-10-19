from django.urls import path
from program import views

urlpatterns = [
   path('program/', views.get_program, name='program'),
]