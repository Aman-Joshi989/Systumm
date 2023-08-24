
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Video, Subtitle
from .serializers import VideoSerializer, SubtitleSerializer
from rest_framework.parsers import FileUploadParser
from rest_framework import status
from rest_framework.decorators import api_view


class UploadVideoView(APIView):
    parser_classes = (FileUploadParser,)
    permission_classes = [IsAuthenticated] 

    def post(self, request):
        video_file = request.data['file']  # Assuming you are using 'file' as the field name
        # Process the video file, save it, and return a response
        return Response({'message': 'Video uploaded successfully'}, status=status.HTTP_201_CREATED)
        

class VideoUploadView(APIView):
    parser_classes = (FileUploadParser,)

    def post(self, request):
        video_file = request.FILES.get('video')
        title = request.data.get('title', '')
        
        if video_file:
            video = Video.objects.create(title=title, video_file=video_file)
            return Response({'message': 'Video uploaded successfully'}, status=201)
        else:
            return Response({'error': 'No video file provided'}, status=400)

class SubtitleCreateView(APIView):
    def post(self, request):
        video_id = request.data.get('video_id')
        text = request.data.get('text', '')
        timestamp = request.data.get('timestamp', 0)
        
        try:
            video = Video.objects.get(id=video_id)
        except Video.DoesNotExist:
            return Response({'error': 'Video not found'}, status=404)
        
        subtitle = Subtitle.objects.create(video=video, text=text, timestamp=timestamp)
        return Response({'message': 'Subtitle created successfully'}, status=201)

class SubtitleRetrieveView(APIView):
    def get(self, request, video_id):
        try:
            subtitles = Subtitle.objects.get(video_id=1)
        except Subtitle.DoesNotExist:
            return Response({'error': 'Subtitles not found'}, status=404)
        
        serializer = SubtitleSerializer(subtitles, many=True)
        return Response(serializer.data)