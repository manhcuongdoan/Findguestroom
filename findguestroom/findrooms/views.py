from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import json
# Create your views here.

from findrooms.models import HouseAd, HouseOwner
# about = {"about": "this is about page"}
# contact = ""

def index(request):
    """ View function for home page of site. """
    num_house_ads = HouseAd.objects.all().count()
    num_house_owners = HouseOwner.objects.all().count()

    # Number of visits to this view, as counted in the session
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    house_ads = HouseAd.objects.all()[:10]

    context = {
        'num_house_ads': num_house_ads,
        'num_house_owners': num_house_owners,
        'num_visits': num_visits,
        'house_ads': house_ads,
    }
    
    return render(request, 'index.html', context=context)

def about(request):
    # return render(request, 'about.html')
    about = {"about": "about page"}
    return JsonResponse(about)

def contact(request):
    contact = {"contact": "contact page"}
    return JsonResponse(contact)
