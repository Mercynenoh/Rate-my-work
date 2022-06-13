from django import forms
from .models import Reviewrating

class ReviewForm(Forms:ModelForm)
    class Meta
    model = Reviewrating
    fields=['subject','reviews', 'ratings']