from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False)
    last_name = forms.CharField(max_length=100)