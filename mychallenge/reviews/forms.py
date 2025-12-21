from django import forms

class ReviewForm(forms.Form):
    first_name = forms.CharField(max_length=100, required=False, label="F_Name Custom Label")
    last_name = forms.CharField(max_length=100, error_messages={
        "required": "Custom - This field needs a value",
        "max_length": "Custome - Please shorter field"
    })
    review_text = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
    