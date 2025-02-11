from django.urls import path
from . import views
from .constant import MONTHLY_CHALLENGE_BY_NUMBER, MONTHLY_CHALLENGE, INDEX

# List all urls we want to support
urlpatterns = [
    path("", view=views.index, name=INDEX),
    # path("challenges/") # No need with the prefix "challenges"
    path("<int:month>", view=views.monthly_challenge_by_number, name=MONTHLY_CHALLENGE_BY_NUMBER),
    path("<str:month>", view=views.monthly_challenge, name=MONTHLY_CHALLENGE),
]
