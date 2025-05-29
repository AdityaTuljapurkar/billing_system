from django.urls import path
from django.urls import include
from myapp import views 


urlpatterns = [
    path("", views.home, name='home'),
    path('customer_form/', views.customer_form, name='customer_form'),
    path('submit_customer/', views.submit_customer, name='submit_customer'),
]
