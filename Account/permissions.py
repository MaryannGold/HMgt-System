from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType

from Account.models import UserInfo
from website import constants


def get_content_type():
    try:
        return ContentType.objects.get_for_model(UserInfo)
    except:
        return None


def create_default_permissions():
    ct = get_content_type()
    if not ct:
        return
    Permission.objects.get_or_create(codename='hotel', name='Hotel Admin', content_type=ct)
    Permission.objects.get_or_create(codename='guest', name='Guest', content_type=ct)
    Permission.objects.get_or_create(codename='receptionist', name='Receptionist', content_type=ct)


create_default_permissions()


def get_user_type(user):
    if user.is_superuser:
        return constants.SUPERUSER
    if user.has_perm('account.hotel'):
        return constants.HOTEL_ADMIN
    if user.has_perm('account.guest'):
        return constants.GUEST
    if user.has_perm('account.receptionist'):
        return constants.RECEPTIONIST
