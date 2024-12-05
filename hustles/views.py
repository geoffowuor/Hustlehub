from django.shortcuts import render,redirect,get_object_or_404
from .forms import employerForm, employeeForm, gigForm,applicationForm
from .models import gig, employee, application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


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
            return redirect('boss')  
    else:
        form = employerForm()
    return render(request, 'boss_profile_add.html', {'form': form})

def create_employee(request):
    if request.method == 'POST':
        form = employeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('worker_dash')
    else:
        form = employeeForm()
    return render(request, 'emp_profile_add.html', {'form': form})

def create_gig(request):
    if request.method == 'POST':
        form = gigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('boss_dash')
    else:
        form = gigForm()
    return render(request, 'gig_add.html', {'form': form})

#gig lists
def list_gigs(request):
    gigs = gig.objects.filter(status='Open').order_by('-date_posted')  
    return render(request, 'list_gigs.html', {'gigs': gigs})

def gig_details(request, gig_id):
    gig = get_object_or_404(gig, id=gig_id)
    return render(request, 'gig_details.html', {'gig': gig})

#gig application

def apply_for_gig(request, gig_id):
    gig = get_object_or_404(gig, id=gig_id)  
    employee = employee.objects.get(emp_name=request.user.username)  

    if request.method == 'POST':
        form = applicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.gig = gig
            application.employee = employee
            application.save()
            return redirect('gig_list')  
    else:
        form = applicationForm()

    return render(request, 'apply_for_gig.html', {'form': form, 'gig': gig})

def edit_application(request, application_id):
    application = get_object_or_404(application, id=application_id)
    if request.method == 'POST':
        form = applicationForm(request.POST, instance=application)
        if form.is_valid():
            form.save()
            messages.success(request, 'Application updated successfully.')
            return redirect('admin_applications')  
    else:
        form = applicationForm(instance=application)
    return render(request, 'edit_application.html', {'form': form, 'application': application})


# Delete an application
def delete_application(request, application_id):
    application = get_object_or_404(application, id=application_id)
    if request.method == 'POST':
        application.delete()
        messages.success(request, 'Application deleted successfully.')
        return redirect('admin_applications')  
    return render(request, 'delete_application.html', {'application': application})

#employee view for his applications
def employee_applications(request):
    employee = request.user.employee  
    applications = application.objects.filter(employee=employee).order_by('-application_date')
    return render(request, 'employee_applications.html', {'applications': applications})


#boss view applications
def employer_applications(request):
    employer = request.user.employer  
    applications = application.objects.filter(gig__employer=employer).order_by('-application_date')
    return render(request, 'employer_applications.html', {'applications': applications})

#action on applications
def respond_application(request, application_id):
    application = get_object_or_404(application, id=application_id, gig__employer=request.user.employer)
    if request.method == 'POST':
        new_status = request.POST.get('status')
        if new_status in ['Pending', 'Accepted', 'Rejected']:
            application.status = new_status
            application.save()
            return redirect('employer_applications')
    return render(request, 'respond_application.html', {'application': application})

