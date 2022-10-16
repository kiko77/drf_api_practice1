# Create your views here.
from face.models import Image, Video
from face.serializers import ImageSerializer, VideoSerializer
from django.http import FileResponse
from rest_framework.response import Response
from rest_framework import viewsets


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    Response(ImageSerializer.data)

    def list(self, request):
        if request.method == 'GET':
            data_list = ImageSerializer(self.get_queryset(), many=True).data
            for data in data_list: 
                data['media_filename'] = data['media_filename'].split("/")[-1]  # del dir_name in path
                del data['upload_timestamp']    # del upload_timestamp
            return Response(data_list)
    
    def create(self, request):
        if request.method == 'POST':
            f_name = '{}{}'.format('image/', request.data['media_filename'])
            exist_data = Image.objects.filter(media_filename=f_name).first()
            if exist_data:
                serializer = ImageSerializer(exist_data, data=request.data) # update data if filename already exist
            else:
                serializer = ImageSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            return Response(serializer.errors["media_filename"], status=400)




class VideoViewSet(viewsets.ModelViewSet):
    queryset = Video.objects.all()
    serializer_class = VideoSerializer
    Response(VideoSerializer.data)
    
    def list(self, request):
        if request.method == 'GET':
            data_list = ImageSerializer(self.get_queryset(), many=True).data
            for data in data_list: 
                data['media_filename'] = data['media_filename'].split("/")[-1]
                del data['upload_timestamp']
            return Response(data_list)
    
    def create(self, request):
        if request.method == 'POST':
            f_name = '{}{}'.format('video/', request.data['media_filename'])
            exist_data = Video.objects.filter(media_filename=f_name).first()
            if exist_data:
                serializer = VideoSerializer(exist_data, data=request.data)
            else:
                serializer = VideoSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(status=200)
            return Response(serializer.errors["media_filename"], status=400)


def ImageDownloadViewSet(request, filename):
    img = open('image/'+filename, 'rb')
    return FileResponse(img)

def VideoDownloadViewSet(request, filename):
    video = open('video/'+filename, 'rb')
    return FileResponse(video)