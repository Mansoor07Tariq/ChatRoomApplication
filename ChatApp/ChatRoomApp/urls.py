from django.urls import path
from . import views

urlpatterns = [
    path('create-room/', views.create_room, name='create_room'),
    path('', views.rooms, name='rooms'),  # Add name attribute for the rooms view
    path("<str:slug>/", views.room, name='room'),  # Add name attribute for the room view
        path("enter-room/<str:slug>/", views.enter_room, name='enter_room'),  # Add this URL pattern

]
