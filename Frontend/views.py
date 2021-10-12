from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from Account.models import UserInfo
from Hotel.models import HotelProfile, HotelPictures,  Room, RoomCategory, RoomPictures, RoomStatus
from Reservation.models import GuestReservation
from django.db.models import Q
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse


def homepage(request):
    return render(request, 'Frontend/home.html')


def aboutus(request):
    return render(request, 'Frontend/about.html')


def cities(request):
    lagos = HotelProfile.objects.filter(location='lagos')
    count_number_lagos = lagos.count()
    abuja = HotelProfile.objects.filter(location='abuja')
    count_number_abuja = abuja.count()
    owerri = HotelProfile.objects.filter(location='owerri')
    count_number_owerri = owerri.count()
    portharcourt = HotelProfile.objects.filter(location='portharcourt')
    count_number_of_portharcourt = portharcourt.count()
    delta = HotelProfile.objects.filter(location='delta')
    count_number_of_delta = delta.count()
    calabar = HotelProfile.objects.filter(location='calabar')
    count_number_of_calabar = calabar.count()
    uyo = HotelProfile.objects.filter(location='uyo')
    count_number_of_uyo = uyo.count()
    enugu = HotelProfile.objects.filter(location='enugu')
    count_number_of_enugu = enugu.count()
    kano = HotelProfile.objects.filter(location='kano')
    count_number_kano = kano.count()
    context = {'count_number_lagos': count_number_lagos, 'count_number_abuja': count_number_abuja,
               'count_number_owerri': count_number_owerri, 'count_number_portharcourt': count_number_of_portharcourt,
               'count_number_delta': count_number_of_delta, 'count_number_calabar': count_number_of_calabar,
               'count_number_uyo': count_number_of_uyo, 'count_number_enugu': count_number_of_enugu,
               'count_number_kano': count_number_kano}
    template = 'Frontend/cities.html'
    return render(request, template, context)


def view_more(request, hotels_id):
    get_hotel = HotelPictures.objects.filter(hotel__id=hotels_id)
    hotel_name = HotelProfile.objects.get(pk=int(hotels_id))
    room_category = RoomCategory.objects.filter(hotel_id=hotels_id).order_by('pk')
    context = {'get_hotel': get_hotel, 'room_category': room_category, 'hotel_name': hotel_name}
    return render(request, 'Frontend/view_more.html', context)


def calendar(request, category_id, hotel_name):
    current_user = request.user
    get_name = RoomCategory.objects.filter(pk=int(category_id))
    check_room = Room.objects.filter(room_type__in=get_name)
    if request.method == 'POST':
        check_In_Date = request.POST["date_in"]
        check_Out_Date = request.POST["date_out"]
        how_many_guests = request.POST["num_of_guests"]
        additional_request = request.POST["additional_info"]
        payment_type = request.POST["payment_type"]
        for rooms in check_room:
            if RoomStatus.objects.filter(starting_Date=check_In_Date,
                                         ending_Date=check_Out_Date,
                                         room_id=rooms.pk, occupationStatus='Occupied').exists():
                continue
            else:
                create_room_status = RoomStatus.objects.create(occupationStatus='Occupied',
                                                               starting_Date=check_In_Date,
                                                               ending_Date=check_Out_Date,
                                                               room_id=rooms.pk)
                create_room_status.save()
                user_info = UserInfo.objects.get(user=current_user)
                create_reservation = GuestReservation.objects.create(guest_id=user_info.pk, check_In_Date=check_In_Date,
                                                                     check_Out_Date=check_Out_Date,
                                                                     how_many_guests=how_many_guests,
                                                                     additional_request=additional_request,
                                                                     reserved_room_id=create_room_status.pk,
                                                                     payment_type=payment_type)
                create_reservation.save()
                msg = u'Successfully reserved room %s for %s' % (rooms.room_number, user_info.user.last_name)
                messages.success(request, msg)
                return HttpResponseRedirect(reverse('Frontend:calendar', kwargs={'category_id': category_id,
                                                                                 'hotel_name': hotel_name}))
        else:
            messages.warning(request, 'All rooms are currently occupied')
            return HttpResponseRedirect(reverse('Frontend:calendar', kwargs={'category_id': category_id,
                                                                             'hotel_name': hotel_name}))

    return render(request, 'Frontend/calendar.html', {'category_id': category_id, 'hotel_name': hotel_name})


def findcity(request):
    if request.method == 'POST':
        check_cities = request.POST["cities"]
        if HotelProfile.objects.filter(location=check_cities).exists():
            check_for_city = HotelProfile.objects.filter(location=check_cities)
            count_hotel = check_for_city.count()
            context = {
                'check_for_city': check_for_city,
                'count_hotel': count_hotel
            }
            return render(request, 'Frontend/findcity.html', context)
        else:
            messages.warning(request, 'City Unavailable')
            return redirect(request, 'Frontend:home')


#def display_actions(request,category_id):
 #   current_user = request.user
  #  get_identity = RoomCategory.objects.filter(pk=int(category_id))
   # context = {'current_user': current_user, 'get_identity': get_identity}
# return render(request, 'Frontend/display_actions.html', context)


