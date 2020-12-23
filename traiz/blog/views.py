from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm, Proritize_Indicato, DateForm
import csv

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
        # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        form = NameForm(request.POST)
        date = DateForm(request.POST)

        if form.is_valid():
            country = form.cleaned_data['country']
            company = form.cleaned_data['company']
            industry = form.cleaned_data['industry']
            segment_Spezialication = form.cleaned_data['segment_Spezialication']
            main_Market = form.cleaned_data['main_Market']
            keyword_Search = form.cleaned_data['keyword_Search']
            print (request.POST.getlist('date'))
            print("Company: " + company + '_cut_') 
            print("industry: " + industry + '_cut_')    
            print("segment: " + segment_Spezialication + '_cut_')   
            print("main Market: " + main_Market + '_cut_')    
            print("Keywords: " + keyword_Search + '_cut_') 
            #print(request.POST)
            #print( 'alliance:' + str(request.POST.getlist('alliances')))
            #if request.POST.getlist('alliances'): 
            #  varialeAlliance = 'alliance'
            #  print('Indicator:' + varialeAlliance + '_cut_')

    else:
         form = NameForm()
         date = DateForm()

    return render(request, 'blog/home.html', {
        'form': form, 
        'date' : date
    })

    if date.is_valid():
        date = request.POST.getlist('date')
        date = date.cleaned_data()
        print(date)

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

def results(request):        # if this is a POST request we need to process the form data
        # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        form = NameForm(request.POST)
        date = DateForm(request.POST)

        if form.is_valid():
            country = form.cleaned_data['country']
            company = form.cleaned_data['company']
            industry = form.cleaned_data['industry']
            segment_Spezialication = form.cleaned_data['segment_Spezialication']
            main_Market = form.cleaned_data['main_Market']
            keyword_Search = form.cleaned_data['keyword_Search']
            print (request.POST.getlist('date'))
            print("Company: " + company + '_cut_') 
            print("industry: " + industry + '_cut_')    
            print("segment: " + segment_Spezialication + '_cut_')   
            print("main Market: " + main_Market + '_cut_')    
            print("Keywords: " + keyword_Search + '_cut_') 
            #print(request.POST)
            #print( 'alliance:' + str(request.POST.getlist('alliances')))
            #if request.POST.getlist('alliances'): 
            #  varialeAlliance = 'alliance'
            #  print('Indicator:' + varialeAlliance + '_cut_')

    else:
         form = NameForm()
         date = DateForm()

    return render(request, 'blog/results.html', {
        'form': form, 
        'date' : date
    })

    if date.is_valid():
        date = request.POST.getlist('date')
        date = date.cleaned_data()
        print(date)

def target_finder(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST': 
        form = NameForm(request.POST)
        char_1 = Proritize_Indicato(request.POST)
        date = DateForm(request.POST)
        

        if form.is_valid() or char_1.is_valid():
            country = form.cleaned_data['country']
            company = form.cleaned_data['company']
            industry = form.cleaned_data['industry']
            segment_Spezialication = form.cleaned_data['segment_Spezialication']
            main_Market = form.cleaned_data['main_Market']
            keyword_Search = form.cleaned_data['keyword_Search']
            charrty = char_1['alliances']
            print("Company: " + company + '_cut_') 
            print("industry: " + industry + '_cut_')    
            print("segment: " + segment_Spezialication + '_cut_')   
            print("main Market: " + main_Market + '_cut_')    
            print("Keywords: " + keyword_Search + '_cut_') 
            #print(request.POST)
            #print( 'alliance:' + str(request.POST.getlist('alliances')))
            if request.POST.getlist('alliances'): 
                varialeAlliance = 'alliance'
                print('Indicator:' + varialeAlliance + '_cut_')
            return render(request, 'blog/results.html', {
                    'form': form, 
                    'date' : date
                })

    # if a GET (or any other method) we'll create a blank form
    else:
         form = NameForm()
         char_1 = Proritize_Indicato()
         date = DateForm()

  
    return render(request, 'blog/target_finder.html', {
        'form': form,
        'char_1': char_1})




