from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.


def home(request):
    return HttpResponse("fn home ok")


monthly_content_dict = {
    "jan": "Eat no meat",
    "feb": "walk 60 minutes",
    "mar": "study 28 minutes",
    "apr": "go cycling",
    "may": "go trekking",
    "jun": "go swimming",
    "jul": "go yoga",
    "aug": "go dancing",
    "set": "learn django",
    "oct": "go running",
    "nov": "play paddle",
    "dec": "go sailing",
}

# TEST CODE
# dict_keys = list( monthly_content_dict.keys())
# print ("dict_keys", dict_keys[6])
# print ("dict_keys type", type(dict_keys))


def index(request):
    list_items_str = ""
    # new_list = new item for item in list
    months = list(monthly_content_dict.keys())
    for month in months:
        month_path = reverse("month_url", args=[month])
        list_items_str += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    #print("list_items_str:", list_items_str)
    response_data = list_items_str
    return HttpResponse (response_data)


def monthly_challenge_number(request, month):
    months = list(monthly_content_dict.keys())
    if month > len(months) or month < 1:
        return HttpResponseNotFound("Invalid Month")
    redirect_month = months[month-1]
    # print ("list:", list (monthly_content_dict.keys()))
    # print ("month -1", month-1)
    # print ("month -1 type ", type(month-1))
    # Como evitar el harcoded del "/challenges/" en V0
    # import from django.urls import reverse
    # add name parameter in urls.py
    # add reverse function
    redirect_path = reverse(
        "month_url", args=[redirect_month])  # /challenge/jan
    return HttpResponseRedirect(redirect_path)
    # V0 -> return HttpResponseRedirect("/challenges/" + redirect_month )
    # monthly_challenge(request, months[month-1]) -> esto no anda

# # def monthly_challenge_int(request, month):
#     print("request:", request)
#     print("month:", month)
#     print("month type:", type(month))
#     return HttpResponse(month)


def monthly_challenge(request, month):
    # print("request:", request)
    # print("month:", month)
    # print("month type:", type(month))
    try:
        challenge_text = monthly_content_dict[month]
        response_data = f"<h2>{challenge_text}</h2>"
        return HttpResponse(response_data)
    except:
        return HttpResponseNotFound("This is the text for the 404 -> month not supported")

   # V01 of fn, before of the dictionary solution
    # if month == "jan":
    #     response_text = "fn montly_challenge -> jan response ok"
    # elif month == "feb":
    #     response_text = "fn montly_challenge -> feb response ok"
    # elif month == "mar":
    #     response_text = "fn montly_challenge -> mar response ok"
    # else:
    #     return HttpResponseNotFound("This is the text for the 404 -> month not supported")
    # return HttpResponse(response_text)
