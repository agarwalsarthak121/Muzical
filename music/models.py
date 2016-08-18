from django.db import models

class Album(models.Model):
	artist = models.CharField(max_length=250)
	album_title = models.CharField(max_length=500)
	genre = models.CharField(max_length=250)
	album_logo = models.CharField(max_length=1000)

	def __str__(self):
		return self.artist +' - '+self.album_title

class Song(models.Model):
	album_name = models.ForeignKey(Album,on_delete=models.CASCADE)
	file_type = models.CharField(max_length=10)
	song_title = models.CharField(max_length=250)
	is_favourite = models.BooleanField(default=False)

	def __str__(self):
		return self.song_title


