from django.urls import path

from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
]

urlpatterns += [
    path('myHouseAds/', views.HouseAdsByHouseOwnerListView.as_view(),
                name='my-houseAds')
]

# urlpatterns += [
#     path('book/create', views)
# ]
