
from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=100)
    video_file = models.FileField(upload_to='videos/')

class Subtitle(models.Model):
    video = models.OneToOneField(Video, on_delete=models.CASCADE, primary_key=True)
    text = models.TextField()
    timestamp = models.DecimalField(max_digits=10, decimal_places=3)

    def __str__(self):
        return f"Subtitle for {self.video.title} - {self.timestamp}"

