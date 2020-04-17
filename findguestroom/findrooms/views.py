from django.shortcuts import render
from django.http import HttpResponse
from .models import Room
# Create your views here.


def index(request):
    room_list = Room.objects.all()
    context = {
        'room_list': room_list,
    }


    return render(request, 'index.html', context=context)
