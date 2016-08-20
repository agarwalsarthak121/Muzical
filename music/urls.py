from django.conf.urls import url
from . import views #Including views from the current directory

app_name = 'music'

#Here i'm adding sections to my music app
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'songs$',views.songs,name='songs'),
	url(r'album/new$',views.new,name='new'),
	url(r'^(?P<album_id>[0-9]+)/edit$',views.edit,name='edit'),
	url(r'^(?P<album_id>[0-9]+)/delete$',views.delete_album,name='delete'),
	url(r'^(?P<album_id>[0-9]+)/addSong$',views.addSong,name='addSong'),
	url(r'^(?P<album_id>[0-9]+)/favouriteAlbum$',views.favouriteAlbum,name='favouriteAlbum'),
	url(r'^(?P<album_id>[0-9]+)/(?P<song_id>[0-9]+)/deleteSong$',views.deleteSong,name='deleteSong'),
	url(r'^(?P<album_id>[0-9]+)/(?P<song_id>[0-9]+)/favouriteSong',views.favouriteSong,name='favouriteSong'),
	url(r'^(?P<album_id>[0-9]+)/(?P<song_id>[0-9]+)/editSong',views.editSong,name='editSong'),
	url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

]
