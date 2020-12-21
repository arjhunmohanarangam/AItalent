from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm


# Create your views here.
data_generated=[
{
'Company_name':'tanzet ',
'Title':'data collected on tanzet',
'Tag':'recruitment',
'Date':'6 september 2020',
'Content':'Recruitment of people from development industory.',
'Link':'https://tanzet.com'
},
{
'Company_name':'bluemart ',
'Title':'data collected on bluemart',
'Tag':'Popularity',
'Date':'4 september 2020',
'Content':'Came in news for catching robbers.',
'Link':'https://bluemart.com'
},
{
'Company_name':'tanzet ',
'Title':'data collected on tanzet',
'Tag':'recruitment',
'Date':'6 september 2020',
'Content':'Recruitment of people from development industory.',
'Link':'https://tanzet.com'
}
]

def dash_board(request):
    return render(request, 'blog/home.html')

def about(request):
    return render(request, 'blog/about.html')

def threat_detection(request):
    return render(request, 'blog/threat_detection.html')

def license(request):
    return render(request, 'blog/license.html')

def customer_care(request):
    return render(request, 'blog/customer_care.html')

def notification(request):
    context={
        'signals':data_generated
    }
    return render(request, 'blog/notification.html', context)

def results(request):
    return render(request, 'blog/results.html')

def target_finder(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        form = NameForm(request.POST)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            country = form.cleaned_data['country']
            company = form.cleaned_data['company']

            print("1")        
            print("country: " + country)    
            print("company: " + company)    

            return render(request, 'blog/results.html')
    # if a GET (or any other method) we'll create a blank form
    else:
         form = NameForm()
        
  
    return render(request, 'blog/target_finder.html', {'form': form})


