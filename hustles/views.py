from django.shortcuts import render,redirect,get_object_or_404
from .forms import  gigForm,applicationForm
from .models import gig, application
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def success(request):
    return render(request, 'application_success.html')

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
            return redirect('add_gig')  # Redirect to a dashboard
        else:
            messages.error(request, 'Invalid username or password!')
    return render(request, 'accounts/login.html')



@login_required
def create_gig(request):
    if request.method == 'POST':
        form = gigForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dash_boss')
    else:
        form = gigForm()
    return render(request, 'gig_add.html', {'form': form})

# View for editing a gig

def edit_gig(request, pk):
    gig_instance = get_object_or_404(gig, pk=pk)  # Fetch gig by pk

    if request.method == 'POST':
        # Update gig instance with form data
        gig_instance.name = request.POST['name']
        gig_instance.rate = request.POST['rate']
        gig_instance.description = request.POST['description']
        gig_instance.skill = request.POST['skill']
        gig_instance.location = request.POST['location']
        gig_instance.save()
        return redirect('dash_boss')  # Replace with the appropriate success URL

    return render(request, 'gig_edit.html', {'gig': gig_instance})

# View for deleting a gig
def delete_gig(request, pk):
    gig_instance = get_object_or_404(gig, pk=pk)
    if request.method == 'POST':
        gig_instance.delete()
        return redirect('dash_boss')  # Redirect to your list view
    return render(request, 'gig_confirm_delete.html', {'gig': gig_instance})

#gig lists
def list_gigs(request):
    gigs = gig.objects.order_by('-date_posted')  
    return render(request, 'list_gigs.html', {'gigs': gigs})

def dash_boss(request):
    gigs = gig.objects.order_by('-date_posted')  
    return render(request, 'boss.html', {'gigs': gigs})

#gig application

def apply_for_gig(request, gig_id):
    gig_instance = get_object_or_404(gig, id=gig_id)  
    if request.method == 'POST':
        form = applicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.gig = gig_instance
            application.save()
            return redirect('application_success')  
    else:
        form = applicationForm()

    return render(request, 'apply_for_gig.html', {'form': form, 'gig': gig_instance})



#boss view applications
def employer_applications(request):
    #employer = request.user.employer  
    applications = application.objects.order_by('-application_date')
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

