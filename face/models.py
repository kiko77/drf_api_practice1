from django.db import models
from face.validators import validate_image_size, validate_video_size
from face.storage import OverwriteStorage
import os
from django.utils.deconstruct import deconstructible
@deconstructible
class upload_location(object):
    def __init__(self, sub_path):
        self.path = sub_path

    def __call__(self, instance, filename):
        return os.path.join(self.path, filename)


class Image(models.Model):
    type = models.TextField(default='image')
    media_filename = models.FileField(storage=OverwriteStorage(), upload_to=upload_location('image/'), blank=True, null=True, validators=[validate_image_size])   
    uid = models.TextField(blank=True)
    upload_timestamp = models.DateTimeField(auto_now_add=True)
    
    def save(self, *args, **kwargs):
        self.uid= self.media_filename.name.split(".")[-2]
        super().save(*args, **kwargs)

    class Meta:
        db_table = "image"



class Video(models.Model):
    type = models.TextField(default='video')
    media_filename = models.FileField(storage=OverwriteStorage(), upload_to=upload_location('video/'), blank=True, null=True, validators=[validate_video_size])   
    uid = models.TextField(blank=True)
    upload_timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        self.uid= self.media_filename.name.split(".")[-2]
        super().save(*args, **kwargs)

    class Meta:
        db_table = "video"