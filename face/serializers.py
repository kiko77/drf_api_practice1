from rest_framework import serializers
from face.models import Image, Video


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('id', 'uid', 'type', 'media_filename', 'upload_timestamp')
        
class VideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Video
        fields = ('id', 'uid', 'type', 'media_filename', 'upload_timestamp')