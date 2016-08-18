from django.conf.urls import url
from . import views #Including views from the current directory

app_name = 'music'

#Here i'm adding sections to my music app
urlpatterns = [
	url(r'^$',views.index,name='index'),
	url(r'^(?P<album_id>[0-9]+)/$',views.detail,name='detail'),
	url(r'^(?P<album_id>[0-9]+)/favourite/$',views.favourite,name='favourite'),
]
