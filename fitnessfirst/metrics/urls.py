# metrics/urls.py
from django.urls import path
from . import views

app_name = 'metrics'

urlpatterns = [
    path('calculate/', views.calculate_metrics, name='calculate_metrics'),
    path('results/<int:metric_id>/', views.results, name='results'),
]
