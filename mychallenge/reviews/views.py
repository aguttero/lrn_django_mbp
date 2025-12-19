from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import ReviewForm
# Create your views here.

# V01 manual html form
# def review(request):
#     if request.method == 'POST':
#         entered_username = request.POST['form_item_name']
        
#         if entered_username == "":
#             return render(request, "reviews/review.html", {
#                     "has_error": True
#                 })
        
#         print("entered_username:", entered_username)
#         return HttpResponseRedirect ("thank-you")
    
#     return render(request, "reviews/review.html", {
#         "has_error": False
#     })

# V02 django form class
# form_01 = ReviewForm()
# def review(request):
#     return render(request, "reviews/review.html", {
#         "form": form_01
#     })

# V03 django optimized form class
def review(request):
    if request.method == 'POST':
        form_01 = ReviewForm(request.POST)

        if form_01.is_valid():
            print("django form data:", form_01.cleaned_data)
            return HttpResponseRedirect ("thank-you")

    form_01 = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form_01
    })

def thank_you(request):
    return render(request, "reviews/thank_you.html")