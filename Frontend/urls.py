"""website URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from Frontend import views

app_name = 'Frontend'
urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('aboutus', views.aboutus, name='aboutus'),
    path('cities', views.cities, name='cities'),
    path('view_more/<int:hotels_id>/', views.view_more, name='view_more'),
    path('<int:category_id>/<hotel_name>/reservation/', views.calendar, name='calendar'),
    path('findcity', views.findcity, name='findcity')

]




