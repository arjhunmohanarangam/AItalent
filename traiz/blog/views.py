from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import NameForm, Proritize_Indicato, DateForm, MyModelForm
import csv
from blog import models
from .models import MyModel
import pandas as pd
import matplotlib.pyplot as plt
from nltk.tokenize import sent_tokenize
import re
from wordcloud import WordCloud, STOPWORDS
import io
import urllib, base64
import json


data_updated=pd.read_excel("blog/updated.xlsx")
countries_var=""
company=""
keyword_Search=""

# integration funtion global variables 
selected_country_data= ""
comcloud=""
comsignal=""
#Infocator global variables
charrty = ""
alternativeEngines = ""
capacityIncrease = ""
companyLaunch = ""
corporateFinance = ""
corporateMA = ""
humanResource = ""
presicionTechnology = ""
innovation = ""
productLaunches = ""
productUpgrades = ""
reporting =  ""
strategy = ""

varialeAlliance = ""
varialealternativeEngines = ""
varialecapacityIncrease = ""
varialecompanyLaunch = ""
varialecorporateFinance = ""
varialecorporateMA = ""
varialehumanResource = ""
varialepresicionTechnology = ""
varialeinnovation = ""
varialeproductLaunches = ""
varialeproductUpgrades = ""
varialereporting = ""
varialestrategy = ""
varialeNegaive = ""
varialePositive = ""
varialeIndustry = ""


Variable_FORM=[]
Keys_FORM=[]
Indicator_FORM =[]
Indicator_RESULT = []

#context = {'primary_type': primary_type, 'columns': columns}
#df2 = pd.read_csv("blog\Company_data_base.CSV")
#print(df2.columns.tolist())
#print (df2)
#columns2 = df2.columns
#primary_type2 = df2['company'].unique()
#context = {'primary_type': primary_type, 'columns': columns}

def dash_board(request):

        # if this is a POST request we need to process the form data
    if request.method == 'POST':
        date = DateForm(request.POST)
        print(request.POST)

        if date.is_valid():
            #country = form.cleaned_data['country']
            #company = form.cleaned_data['company']
            #industry = form.cleaned_data['industry']
            #segment_Spezialication = form.cleaned_data['segment_Spezialication']
            #main_Market = form.cleaned_data['main_Market']
            #keyword_Search = form.cleaned_data['keyword_Search']
            print('input from dashboard page:')
            country = date.cleaned_data['country']
            company = date.cleaned_data['company']
            print('Country:' + country)
            print(company)
            date1= request.POST.getlist('date') # retruns the timefram as ['date', 'date']
            print(date1)
            print(request.POST)


    else:
         date = DateForm()

    return render(request, 'blog/home.html',
     {'date': date,
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
    if request.method == 'GET':
        integration()
        return comcloud

    if request.method == 'POST':
        date = DateForm(request.POST)
        char_1 = Proritize_Indicato(request.POST)
        print(request.POST)


        if date.is_valid() or char_1.is_valid() :
            print('input from result page:')
            date1= request.POST.getlist('date')
            date2 = request.POST.getlist('date2')
            print(date1)
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


               #print( 'alliance:' + str(request.POST.getlist('alliances')))
        if request.POST.getlist('alliances'):
                    varialeAlliance = 'Alliance'
                    Indicator_RESULT.append(varialeAlliance)

        if request.POST.getlist('alternativeEngines'):
                    varialealternativeEngines = 'Alternative Engines'
                    Indicator_RESULT.append(varialealternativeEngines)


        if request.POST.getlist('capacityIncrease'):
                    varialecapacityIncrease = 'Capacity Increase'
                    Indicator_RESULT.append(varialecapacityIncrease)

        if request.POST.getlist('companyLaunch'):
                    varialecompanyLaunch = 'Company Launch'
                    Indicator_RESULT.append(varialecompanyLaunch)

        if request.POST.getlist('corporateFinance'):
                    varialecorporateFinance = 'Corporate Finance'
                    Indicator_RESULT.append(varialecorporateFinance)

        if request.POST.getlist('corporateMA'):
                    varialecorporateMA = 'Corporate M&A'
                    Indicator_RESULT.append(varialecorporateMA)

        if request.POST.getlist('humanResource'):
                    varialehumanResource = 'Human Resource'
                    Indicator_RESULT.append(varialehumanResource)

        if request.POST.getlist('presicionTechnology'):
                    varialepresicionTechnology = 'Presicion Technology'
                    Indicator_RESULT.append(varialepresicionTechnology)

        if request.POST.getlist('innovation'):
                    varialeinnovation = 'Innovation'
                    Indicator_RESULT.append(varialeinnovation)

        if request.POST.getlist('productLaunches'):
                    varialeproductLaunches = 'Product Launch'
                    Indicator_RESULT.append(varialeproductLaunches)

        if request.POST.getlist('productUpgrades'):
                    varialeproductUpgrades = 'Product Upgrade'
                    Indicator_RESULT.append(varialeproductUpgrades)

        if request.POST.getlist('reporting'):
                    varialereporting = 'Reporting'
                    Indicator_RESULT.append(varialereporting)

        if request.POST.getlist('strategy'):
                    varialestrategy = 'Strategy'
                    Indicator_RESULT.append(varialestrategy)

        if request.POST.getlist('Negative_Development'):
                    varialeNegaive = 'Negative Development'
                    Indicator_RESULT.append(varialeNegaive)

        if request.POST.getlist('Positive_Development'):
                    varialePositive = 'Positive Development'
                    Indicator_RESULT.append(varialePositive)

        if request.POST.getlist('Industry'):
                    varialeIndustry = 'Industry'
                    Indicator_RESULT.append(varialeIndustry)


        print(Indicator_RESULT)



    else:
        date = DateForm()
        char_1 = Proritize_Indicato()



    return render(request, 'blog/results.html', {
        'date' : date,
        'char_1': char_1,
    })


def target_finder(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        form = NameForm(request.POST)
        char_1 = Proritize_Indicato(request.POST)
        date = DateForm(request.POST)
        model = MyModelForm(request.POST)




        if form.is_valid() or char_1.is_valid() or model.is_valid():

                industry = form.cleaned_data['industry']
                segment_Spezialication = form.cleaned_data['segment_Spezialication']
                main_Market = form.cleaned_data['main_Market']
                keyword_Search = form.cleaned_data['keyword_Search']
                Keys_FORM.append(keyword_Search.split(","))
                countries_var = request.POST.getlist('Countries')
                company_var = request.POST.getlist('Companies')

                #Variable_FORM[0]=countries_var
                #Variable_FORM.append(countries_var)
                Variable_FORM.append([countries_var[0],company_var[0]])



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




                #print(country)
                #print(company)
                #print(industry)
                #print(segment_Spezialication)
                #print(main_Market)
                #print(keyword_Search)


                #print(request.POST)
                #print( 'alliance:' + str(request.POST.getlist('alliances')))
                if request.POST.getlist('alliances'):
                    varialeAlliance = 'Alliances'
                    Indicator_FORM.append(varialeAlliance)

                if request.POST.getlist('alternativeEngines'):
                    varialealternativeEngines = 'Alternative Engines'
                    Indicator_FORM.append(varialealternativeEngines)


                if request.POST.getlist('capacityIncrease'):
                    varialecapacityIncrease = 'Capacity Increase'
                    Indicator_FORM.append(varialecapacityIncrease)

                if request.POST.getlist('companyLaunch'):
                    varialecompanyLaunch = 'Company Launch'
                    Indicator_FORM.append(varialecompanyLaunch)

                if request.POST.getlist('corporateFinance'):
                    varialecorporateFinance = 'Corporate Finance'
                    Indicator_FORM.append(varialecorporateFinance)

                if request.POST.getlist('corporateMA'):
                    varialecorporateMA = 'Corporate M&A'
                    Indicator_FORM.append(varialecorporateMA)

                if request.POST.getlist('humanResource'):
                    varialehumanResource = 'Human Resources'
                    Indicator_FORM.append(varialehumanResource)

                if request.POST.getlist('presicionTechnology'):
                    varialepresicionTechnology = 'Precision Technology'
                    Indicator_FORM.append(varialepresicionTechnology)

                if request.POST.getlist('innovation'):
                    varialeinnovation = 'Innovation'
                    Indicator_FORM.append(varialeinnovation)

                if request.POST.getlist('productLaunches'):
                    varialeproductLaunches = 'Product Launches'
                    Indicator_FORM.append(varialeproductLaunches)

                if request.POST.getlist('productUpgrades'):
                    varialeproductUpgrades = 'Product Upgrades'
                    Indicator_FORM.append(varialeproductUpgrades)

                if request.POST.getlist('reporting'):
                    varialereporting = 'Reporting'
                    Indicator_FORM.append(varialereporting)

                if request.POST.getlist('strategy'):
                    varialestrategy = 'Strategy'
                    Indicator_FORM.append(varialestrategy)

                if request.POST.getlist('Negative_Development'):
                    varialeNegaive = 'Negative Development'
                    Indicator_FORM.append(varialeNegaive)

                if request.POST.getlist('Positive_Development'):
                    varialePositive = 'Positive Development'
                    Indicator_FORM.append(varialePositive)

                if request.POST.getlist('Industry'):
                    varialeIndustry = 'Industry'
                    Indicator_FORM.append(varialeIndustry)

                #Indicator_FORM.append([varialeAlliance[0], varialealternativeEngines[0], varialecapacityIncrease[0], varialecompanyLaunch[0], varialecorporateFinance[0], varialecorporateMA, varialehumanResource, varialepresicionTechnology, varialeinnovation, varialeproductLaunches, varialeproductUpgrades, varialereporting, varialestrategy])
                a,b,c,d, e = integration()


                #integration()
                return render(request, 'blog/results.html', {
                         'date' : date,
                        'char_1': char_1,
                        "comcloud": b,
                        "comnumber": c,
                        "comsignal": d, 
                        "value": e
                })

    # if a GET (or any other method) we'll create a blank form
    else:
         form = NameForm()
         char_1 = Proritize_Indicato()
         model = MyModelForm()



    return render(request, 'blog/target_finder.html', {
        'form': form,
        'char_1': char_1,
        'model' : model

    })




def integration():

    
    #print(Variable_FORM)
    #print(Keys_FORM)
    #print(Indicator_FORM)
    selected_country_data=data_updated[data_updated["Name (Country)"]==Variable_FORM[0][0]]
    selected_company_data=selected_country_data[selected_country_data["Name (Organization)"]==Variable_FORM[0][1]]
    if selected_company_data.empty:
        message="no companyies found"
    result = pd.DataFrame()
    for i in Indicator_FORM:
        dada=selected_country_data[selected_country_data["Name (Source Tag)"]== i]
        result=pd.concat([result,dada])
    Wn=len(Indicator_FORM)
    unique_comp=result["Name (Organization)"].unique()
    #print(unique_comp)
    bn=0
    comp_name=[]
    number_signals=[]
    comp_score=[]
    sig=[]
    for comp in unique_comp:
        df_Comp=result[result["Name (Organization)"]==comp]
        #new code for listing the content 
        textclo=[]
        resl=df_Comp["Content"]
        for txt in resl:
            sent=sent_tokenize(txt)
            #print(sent)
            for sen in sent:
                if sen not in textclo:
                    textclo.append(sen)

        #print(textclo)
        sentan=" ".join(textclo)
        Sn=df_Comp["Name (Organization)"].count()
        for item in Indicator_FORM:
            item1=df_Comp[df_Comp["Name (Source Tag)"]== item]
            value=item1["Name (Organization)"].count()
            if value > 0:
                bn=bn+1
        score= Sn*0.8+Sn*0.2*bn/Wn #score calculation
        comp_name.append(comp)
        number_signals.append(Sn)
        comp_score.append(score)
        sig.append(sentan)
        #print("Bn value=",bn)
        #print("Sn value=",Sn)
        #print("Wn value=", Wn)
        bn=0
        #print(score)
    data_new = {'Company_name':comp_name,
        'Number_of_signals':number_signals,
        'Score':comp_score, 
        'Signal':sig
        }#new dataframe for only the output

    score_data = pd.DataFrame(data_new)
    score_data=score_data.sort_values(by=['Score'], ascending=False)


    fig = plt.figure(figsize=(20,10))
    ax1 = fig.add_subplot(121)
    ax1.bar(score_data["Company_name"],score_data["Score"])
    plt.xticks(rotation=50)
    plt.xlabel("Country of Origin")
    plt.ylabel("Number of Wines")
    plt.savefig('books_read.png')
    #print(selected_company_data)
    score_data=score_data.drop(['Score'], axis=1)
    score_data_new=score_data.drop(['Number_of_signals'], axis=1)
    print(score_data)
    #cloud("Claas")
    del Variable_FORM[0]
    del Keys_FORM[0]
    del Indicator_FORM[0:]
    #print(score_data.Company_name)
    #print(score_data.Number_of_signals)
    josonObject = score_data.to_json(orient="table")
    parsed = json.loads(josonObject)
    dumped = json.dumps(parsed, indent=4)

    josonObject_new = score_data_new.to_json(orient="table")
    parsed_new = json.loads(josonObject)
    dumped_new = json.dumps(parsed, indent=4)

    #print(parsed["data"])
    comcloud = [] 
    comnumber = []
    comsignal = []

    for i in parsed["data"]:
        comcloud.append(i["Company_name"]) 
        comnumber.append(i["Number_of_signals"])
        comsignal.append(i["Signal"])

    print(comcloud)
    print(comnumber)
    print(comsignal)
    # we need to install json 

    value=zip(comcloud, comsignal)
    return score_data, comcloud, comnumber, comsignal, value

def cloud(companyname):
    selected_country_data=data_updated[data_updated["Name (Country)"]==Variable_FORM[0][0]]
    selected_company_data=selected_country_data[selected_country_data["Name (Organization)"]==companyname]
    result = pd.DataFrame()
    #print(Indicator_FORM)
    for i in Indicator_FORM:
        dada=selected_company_data[selected_company_data["Name (Source Tag)"]== i]
        #print(dada)
        result=pd.concat([result,dada])
    #print(result["Content"])
    textclo=[]
    resl=result["Content"]
    for txt in resl:
        sent=sent_tokenize(txt)
        #print(sent)
        for sen in sent:
            textclo.append(sen)
    #print(textclo)
    sentan=" ".join(textclo)
    #print(sentan)
    #text = re.sub(r'==.*?==+', '', sentan)
    #plt.figure(figsize=(40, 30))
    wc = WordCloud().generate(sentan)
    plt.figure(figsize=(40, 30))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.savefig('books_read1.png')
    image = io.BytesIO()
    plt.savefig(image, format='png')
    image.seek(0)  # rewind the data
    string = base64.b64encode(image.read())

    image_64 = 'data:image/png;base64,' + urllib.parse.quote(string)
    return image_64


def cloud_gen(request):
    '''Your code'''

    wordcloud = word_cloud(text)
    #return render(request, 'articles/index.html', {'wordcloud':wordcloud}

def halloWelt():
        return [(score_data.Company_name, score_data.Number_of_signals)]







