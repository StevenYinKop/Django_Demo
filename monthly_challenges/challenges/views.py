from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

months = {
    "january": "Eat no meat for the entire month!",
    "february": "Walk for at least 20 minutes every day!",
    "march": "Learn Django for at leat 20 minutes every day!",
    "april": "Eat no meat for the entire month!",
    "may": "Walk for at least 20 minutes every day!",
    "june": "Learn Django for at leat 20 minutes every day!",
    "july": "Eat no meat for the entire month!",
    "august": "Walk for at least 20 minutes every day!",
    "september": "Learn Django for at leat 20 minutes every day!",
    "october": "Eat no meat for the entire month!",
    "november": "Walk for at least 20 minutes every day!",
    "december": "Learn Django for at leat 20 minutes every day!"
}


def monthly_challenge_by_number(request, month_by_number):
    month_list = list(months.keys())
    month = month_list[month_by_number]
    if month > len(month_list):
        return HttpResponseNotFound("Invalid month")
    return HttpResponseRedirect(f"challenges/monthly_challenge/{month}")


# Create your views here.
# define a python function for a view.
def monthly_challenge(request, month):
    result = ""
    if month == "january":
        result = "Eat no meat for the entire month!"
    elif month == "februray":
        result = "Walk for at least 20 minutes every day!"
    elif month == "march":
        result = "Learn Django for at leat 20 minutes every day!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(result)
