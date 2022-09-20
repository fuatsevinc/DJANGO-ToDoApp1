from django import forms
from .models import Todos

class ListForm(forms.ModelForm):
    class Meta:
        model = Todos
        fields = ["title", "content",  "finished", "date"]


