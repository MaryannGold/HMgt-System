from django.shortcuts import render, redirect
from django.views.generic import DetailView
from .forms import HotelForm
from django.contrib.auth.decorators import login_required
from Account.models import UserInfo
from django.contrib import messages
from django.urls import reverse
from django.http import HttpResponseRedirect
from .forms import HotelImageForm, RoomCategoriesForm
from .models import HotelPictures, HotelProfile, Room, RoomPictures, RoomCategory


@login_required
def addhotel(request):
    form = HotelForm()
    if request.method == 'POST':
        image_name = request.POST["image"]
        image = request.FILES["image2"]
        admin = UserInfo.objects.get(user=request.user)
        form = HotelForm(request.POST, request.FILES)
        if form.is_valid():
            hotel = form.save(commit=False)
            hotel.admin = admin
            hotel.save()
            addhot = HotelPictures.objects.create(hotel_id=hotel.pk, image_name=image_name, hotel_image=image)
            addhot.save()
            messages.success(request, 'Successfully created Hotel')
            return HttpResponseRedirect(reverse('Hotel:add-image'))
    return render(request, 'Hotel/add-hotel.html', {'form': form})


@login_required
def view_hotels_list(request):
    template = 'Hotel/upload.html'
    user = UserInfo.objects.get(user=request.user)
    hotels = HotelProfile.objects.filter(admin=user)
    return render(request, template, {'hotels': hotels})


@login_required
def details(request, hotel_id):
    user = UserInfo.objects.get(user=request.user)
    hot = HotelProfile.objects.get(pk=int(hotel_id), admin=user)
    messages.success(request, 'Successfully Added Image. Kindly add few other '
                              'Hotel images(i.e Lobby,Swimming pool,Gym etc)')
    return redirect('Hotel:details', hotel_id=hotel_id)


class HotelDetails(DetailView):
    perms_to_check = ['Account.hotel']
    model = HotelProfile
    template_name = 'Hotel/details.html'
    context_object_name = 'hotel'

    def get_context_data(self, **kwargs):
        context = super(HotelDetails, self).get_context_data(**kwargs)
        image = HotelPictures.objects.filter(hotel=self.object) if HotelPictures.objects.filter(hotel=self.object).exists() else None
        context['hotel_image'] = image
        print('-------------------------')
        print(image)
        context['room_types'] = RoomCategory.objects.filter(admin=self.object.admin) if RoomCategory.objects.filter(admin=self.object.admin).exists() else None
        context['room'] = Room.objects.filter(hotel=self.object) if Room.objects.filter(hotel=self.object).exists() else None

        return context


@login_required
def dshboard(request):
    template = 'Profile/dshboard.html'
    return render(request, template)


@login_required
def add_more_image(request, hotel_id):
    if request.method == 'POST':
        image = request.POST['image']
        image2 = request.FILES['image2']
        if image == "" or image2 == "":
            messages.warning(request, 'All Field is Required.')
            return redirect('Hotel:details', pk=hotel_id)
        else:
            save_image = HotelPictures.objects.create(hotel_id=int(hotel_id), image_name=image, hotel_image=image2)
            save_image.save()
            messages.success(request, 'Successfully Added Image. Kindly add more Hotel images'
                                      '(i.e Lobby,Swimming pool,Gym etc)')
            return redirect('Hotel:details', pk=hotel_id)


@login_required
def room_categories(request):
    user = UserInfo.objects.get(user=request.user)
    hotels = HotelProfile.objects.filter(admin=user)
    form = RoomCategoriesForm()
    if request.method == 'POST':
        user = UserInfo.objects.get(user=request.user)
        form = RoomCategoriesForm(request.POST)
        hotel = int(request.POST['hotel'])
        if form.is_valid:
            room_category = form.save(commit=False)
            room_category.hotel_id = hotel
            room_category.admin_id = user.pk
            room_category.save()
            messages.success(request, 'Category successfully created')
            return redirect('Hotel:room-categories')
    return render(request, 'Hotel/room-categories.html', {'form': form,
                                                          'hotels': hotels})


@login_required
def add_room(request, hotel_id):
    if request.method == 'POST':
        roomtype = request.POST['room_type']
        rate = request.POST['room_rate']
        description = request.POST['room_description']
        number = request.POST['room_number']
        imgname = request.POST['room_image_name']
        bed = request.POST['room_bed_type']
        img = request.FILES['room_image']

        if roomtype != '':
            room_cat = RoomCategory.objects.get(category_name=roomtype)

            create_room = Room.objects.create(room_type=room_cat, room_rate=rate, room_description=description,
                                              room_number=number, room_bed_type=bed, hotel_id=int(hotel_id))
            create_room.save()
            create_roompictures = RoomPictures.objects.create(room_image_name=imgname, room_image=img,
                                                              roomcategory=room_cat)
            create_roompictures.save()
        else:
            messages.success(request, 'Kindly go to the roomCategory page and add a category  ')
            return redirect('Hotel:details', pk=int(hotel_id))
        messages.success(request, 'Room successfully created!')
        return redirect('Hotel:details', pk=int(hotel_id))
    return redirect('Hotel:details', pk=int(hotel_id))


@login_required
def add_more_room_image(request, hotel_id):
    if request.method == 'POST':
        room_pk = request.POST['status']
        room_image_name = request.POST['room_image_name']
        room_image = request.FILES['room_image']
        if room_image_name == "" or room_image == "":
            messages.warning(request, 'All Field is Required.')
            return redirect('Hotel:details', pk=hotel_id)
        else:
            save_image = RoomPictures.objects.create(roomcategory_id=int(room_pk), room_image_name=room_image_name,
                                                     room_image=room_image)
            save_image.save()
            messages.success(request, 'Successfully Added Image. You can add few more images)')
            return redirect('Hotel:details', pk=hotel_id)


def locations(request, location):
    state = HotelProfile.objects.filter(location=location)
    template = 'Hotel/locations.html'
    context = {'locations': state}
    return render(request, template, context)


