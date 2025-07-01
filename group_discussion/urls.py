# gd_app/urls.py
from django.urls import path
from . import views

app_name = 'group_discussion'
urlpatterns = [

    path('create/', views.create_room, name='create_room'),
    path('gd-lobby/', views.gd_lobby, name='gd_lobby'),
    path('join/<str:room_code>/', views.join_room, name='join_room'),
    path('room/<str:room_code>/', views.room_detail, name='room_detail'),
]