from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, Group, Permission
from .models import UserInfo
from django.http import HttpResponse
from django.contrib.auth import login as dj_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.auth import authenticate, login as auth_login, logout
from django.urls.base import reverse

from Account.permissions import get_content_type


def register(request):
    return render(request, 'Account/register.html', {'type': 'guest'})


def hotel_register(request):
    return render(request, 'Account/register.html', {'type': 'hotel_owner'})


def save_register(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        firstname1 = firstname.lower()
        lastname = request.POST['last_name']
        lastname1 = lastname.lower()
        middlename = request.POST['middle_name']
        middlename1 = middlename.lower()
        email = request.POST['email']
        email = email.lower()
        phonenumber = request.POST['telephoneNumber']
        address = request.POST['address']
        username = request.POST['username']
        username1 = username.lower()
        password = request.POST['password']
        password1 = password.lower()
        confirmpassword = request.POST['confirm_password']
        type = request.POST['type']
        # confirmpassword1 = confirmpassword.lower()
        if firstname == "" or middlename == "" or lastname == "" or email == "" or phonenumber == "" or address == "" or username == "" \
                or password == "" or confirmpassword == "":
            messages.success(request, 'All Field is Required.')
            return redirect('Account:register')
        else:
            user = User.objects.filter(username=username1).exists()
            if user:
                messages.success(request, 'User already exist.')
                return redirect('Account:register')
            elif password == confirmpassword and len(phonenumber) == 11:
                createuser = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                                                       username=username, password=password, is_active=False)

                createuser.save()
                if type == 'guest':
                    create_profile = UserInfo.objects.create(user_id=createuser.id, telephoneNumber=phonenumber,
                                                             address=address, middle_name=middlename1, user_type='Guest')
                    create_profile.save()
                    # This part will assign permissions
                    assign_user_permission(create_profile.user)

                    # my_group = Group.objects.get(name='Guest')
                    # createuser.groups.add(my_group)

                elif type == 'hotel_owner':
                    create_profile = UserInfo.objects.create(user_id=createuser.id, telephoneNumber=phonenumber,
                                                             address=address, middle_name=middlename1,
                                                             user_type='Hotel Admin')
                    create_profile.save()
                    # This part will assign permissions
                    assign_user_permission(create_profile.user)

                    # my_group = Group.objects.get(name='Hotel Admin')
                    # createuser.groups.add(my_group)
                # my_group.user_set.add(createuser)
                print('Profile created')
                current_site = get_current_site(request)
                message = render_to_string('Account/email.html', {
                    'user': createuser,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(createuser.pk)).decode(),
                    'token': account_activation_token.make_token(createuser),
                })
                mail_subject = 'Activate your account.'
                to_email = email
                send_email = EmailMessage(mail_subject, message, to=[to_email])
                send_email.send()
                return HttpResponse('Please check your email address to complete the registration')
                # messages.success(request, 'User Successfully registered')
                # return redirect('Frontend:homepage')
            else:
                messages.success(request, 'both password do not match or phone_Number not up to 11.')
                return redirect('Account:register')


def login(request):
    return render(request, 'Account/login.html')

def loginn(request):
    if request.method == "POST":
        username1 = request.POST['username']
        password1 = request.POST['password']

        user = authenticate(username=username1, password=password1)
        if user is not None:
            if user.is_active:
                #log user in
                auth_login(request, user)
                return redirect('Frontend:homepage')
        else:
            messages.warning(request, 'username or password does not match')
            return redirect('Account:login')


@login_required
def choose_profile(request):
    user = request.user
    if user.is_superuser:
        return redirect(reverse('Customer:padmin'))
    elif user.has_perm('Account.hotel'):
        return redirect(reverse('Customer:hotel_dashboard'))
    elif user.has_perm('Account.guest'):
        return redirect(reverse('Customer:guest_dashboard'))
    elif user.has_perm('Account.receptionist'):
        return redirect(reverse('Customer:receptionist_dashboard'))


def logout_view(request):
    logout(request)
    return redirect('Frontend:homepage')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        # print(uid)
        # print('-----------')
        # print(token)
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        dj_login(request, user)
        # return redirect('home')
        messages.success(request, 'Thank you for your email confirmation. Now you can login your account.')
        return redirect('Account:login')
    else:
        return HttpResponse('Activation link is invalid!')


@login_required
def assign_user_permission(user):
    ct = get_content_type()
    if not ct:
        return
    a = User.objects.get(pk=user.id)
    user_info = UserInfo.objects.get(user=a)
    if user_info.user_type == 'Guest':
        user.has_perm('Account.guest')
        permission = Permission.objects.get(
            codename='guest',
            content_type=ct
        )
        user.user_permissions.add(permission)
    elif user_info.user_type == 'Hotel Admin':
        user.has_perm('Account.hotel')
        permission = Permission.objects.get(
            codename='hotel',
            content_type=ct
        )
        user.user_permissions.add(permission)
    user.save()


