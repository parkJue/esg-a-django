from django import forms
from blog.models import Restaurant

class RestForm(forms.ModelForm):
    class Meta:
        model = Restaurant
        fields = "__all__"