
from django import forms
from students.models import StudentClassInfo,StudentShiftInfo


class StudentRegisterationForm(forms.Form):
    roll = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Roll  .....'}))
    english_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name English  .....'}))
    banglali_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Name Banglali  .....'}))
    father_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Father\'s Name  .....'}))
    mother_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mother\'s Name  .....'}))
    present_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Present Address  .....'}))
    permanet_address = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Permanent Address  .....'}))
    date_of_brith = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Date Of Brith .....','type':'date'}))
    gender_choise = (
        ('male','Male'),
        ('female','Female'),
    )
    gender = forms.ChoiceField(choices=gender_choise,widget=forms.Select(attrs={'class': 'form-control'}))

    student_class = forms.ModelChoiceField(queryset=StudentClassInfo.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    student_shift = forms.ModelChoiceField(queryset=StudentShiftInfo.objects.all(),widget=forms.Select(attrs={'class':'form-control'}))
    student_section = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    student_session = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control'}))


    # class Meta:
    #     model = StudentInfo
    #     fields = '__all__'
    #     widgets = {
            # 'roll': forms.NumberInput(attrs={'class': 'form-control','placeholder': 'Roll  .....'}),
            # 'english_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name English  .....'}),
            # 'Bangla_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Name Banglali  .....'}),
            # 'father_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Father\'s Name .....'}),
            # 'mother_name': forms.TextInput(attrs={'class': 'form-control','placeholder': 'Mother\'s Name  .....'}),
            # 'present_address': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Present Address  .....'}),
            # 'permanet_address': forms.Textarea(attrs={'class': 'form-control','placeholder': 'Permanent Address  .....'}),
            # 'date_of_brith': forms.DateInput(attrs={'class': 'form-control','placeholder': 'Date Of Brith .....'}),
            # 'gender': forms.Select(attrs={'class': 'form-control'}),
        # }
