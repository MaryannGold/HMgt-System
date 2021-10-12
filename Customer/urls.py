from django.urls import path, re_path
from Customer import views

app_name = 'Customer'
urlpatterns = [
    path('hotel/dashboard', views.hotel_dashboard, name='hotel_dashboard'),
    path('guest/dashboard', views.guest, name='guest_dashboard')

]

