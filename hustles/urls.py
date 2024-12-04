from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('employer_add/', views.create_employer, name='employer_add'),
    path('worker_add', views.create_employee, name='worker_add'),
    path('gig_add', views.create_gig, name='gig_add'),

]



#media handler
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)