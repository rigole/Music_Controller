from django.urls import path
from .views import RoomView, CreateRoomView, GetRoom, UserInRoom


urlpatterns = [
    path('home', RoomView.as_view()),
    path('create-room', CreateRoomView.as_view()),
    path('get-room', GetRoom.as_view()),
    path('user-in-room', UserInRoom.as_view())

 ]