from django.urls import path
from . import views

## path converter
## add name parameter to be able to user reverse and dynamic path building in views.py
urlpatterns = [
    path("", views.home),
    path("<int:month>", views.monthly_challenge_number),
    path("<str:month>", views.monthly_challenge, name="month_url"),
    # path("january", views.january),
    # path("february", views.february),
]