from django.conf.urls import url
from views import UserViewSet, CategoryViewSet, BandViewSet, AlbumViewSet, SongViewSet
from rest_framework.urlpatterns import format_suffix_patterns
from viewset_maps import CustomViewSet, ViewSetType
import views


urlpatterns = [
    url(r'^$', views.api_root),
    url(r'^categories/$', CustomViewSet.register(CategoryViewSet, ViewSetType.GENERIC_LIST) , name='category-list'),
    url(r'^category/(?P<pk>[a-zA-Z0-9]+)/$', CustomViewSet.register(CategoryViewSet, ViewSetType.GENERIC_DETAIL), name='category-detail'),
    url(r'^bands/$', CustomViewSet.register(BandViewSet, ViewSetType.GENERIC_LIST) , name='band-list'),
    url(r'^band/(?P<pk>[a-zA-Z0-9]+)/$', CustomViewSet.register(BandViewSet, ViewSetType.GENERIC_DETAIL), name='band-detail'),
    url(r'^albums/$', CustomViewSet.register(AlbumViewSet, ViewSetType.GENERIC_LIST) , name='album-list'),
    url(r'^album/(?P<pk>[a-zA-Z0-9]+)/$', CustomViewSet.register(AlbumViewSet, ViewSetType.GENERIC_DETAIL), name='album-detail'),
	url(r'^songs/$', CustomViewSet.register(SongViewSet, ViewSetType.GENERIC_LIST) , name='song-list'),
    url(r'^song/(?P<pk>[a-zA-Z0-9]+)/$', CustomViewSet.register(SongViewSet, ViewSetType.GENERIC_DETAIL), name='song-detail'),      
    url(r'^users/$', CustomViewSet.register(UserViewSet, ViewSetType.GENERIC_LIST), name='user-list'),
    url(r'^users/(?P<pk>[a-zA-Z0-9]+)/$', CustomViewSet.register(UserViewSet, ViewSetType.READ_ONLY_DETAIL), name='user-detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)