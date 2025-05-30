from django.urls import path
from django.urls import include
from myapp import views 


urlpatterns = [
    path('', views.autenthication, name='autentication'),
    path('log_in',views.log_in,name = 'log_in'),


    path("home", views.home, name='home'),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('submit_customer/', views.submit_customer, name='submit_customer'),
]
