
from django import forms
from students.models import StudentInfo


class StudentCreateForm(forms.ModelForm):
    class Meta:
        model = StudentInfo
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name  .....'}),
            'age': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Age .....'}),
            'gender': forms.Select(attrs={'class': 'form-control'}),
        }
