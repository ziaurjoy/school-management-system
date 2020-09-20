

from django import forms

class StudentCreateForms(forms.Form):
    name = forms.CharField()
    age = forms.IntegerField()
    select_gender = (
        ('male','Male'),
        ('female','Female')
    )
    gender = forms.ChoiceField(choices=select_gender)
