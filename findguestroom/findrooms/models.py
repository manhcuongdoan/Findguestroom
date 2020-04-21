from django.db import models

# Create your models here.
from django.contrib.auth.models import User
from datetime import date
from django.urls import reverse
import os
from django.conf import settings

import uuid # for unique house ad

class HouseAd(models.Model):
    """ Model representing house ad from HouseOwner """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4,
                            help_text="ID duy nhất cho bài đăng tin này trong \
                                        cả cơ sở dữ liệu")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200,
                            help_text="Nhập ngắn gọn nội dung nhà bạn cho thuê")
    # location in Hanoi, Da Nang, TP Ho chi Minh quận ? , đường ?
    province = models.CharField(max_length=100,
                            help_text="Tỉnh, thành phố")
    district = models.CharField(max_length=100,
                            help_text="Quận, huyện")
    locationDetail = models.CharField(max_length=200,
                            help_text="Số nhà, tên đường, ...")

    # price = per month
    price = models.IntegerField(help_text="Giá cho thuê mỗi tháng, \
                                tối đa 5 triệu")

    # area = m2
    area = models.IntegerField(help_text="Tổng diện tích cho thuê \
                                (phòng ngủ, vệ sinh, ...) bằng mét vuông")
    # bed room image < 10 MB
    livingroomImage = models.ImageField(upload_to="findrooms/media")

    # # bathroom or restroom image < 10 MB
    # bathroomImage = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    #
    # # other images maximum 4 < 10 MB per image
    # houseImage1 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    # houseImage2 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    # houseImage3 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)
    # houseImage4 = models.ImageField(upload_to=settings.MEDIA_ROOT, blank=True)

    content = models.TextField(max_length=1000,
                            help_text="Miêu tả cụ thể nội dung nhà bạn cho thuê")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """ Returns the url to access a house ad instance"""
        return reverse('houseAd-detail', args=[str(self.id)])
