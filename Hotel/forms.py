from django import forms
from .models import HotelProfile, HotelPictures, RoomCategory


class HotelForm(forms.ModelForm):
    class Meta:
        model = HotelProfile
        exclude = ('admin',)
        fields = ('hotel_name', 'hotel_address', 'hotel_contact', 'brief_description', 'location')

        widgets = {
            'hotel_name': forms.TextInput(attrs={'class': 'form-control'}),
            #  'hotel_image': forms.FileInput(attrs={'class': 'default form-control'}),
            'hotel_address': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_contact': forms.TextInput(attrs={'class': 'form-control'}),
            'brief_description': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.Select(attrs={'class': 'form-control'})
        }


class HotelImageForm(forms.ModelForm):
    class Meta:
        model = HotelPictures
        exclude = ('Hotel',)
        fields = ('image_name', 'hotel_image')

        widgets = {
            'image_name': forms.TextInput(attrs={'class': 'form-control'}),
            'hotel_image': forms.FileInput(attrs={'class': 'form-control'})
        }


class RoomCategoriesForm(forms.ModelForm):
    class Meta:
        model = RoomCategory
        exclude = ('admin', 'hotel')
        fields = ['category_name', 'category_descriptions', 'room_rate']

        widgets = {
            'category_name': forms.TextInput(attrs={'class': 'form-control'}),
            'room_rate': forms.TextInput(attrs={'class': 'form-control'}),
            'category_descriptions': forms.Textarea(attrs={'class': 'form-control'})
        }