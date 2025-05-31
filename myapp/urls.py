from django.urls import path
from django.urls import include
from myapp import views 
from . import views




urlpatterns = [
    path('', views.log_in, name='log_in'),  # Login becomes the home page
    path('home/', views.home, name='home'),
    path("home", views.home, name='home'),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('submit_customer/', views.submit_customer, name='submit_customer'),

]
