from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
# Create your models here.

class Host (models.Model):
    host_name = models.CharField(max_length=30)
    host_info = models.TextField()
    host_image = models.ImageField(upload_to='uploads/', verbose_name='Host Image') 
    def __str__(self):
        return self.host_name
class Room (models.Model): 
    title = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default="Khong") 
    publish_date = models.DateTimeField('date published')
    price = models.CharField(max_length=100)
    host_name = models.ForeignKey(Host, on_delete=models.CASCADE)
    describe = RichTextUploadingField(blank=True, null=True)
    room_image = models.ImageField(upload_to='uploads/', verbose_name='Room Image')  
    def __str__(self):
        return self.title

