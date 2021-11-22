from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect

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



def numaric_handler(request,month): #my logic lesson 22
   by_index = [*monthly_challenges]
   
   if(month>len(by_index)):
      
      return HttpResponseNotFound("this month not found")

   
   else:
      output = by_index[month - 1]
         
      return HttpResponseRedirect(output)



#from lesson 20
# def months_handler(req,month):
#    get_month = None
#    if(month == "jan"):
#       get_month = f"Hello from {month}"
#    elif(month == "feb"):
#       get_month = f"Hello from {month}"
#    elif(month == "mar"):
#       get_month = f"Hello from {month}"
#    else:
#       return HttpResponseNotFound("this month not found")
#    return HttpResponse(get_month)

def months_handler(req,month):
   try:
      output = monthly_challenges[month]
      return HttpResponse(output)
   except:
      return HttpResponseNotFound("this month not found")