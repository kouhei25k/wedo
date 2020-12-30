from django.urls import path

from . import views

app_name = 'chat'

urlpatterns = [
    path('', views.index, name='index'),
    path('test', views.test, name='test'),
    path('room/<str:room_name>/', views.room, name='room'),
    path('createroom/', views.createroom, name='createroom'),
    path('add_friend/', views.add_friend, name='add_friend'),
    path('room/<str:room_name>/edit/add_menber/',
         views.add_menber, name='add_menber'),
    path('room/<str:room_name>/edit/', views.room_edit, name='room_edit'),

]
