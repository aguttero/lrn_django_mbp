from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def january(request):
    return HttpResponse("fn january response ok")

def february(request):
    return HttpResponse("fn february response ok")

def home(request):
    return HttpResponse("fn home ok")

def monthly_challenge_int(request, month):
    print("request:", request)
    print("month:", month)
    print("month type:", type(month))
    return HttpResponse(month)


def monthly_challenge(request, month):
    print("request:", request)
    print("month:", month)
    response_text = None
    if month == "jan":
        response_text = "fn montly_challenge -> jan response ok"
    elif month == "feb":
        response_text = "fn montly_challenge -> feb response ok"
    elif month == "mar":
        response_text = "fn montly_challenge -> mar response ok"
    else:
        return HttpResponseNotFound("This is the text for the 404 -> month not supported")
    return HttpResponse(response_text)