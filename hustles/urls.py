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
    path('success/', views.success, name='application_success'),
    path('add', views.create_gig, name='add_gig'),
    path('dashboard/', views.dash_boss, name="dash_boss"),
    path('applications/', views.employer_applications, name='applications'),
    path('application/<int:application_id>/respond/', views.respond_application, name='respond_application'),
    path('gigs/', views.list_gigs, name='list_gigs'),
    path('gig/<int:pk>/edit/', views.edit_gig, name='edit'),
    path('gig/<int:pk>/delete/', views.delete_gig, name='gig-delete'),
    path('apply/<int:gig_id>/', views.apply_for_gig, name="apply"),


]



#media handler
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)