from django.db import models
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator

category_choices = (
    ("Quran", "Quran"),
    ("Hadith", "Hadith"),
    ("Fiqh", "Fiqh"),
    ("Heart Softener", "Heart Softener"),
    ("Biography", "Biography"),
    ("Debate", "Debate"),
    ("Dawah", "Dawah")
)

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Video(models.Model):
    uploader = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='video_uploader')
    video_title = models.CharField(
        max_length=255, verbose_name="Title for your video")
    slug = models.SlugField(max_length=264, unique=True)
    video_link = models.URLField(max_length=264, unique=False)
    video_description = models.TextField(verbose_name="Video description")
    category = models.CharField(
        max_length=255, choices=category_choices, default='Islamic')
    video = models.FileField(upload_to='video-files', verbose_name='video',
                             validators=[FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])])
    video_thumb = models.ImageField(
        upload_to='video_thumbs', verbose_name='thumb')
    publish_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-publish_date']

    def __str__(self):
        return self.video_title


class Comment(models.Model):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='video_comment')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_comment')
    comment = models.TextField()
    comment_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-comment_date']

    def __str__(self):
        return self.comment


class Like(models.Model):
    video = models.ForeignKey(
        Video, on_delete=models.CASCADE, related_name='liked_video')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='liker_user')

    def __str__(self):
        return str(self.user) + " likes " + str(self.video)
