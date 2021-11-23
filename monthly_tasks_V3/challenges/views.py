from django.shortcuts import render
from django.http import HttpResponse , HttpResponseNotFound , HttpResponseRedirect
from django.urls import reverse

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
   li_str = ""
   months_list = [*monthly_challenges]
   for month in months_list:
      href = reverse("month-challenge",args=[month])
      li_str += f"<li><a href=\"{month}\">{month.capitalize()}</a></li>"
   res = f"<ul>{li_str}</ul>"
   return HttpResponse(res)



def numaric_handler(request,month): #my logic lesson 22 (modren one)
   by_index = [*monthly_challenges]
   
   if(month>len(by_index)):
      
      return HttpResponseNotFound("<h1>This month is not supported!</h1>")

   
   else:
      output = by_index[month - 1]
         
      return HttpResponseRedirect(output)


# def monthly_challenge_by_number(request, month): #old solution from lesson 23
#     months = list(monthly_challenges.keys())

#     if month > len(months):
#         return HttpResponseNotFound("Invalid month")

#     redirect_month = months[month - 1]
#     redirect_path = reverse("month-challenge",args=[redirect_month])  # /challenge/january
#     return HttpResponseRedirect(redirect_path)


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
      path = reverse("challenge-home")
      response_data = f"""<h1>{monthly_challenges[month]}</h1>
      <a href=\"{path}\">back to home</a>
      """
      return HttpResponse(response_data)
   except:
      return HttpResponseNotFound("<h1>This month is not supported!</h1>")