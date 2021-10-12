from django import template

from Hotel.models import RoomPictures

register = template.Library()


@register.filter
def get_pictures(pk):
    return RoomPictures.objects.filter(roomcategory_id=int(pk))


@register.filter
def get_first_pictures(pk):
    return RoomPictures.objects.filter(roomcategory_id=int(pk))[:1]
