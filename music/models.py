from django.db import models
from django.contrib.auth.models import Permission, User

class Album(models.Model):
	user = models.ForeignKey(User, default=1)
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=250)
	album_logo = models.FileField()
	is_favourite = models.BooleanField(default=False)

	def __str__(self):
		return self.artist +' - '+self.album_title

class Song(models.Model):
	album = models.ForeignKey(Album,on_delete=models.CASCADE)
	song_title = models.CharField(max_length=250)
	is_favourite = models.BooleanField(default=False)
	audio_file = models.FileField(default='')

	def __str__(self):
		return self.song_title


