from django.db import models

# Create your models here.
class Target_Finder_Input(models.Model):
    alliances = models.BooleanField(max_length=500)
    #alternativeEngines = models.BooleanField(max_length=500)
    #capacityIncrease = models.BooleanField(max_length=500)
    #companyLaunch = models.BooleanField(max_length=500)
    #corporateFinance = models.BooleanField(max_length=500)
    #corporateMA = models.BooleanField(max_length=500)
    #humanResource = models.BooleanField(max_length=500)
    #presicionTechnology = models.BooleanField(max_length=500)
    #innovation = models.BooleanField(max_length=500)
    #productLaunches = models.BooleanField(max_length=500)
    #productUpgrades = models.BooleanField(max_length=500)
    #reporting = models.BooleanField(max_length=500)
    #strategy = models.BooleanField(max_length=500)



COLOR_CHOICES = (
    ('green','GREEN'),
    ('blue', 'BLUE'),
    ('red','RED'),
    ('orange','ORANGE'),
    ('black','BLACK'),
)

class MyModel(models.Model):
  color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')
