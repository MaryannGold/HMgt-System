from django.urls import path, re_path
from Account import views

app_name = 'Account'
urlpatterns = [
    path('register', views.register, name='register'),
    path('hotel_register', views.hotel_register, name='hotel_register'),
    path('save_register', views.save_register, name='save_register'),
    re_path(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
            views.activate, name='activate'),
    path('login', views.login, name='login'),
    path('loginn', views.loginn, name='loginn'),
    path('logout_view', views.logout_view, name='logout_view'),
    path('profile/', views.choose_profile, name='choose_profile'),


]

