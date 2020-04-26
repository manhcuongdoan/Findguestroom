from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('properties/', views.contact, name='properties'),
    path('news/', views.contact, name='news'),
]

urlpatterns += [
    path('myHouseAds/', views.HouseAdsByHouseOwnerListView.as_view(),
                name='my-houseAds')
]
