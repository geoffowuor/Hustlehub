from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    #auth urls
    path('accounts/login/', views.login_view, name="login"),
    path('accounts/register', views.register, name="register"),
    #####
    path('employee/applications/', views.employee_applications, name='worker_dash'),
    path('employer_add/', views.create_employer, name='employer_add'),
    path('worker_add', views.create_employee, name='worker_add'),
    path('add', views.create_gig, name='add_gig'),
    path('applications/', views.employer_applications, name='boss_dash'),
    path('application/<int:application_id>/respond/', views.respond_application, name='respond_application'),
    path('gigs/', views.list_gigs, name='list_gigs'),
    path('gigs/<int:gig_id>/', views.gig_details, name='gig_details'),


]



#media handler
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)