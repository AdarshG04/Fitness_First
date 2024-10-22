from django.urls import path
from users import views

urlpatterns = [
   path('', views.index, name='index'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('signup/', views.signup_view, name='signup'),
   path("password_reset/", views.password_reset_request, name="password_reset"),
   path('process_payment/', views.process_payment, name='process_payment'),
]