from django.shortcuts import render,redirect,get_object_or_404
from .forms import employerForm, employeeForm, gigForm
from .models import employer, employee, gig
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


def test(request):
    return render(request, 'boss_profile_add.html')


# Register view
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']
        if password == password_confirm:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                messages.success(request, 'Account created successfully!')
                return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
    return render(request, 'accounts/register.html')

# Login view
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to a dashboard or homepage
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'accounts/login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')
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