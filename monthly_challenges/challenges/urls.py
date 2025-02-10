from django.urls import path
from . import views

# List all urls we want to support
urlpatterns = [
    # path("challenges/") # No need with the prefix "challenges"
    path("<int:month>", view=views.monthly_challenge_by_number, name="monthly_challenge_by_number"),
    path("<str:month>", view=views.monthly_challenge, name="monthly_challenge"),
]
