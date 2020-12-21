from django import forms

class NameForm(forms.Form):
    country = forms.CharField(label='Country:', max_length=100)
    company = forms.CharField(label='Company:', max_length=100)
    company = forms.CharField(label='Company:', max_length=100)




    
