from django import template

from Hotel.models import HotelProfile, HotelPictures

register = template.Library()


@register.filter
def get_pictures(pk):
    return HotelPictures.objects.filter(hotel_id=int(pk))[:1]
