from django.urls import path
from . import views

urlpatterns = [

    
    # path("<month>", views.months_handler),  #for all lesson 19

    path("<int:month>", views.numaric_handler),
    path("<str:month>", views.months_handler),
    
]