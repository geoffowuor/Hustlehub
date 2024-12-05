from django import forms
from .models import employer, employee, gig,application

class employerForm(forms.ModelForm):
    class Meta:
        model = employer
        fields = '__all__'

class employeeForm(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'

class gigForm(forms.ModelForm):
    class Meta:
        model = gig
        fields = '__all__'
        
        
#gig application

class applicationForm(forms.ModelForm):
    class Meta:
        model = application
        fields = ['cover_letter'] 