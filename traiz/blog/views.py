from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dash_board(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def target_finder(request):
    return render(request, 'blog/target_finder.html')

def threat_detection(request):
    return render(request, 'blog/threat_detection.html')

def license(request):
    return render(request, 'blog/license.html')

def customer_care(request):
    return render(request, 'blog/customer_care.html')

def notification(request):
    return render(request, 'blog/notification.html')
