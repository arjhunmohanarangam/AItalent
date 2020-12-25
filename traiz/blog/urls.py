from django.urls import path
from . import views


urlpatterns = [
    path('', views.dash_board, name="Blog-home"),
    path("about/",views.about,name="Blog-about"),
    path("target_finder/",views.target_finder,name="Blog-target_finder"),
    path("threat_detection/",views.threat_detection,name="Blog-threat_detection"),
    path("license/",views.license,name="Blog-license"),
    path("customer_care/",views.customer_care,name="Blog-customer_care"),
    path("notification/",views.notification,name="Blog-notification"),   
    path("results/",views.results,name="Blog-results"),
]




