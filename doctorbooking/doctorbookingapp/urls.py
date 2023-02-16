from django.urls import path

from . import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('avi/', views.avi),
    path('booking/', views.booking),
    path('schedules/', views.schedule),
    path('patientbooking/',views.patientbooking)
]
