from django import forms
from .models import *


class FormJuice(forms.Form):
    all = Company.objects.all()
    # mas = []
    # for a in all:
    #     mas.append((a.id, a.title))
    # firma = forms.ChoiceField(choices=tuple(mas))
    firma = forms.ModelChoiceField(queryset=Company.objects.values_list('title', flat=True))