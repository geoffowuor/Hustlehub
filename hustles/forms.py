from django import forms
from .models import employer, employee, gig

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