from django import forms
from .models import Album,Song
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['album_title', 'artist','genre','album_logo']

class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title','audio_file']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']
