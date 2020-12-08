from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


data_generated=[
{
'Company_name':'tanzet ',
'Title':'data collected on tanzet',
'Tag':'recruitment',
'Date':'6 september 2020',
'Content':'Recruitment of people from development industory.'
},
{
'Company_name':'bluemart ',
'Title':'data collected on bluemart',
'Tag':'Popularity',
'Date':'4 september 2020',
'Content':'Came in news for catching robbers'
}
]
def dash_board(request):
    context={
        'Signals':data_generated
    }
    return render(request, 'blog/home.html',context)

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
