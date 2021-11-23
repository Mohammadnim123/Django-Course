from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse
# from django.template.loader import render_to_string # old mehtod

monthly_challenges = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at least 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at least 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at least 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at least 20 minutes every day!"
}

# Create your views here.

def index(req):
   months = [*monthly_challenges]
   return render(req,"challenges/index.html",{
      "months" : months
   })
   
   



def numaric_handler(request,month): #my logic lesson 22 (modren one)
   by_index = [*monthly_challenges]
   
   if(month>len(by_index)):
      
      return HttpResponseNotFound("<h1>This month is not supported!</h1>")

   
   else:
      output = by_index[month - 1]
         
      return HttpResponseRedirect(output)







def months_handler(req,month):

   #old mehtod for static
   # response_data = render_to_string("challenges/index.html",{text: anything you want}) 
   # return HttpResponse(response_data)

   
   
   return render(req,"challenges/month.html",{
      "text" : monthly_challenges[month],
      # "month": month.capitalize(), #instead of using it like this we can use title filter which is refere to DTL in HTML file
      
      "month":month
   })

