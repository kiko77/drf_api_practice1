from django.core.exceptions import ValidationError
from rest_framework import serializers

def validate_image_size(value):

    # file size
    img_size = value.size
    size_max = 20*1024*1024
    if img_size > size_max:
        raise ValidationError("error: max image size is 20Mb")
    
    # file format
    img_name = value.name
    if img_name[-4:] not in ['.jpg', 'png']:
        raise ValidationError("error: image format should be .jpg or .png")
    
    return value


def validate_video_size(value):

    # file size
    video_size = value.size
    size_max = 20*1024*1024
    size_min = 1.5*1024*1024
    if video_size > size_max:
        raise ValidationError("error: max video size is 20Mb")
    elif video_size < size_min:
        raise serializers.ValidationError('error: min video size is 1.5Mb')
    
    # file name
    video_name = value.name
    if video_name[-4:] not in ['.mp4', 'mkv']:
        raise ValidationError("error: video format should be .mp4 or .mkv")
    
    return value