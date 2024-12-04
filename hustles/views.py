from django.shortcuts import render,redirect
from .forms import employerForm, employeeForm, gigForm
from .models import employer, employee, gig

# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'boss_profile_add.html')

####################################

def create_employer(request):
    if request.method == 'POST':
        form = employerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Replace with your redirect URL
    else:
        form = employerForm()
    return render(request, 'boss_profile_add.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = employeeForm()
    return render(request, 'emp_profile_add.html', {'form': form})

def create_gig(request):
    if request.method == 'POST':
        form = gigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = gigForm()
    return render(request, 'gig_add.html', {'form': form})