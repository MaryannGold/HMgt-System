from django.urls import path
from Hotel import views

app_name = 'Hotel'
urlpatterns = [
    path('add-hotel', views.addhotel, name='add-hotel'),
    path('view/hotels/list', views.view_hotels_list, name='add-image'),
    # path('add-room/<int:hotel_id>/', views.add_room, name='add-room')
    path('view-hotels/<int:pk>/details', views.HotelDetails.as_view(), name='details'),
    path('add-images/<int:hotel_id>/', views.add_more_image, name='add_more_image'),
    path('add-room/<int:hotel_id>/', views.add_room, name='add-room'),
    path('room-categories/', views.room_categories, name='room-categories'),
    path('cities/<location>/', views.locations, name='locations'),
    path('<int:hotel_id>/add-room-images/', views.add_more_room_image, name='add_more_room_image')
    # path('lagos', views.lagos, name='lagos')
]




