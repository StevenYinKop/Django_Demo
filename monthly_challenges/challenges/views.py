from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from .constant import INDEX, MONTHLY_CHALLENGE_BY_NUMBER, MONTHLY_CHALLENGE, TEMPLATE_PREFIX

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
    "december": None
}


def index(request):
    month_list = list(months.keys())
    return render(request, template_name=TEMPLATE_PREFIX.format("index.html"), context={'months': month_list})


def monthly_challenge_by_number(request, month):
    month_list = list(months.keys())
    if month > len(month_list):
        return HttpResponseNotFound("Invalid month")
    redirect_month = month_list[month - 1]
    redirect_path = reverse(MONTHLY_CHALLENGE, args=[redirect_month])
    # return HttpResponseRedirect(f"challenges/monthly_challenge/{month}")
    return HttpResponseRedirect(redirect_path)


# Create your views here.
# define a python function for a view.
def monthly_challenge(request, month):
    if month in list(months.keys()):
        return render(request,
                      template_name=TEMPLATE_PREFIX.format("challenges.html"),
                      context={'content': months[month], 'month': month})
    else:
        return HttpResponseNotFound("This month is not supported!")
