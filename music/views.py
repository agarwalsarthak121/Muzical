from .models import Album,Song
from django.shortcuts import render,get_object_or_404
from django.http import Http404
from .forms import PostForm,SongForm,UserForm
from django.shortcuts import redirect
from django.contrib.auth import authenticate,login,logout


IMAGE_FILE_TYPES = ['png', 'jpg', 'jpeg']

def index(request):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		all_albums = Album.objects.filter(user=request.user)
		context = {'all_albums':all_albums,}
		return render(request,'music/index.html',context)

def detail(request,album_id):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		album = get_object_or_404(Album,pk=album_id)
		context = {'album':album,}
		return render(request,'music/detail.html',context)

def songs(request):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		album_list = Album.objects.filter(user=request.user)
		return render(request,'music/songs.html',{'album_list':album_list})

def new(request):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		form = PostForm(request.POST or None, request.FILES or None)
		if form.is_valid():
			album = form.save(commit=False)
			album.user = request.user
			album.album_logo = request.FILES['album_logo']
			album.save()
			return redirect('music:detail', album_id=album.pk)
		context = {
            "form": form,
        }
		return render(request, 'music/new.html', context)

def edit(request, album_id):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		album = get_object_or_404(Album, pk=album_id)
		if request.method == "POST":
			form = PostForm(request.POST,request.FILES, instance=album)
			if form.is_valid():
				album = form.save(commit=False)
				album.save()
				return redirect('music:detail', album_id=album.pk)
		else:
			form = PostForm(instance=album)
		return render(request, 'music/edit.html', {'form': form})

def delete_album(request,album_id):
	album = get_object_or_404(Album, pk=album_id)
	album.delete()
	return redirect('music:index')

def addSong(request,album_id):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		form = SongForm(request.POST or None, request.FILES or None)
		album = get_object_or_404(Album, pk=album_id)
		if form.is_valid():
			albums_songs = album.song_set.all()
			for s in albums_songs:
				if s.song_title == form.cleaned_data.get("song_title"):
					context = {
                    'album': album,
                    'form': form,
                    'error_message': 'You already added that song',
                	}
				return render(request, 'music/addSong.html', context)
			song = form.save(commit=False)
			song.album = album
			song.save()
			return render(request, 'music/detail.html', {'album': album})

		context = {
        'album': album,
        'form': form,
    	}
		return render(request, 'music/addSong.html', context)

def deleteSong(request,album_id,song_id):
	song = Song.objects.get(pk=song_id)
	album = get_object_or_404(Album, pk=album_id)
	song.delete()
	return redirect('music:detail',album_id=album.pk)

def favouriteSong(request,album_id,song_id):
	song = Song.objects.get(pk=song_id)
	album = get_object_or_404(Album, pk=album_id)
	if (song.is_favourite):
		song.is_favourite = False
	else:
		song.is_favourite = True
	song.save()
	return redirect('music:detail',album_id=album.pk)

def favouriteAlbum(request,album_id):
	album = get_object_or_404(Album,pk=album_id)
	if (album.is_favourite):
		album.is_favourite = False
	else:
		album.is_favourite = True
	album.save()
	return redirect('music:index')


def editSong(request, album_id,song_id):
	if not request.user.is_authenticated():
		return redirect( 'music:login_user')
	else:
		song = get_object_or_404(Song, pk=song_id)
		album = get_object_or_404(Album,pk=album_id)
		if request.method == "POST":
			form = SongForm(request.POST,request.FILES, instance=song)
			if form.is_valid():
				song = form.save(commit=False)
				song.save()
				return redirect('music:detail', album_id=album.pk)
		else:
			form = SongForm(instance=song)
		return render(request, 'music/editSong.html', {'form': form})

def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'music/login.html', context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_albums = Album.objects.filter(user=request.user)
                return redirect('music:index')
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')

def register(request):
    form = UserForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_albums = Album.objects.filter(user=request.user)
                return redirect('music:index')
    context = {
        "form": form,
    }
    return render(request, 'music/register.html', context)
