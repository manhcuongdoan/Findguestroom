from django.urls import path

from .views import getAllRooms, getRoom

urlpatterns = [
    path('all', getAllRooms),
    path('<int:pk>', getRoom),

]