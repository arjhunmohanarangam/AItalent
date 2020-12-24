from django.shortcuts import render
from django.http import HttpResponse
from .forms import NameForm, Proritize_Indicato, DateForm
import csv
from blog import models 

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

        if date.is_valid():
            #country = form.cleaned_data['country']
            #company = form.cleaned_data['company']
            #industry = form.cleaned_data['industry']
            #segment_Spezialication = form.cleaned_data['segment_Spezialication']
            #main_Market = form.cleaned_data['main_Market']
            #keyword_Search = form.cleaned_data['keyword_Search']
            date1= request.POST.getlist('date')
            date2 = request.POST.getlist('date2')
            dashboard_object = {"From": date1,
                                "To": date2, 
                               }

            print (dashboard_object)

    else:
         form = NameForm()
         date = DateForm()

    return render(request, 'blog/home.html', {
        'form': form, 
        'date' : date
    })



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

        #if form.is_valid():
            #country = form.cleaned_data['country']
            # company = form.cleaned_data['company']
            #industry = form.cleaned_data['industry']
            # segment_Spezialication = form.cleaned_data['segment_Spezialication']
            #main_Market = form.cleaned_data['main_Market']
            #keyword_Search = form.cleaned_data['keyword_Search']
            #print (request.POST.getlist('date'))
            #print("Company: " + company + '_cut_') 
            #print("industry: " + industry + '_cut_')    
            #print("segment: " + segment_Spezialication + '_cut_')   
            #print("main Market: " + main_Market + '_cut_')    
            #print("Keywords: " + keyword_Search + '_cut_') 
            #print(request.POST)
            #print( 'alliance:' + str(request.POST.getlist('alliances')))
            #if request.POST.getlist('alliances'): 
            #  varialeAlliance = 'alliance'
            #  print('Indicator:' + varialeAlliance + '_cut_')
        if date.is_valid():
            date1= request.POST.getlist('date')
            date2 = request.POST.getlist('date2')
            dashboard_object = {"From": date1,
                                "To": date2, 
                               }

            print (dashboard_object)

    else:
         form = NameForm()
         date = DateForm()

    return render(request, 'blog/results.html', {
        'form': form, 
        'date' : date
    })

    

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
            alternativeEngines = char_1['alternativeEngines']
            capacityIncrease = char_1['capacityIncrease']
            companyLaunch = char_1['companyLaunch']
            corporateFinance = char_1['corporateFinance'] 
            corporateMA = char_1['corporateMA']
            humanResource = char_1['humanResource']
            presicionTechnology = char_1['presicionTechnology']
            innovation = char_1['innovation']
            productLaunches = char_1['productLaunches']
            productUpgrades = char_1['productUpgrades']
            reporting =  char_1['reporting']
            strategy = char_1['strategy']

           

            #print(request.POST)
            #print( 'alliance:' + str(request.POST.getlist('alliances')))
            if request.POST.getlist('alliances'): 
                varialeAlliance = 'Alliance'
                print('Indicator:' + varialeAlliance )

            if request.POST.getlist('alternativeEngines'): 
                varialealternativeEngines = 'Alternative Engines'
                print('Indicator:' + varialealternativeEngines)

            if request.POST.getlist('capacityIncrease'): 
                varialecapacityIncrease = 'Capacity Increase'
                print('Indicator:' + varialecapacityIncrease )
          
            if request.POST.getlist('companyLaunch'): 
                varialecompanyLaunch = 'Company Launch'
                print('Indicator:' + varialecompanyLaunch)
            
            if request.POST.getlist('corporateFinance'): 
                varialecorporateFinance = 'Corporate Finance'
                print('Indicator:' + varialecorporateFinance )
            
            if request.POST.getlist('corporateMA'): 
                varialecorporateMA = 'Corporate M&A'
                print('Indicator:' + varialecorporateMA )

            if request.POST.getlist('humanResource'): 
                varialehumanResource = 'Human Resource'
                print('Indicator:' + varialehumanResource )

            if request.POST.getlist('presicionTechnology'): 
                varialepresicionTechnology = 'Presicion Technology'
                print('Indicator:' + varialepresicionTechnology )

            if request.POST.getlist('innovation'): 
                varialeinnovation = 'Innovation'
                print('Indicator:' + varialeinnovation )

            if request.POST.getlist('productLaunches'): 
                varialeproductLaunches = 'Product Launch'
                print('Indicator:' + varialeproductLaunches ) 

            if request.POST.getlist('productUpgrades'): 
                varialeproductUpgrades = 'Product Upgrade'
                print('Indicator:' + varialeproductUpgrades )

            if request.POST.getlist('reporting'): 
                varialereporting = 'Reporting'
                print('Indicator:' + varialereporting )  

            if request.POST.getlist('strategy'): 
                varialestrategy = 'Strategy'
                print('Indicator:' + varialestrategy)  
            

            target_finder_object = { 
                                "Country: " : country,
                                "Company: " : company, 
                                "industry: " : industry,     
                                "segment: " : segment_Spezialication,  
                                "main Market: " : main_Market,  
                                "Keywords: " : keyword_Search, 

                                #'alliances': varialeAlliance ,
                                #'alternativeEngines':  varialealternativeEngines ,  
                                #'capacityIncrease' : varialecapacityIncrease , 
                                #'companyLaunch' : varialecompanyLaunch , 
                                #'corporateFinance' :  varialecorporateFinance , 
                                #'corporateMA' :   varialecorporateMA , 
                                #'humanResource' :   varialehumanResource , 
                                #'presicionTechnology' : varialepresicionTechnology , 
                                #'innovation' :  varialeinnovation , 
                                #'productLaunches' : varialeproductLaunches , 
                                #'productUpgrades' :  varialeproductUpgrades , 
                                #'reporting' : varialereporting , 
                                #'strategy' :  varialestrategy  } 
            }

            print (target_finder_object)


            return render(request, 'blog/results.html', {
                    'form': form, 
                    'date' : date
                })

            ins = varialeAlliance
            ins.save()

            
       

    # if a GET (or any other method) we'll create a blank form
    else:
         form = NameForm()
         char_1 = Proritize_Indicato()
         date = DateForm()

  
    return render(request, 'blog/target_finder.html', {
        'form': form,
        'char_1': char_1})

    if date.is_valid():
        date1= request.POST.getlist('date')
        date2 = request.POST.getlist('date2')
        print(date1)
        print(date2)

        results_object = {"From": date1,
                          "To": date2}
                             

        print (results_object)
      


