
from django import forms

from teachers.models import TeacherInfo


class TeacherCreateForm(forms.ModelForm):
    class Meta:
        model = TeacherInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name.....'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Age ....'}),
            'designation': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Designation....'}),
            'phone': forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Phone .......'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }