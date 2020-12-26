from django import forms
from blog.models import Target_Finder_Input, MyModel

class NameForm(forms.Form):
    country = forms.CharField(label='Country:', max_length=100, required=False)
    company = forms.CharField(label='Company:', max_length=100, required=False)
    industry = forms.CharField(label='Industry:', max_length=100, required=False)
    segment_Spezialication = forms.CharField(label='Segment/Spezialication:', max_length=100, required=False)
    main_Market = forms.CharField(label='Main Market:', max_length=100, required=False)
    keyword_Search = forms.CharField( widget=forms.Textarea(attrs={"rows":5, "cols":20}), label='keyword_Search:', max_length=100, required=False)


class Proritize_Indicato(forms.ModelForm):
    alliances = forms.BooleanField(label='Alliances', required=False )
    alternativeEngines = forms.BooleanField(label='Alternative Engines', required=False )
    capacityIncrease = forms.BooleanField(label='capacity Increase', required=False )
    companyLaunch = forms.BooleanField(label='Company Launch', required=False )
    corporateFinance = forms.BooleanField(label='Corporate Finance', required=False )
    corporateMA = forms.BooleanField(label='Corporate M&A', required=False )
    humanResource = forms.BooleanField(label='Human Resource', required=False )
    presicionTechnology = forms.BooleanField(label='Presicion Technology', required=False )
    innovation = forms.BooleanField(label='Innovation', required=False )
    productLaunches = forms.BooleanField(label='Product Launches', required=False )
    productUpgrades = forms.BooleanField(label='Product Upgrades', required=False )
    reporting = forms.BooleanField(label='Reporting', required=False)
    strategy = forms.BooleanField(label='Strategy', required=False)

    class Meta: 
      model = Target_Finder_Input
      fields = ('alliances', )
        

class DateInput(forms.DateInput):
      input_type = 'date'



class DateForm(forms.Form):
      date = forms.DateField(label='From ', required= False, widget=DateInput)
      date = forms.DateField(label=' | ', required= False, widget=DateInput)
      #country = forms.CharField(label='Country:',max_length=100, required=False)
      #company = forms.CharField(label='Company:', max_length=100, required=False)


class MyModelForm(forms.ModelForm):
    class Meta:
        model = MyModel
        fields = ['color']

