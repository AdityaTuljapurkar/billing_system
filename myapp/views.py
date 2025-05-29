from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import Customer_Data
# Create your views here.
def home(request):
    return render(request, 'index.html', {})

def customer_form(request):
    return render(request, 'customer_form.html', {})


def customer_form(request):
    return render(request, 'customer_form.html')

def submit_customer(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        total_Bill = request.POST.get('total_Bill')

        Customer_Data.objects.create(
            name=name,
            phone_number=phone_number,
            total_Bill=total_Bill
        )
        return HttpResponse("Customer data submitted successfully!")
    else:
        return HttpResponse("Invalid request method.")
