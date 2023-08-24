from django.urls import path, include
from . import views
from .views import VideoUploadView, SubtitleCreateView, SubtitleRetrieveView, UploadVideoView

urlpatterns = [
    path('upload/', VideoUploadView.as_view(), name='video-upload'),
    path('subtitle/create/', SubtitleCreateView.as_view(), name='subtitle-create'),
    path('subtitle/retrieve/<int:video_id>/', SubtitleRetrieveView.as_view(), name='subtitle-retrieve'),
    path('upload-video/', views.UploadVideoView.as_view(), name='upload-video'),
    path('api-auth/', include('rest_framework.urls'))
    
]










