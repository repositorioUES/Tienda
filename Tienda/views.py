from django.shortcuts import render
from django.http import HttpResponse
from .models import *
# Create your views here.

def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = Customer.objects.all().count()
    total_orders = Order.objects.all().count()
    delivered = Order.objects.all().filter(status = 'Delivered').count()
    pending = Order.objects.all().filter(status = 'Pending').count()
    context = {
        'orders' : orders,
        'customers' : customers,
        'total_customers' : total_customers,
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' : pending
    }
    return render (request, 'dashboard.html', context)

def products(request):
    products = Product.objects.all()
    return render (request, 'products.html', {'products':products}) 

def customer(request,pk):
    customer = Customer.objects.get(id=pk)
    orders = customer.order_set.all()
    order_count = orders.count()
    context = {
        'customer' : customer,
        'orders' : orders,
        'order_count' : order_count
    }
    return render (request, 'customer.html',context)