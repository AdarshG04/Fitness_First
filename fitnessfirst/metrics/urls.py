from django.urls import path
from metrics import views

app_name = 'metrics'

urlpatterns = [
    path('', views.view_fitness_metrics, name='fitness_metrics'),  # Default view for metrics
    path('add/', views.add_fitness_metric, name='add_fitness_metric'),
    path('view/', views.view_fitness_metrics, name='fitness_metrics'),
]
