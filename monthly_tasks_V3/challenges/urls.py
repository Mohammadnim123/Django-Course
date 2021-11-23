from django.urls import path
from . import views

urlpatterns = [

    
    # path("<month>", views.months_handler),  #for all lesson 19
    path("",views.index,name="challenge-home"),
    path("<int:month>", views.numaric_handler),
    # path("<int:month>", views.monthly_challenge_by_number),
    path("<str:month>", views.months_handler, name="month-challenge")
    
]