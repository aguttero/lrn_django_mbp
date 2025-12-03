from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
#from django.template.loader import render_to_string
from django.http import Http404 #can remove HttpResponse if not used


# Create your views here.


def home(request):
    return HttpResponse("fn home ok")

def test():
    return "This is the fn text output value"

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
    #"dec": "go sailing",
    "dec": None
}

# TEST CODE
# dict_keys = list( monthly_content_dict.keys())
# print ("dict_keys", dict_keys[6])
# print ("dict_keys type", type(dict_keys))


def index_old(request):
    list_items_str = ""
    months_list = list(monthly_content_dict.keys())
    for month in months_list:
        month_path = reverse("month_url", args=[month])
        list_items_str += f'<li><a href="{month_path}">{month.capitalize()}</a></li>'
    # print("list_items_str:", list_items_str)
    response_data = f"<ol>{list_items_str}</ol>"
    return HttpResponse(response_data)

def index(request):
    months_list = list(monthly_content_dict.keys())
    return render (request, "challenges/index.html", {
        "months_list" : months_list,
    }) # pasa la variable month_list al template


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
        # response_data = f"<h2>{challenge_text}</h2>"
        # VRS 01 response_data = render_to_string('challenges/challenge.html')
        # VRS 01 return HttpResponse(response_data)
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            # V01 "month_name": month.capitalize(),
            "month_name": month,

        })
    except:
        # V01 - HARDCODED -> return HttpResponseNotFound("This is the text for the 404 -> month not supported")
        # V02 - render to string with 404.html template -> import render_to_string
        # V02 response_data = render_to_string("404.html")
        # V02 return HttpResponseNotFound (response_data)
        # V03 with django 404 handler -> import Http404
        raise Http404() # looks for '404.html' in any templates folder - only works if Debuf = False in settings.py