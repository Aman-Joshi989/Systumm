from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')
    
class Subtitle(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
    timestamp = models.FloatField()
    text = models.TextField()
