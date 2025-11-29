from django.urls import path
from . import views

## path converter
urlpatterns = [
    path("", views.home),
    path("<int:month>", views.monthly_challenge_int),
    path("<str:month>", views.monthly_challenge),
    # path("january", views.january),
    # path("february", views.february),
]
