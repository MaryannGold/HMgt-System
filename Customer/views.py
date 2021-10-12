from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.core.mail import EmailMessage

# Create your views here.


@login_required
def hotel_dashboard(request):
    return render(request, 'customer/dashboard.html')


@login_required
def guest(request):
    template = 'Customer/guest.html'
    return render(request, template)