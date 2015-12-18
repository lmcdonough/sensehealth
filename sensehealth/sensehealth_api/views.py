from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import generics, permissions, viewsets
from sensehealth_api.serializers import UserSerializer, CategorySerializer, BandSerializer, AlbumSerializer, SongSerializer
from sensehealth_api.models import Category, Band, Album, Song
from sensehealth_api.permissions import IsOwnerOrReadOnly, IsOwner
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.reverse import reverse
from rest_framework.permissions import IsAdminUser


@api_view(('GET',))
@permission_classes((permissions.AllowAny,))
def api_root(request, format=None):
    '''returns the endpoints for tha api.'''

    return Response({
        'users': reverse('user-list', request=request, format=format),
        'categories': reverse('category-list', request=request, format=format),
        'bands': reverse('band-list', request=request, format=format),
        'albums': reverse('album-list', request=request, format=format),
        'songs': reverse('song-list', request=request, format=format)         
    })

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset handles all the actions (list create, retreive, update, destroy)
    for the User viewset.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)
    

class CategoryViewSet(viewsets.ModelViewSet):
    """
    This viewset handles all the actions (list create, retreive, update, destroy)
    for the Category viewset.
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer, 
        and assigns the user to the action'''

        serializer.save()


class BandViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Band objects.
    """
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer, 
        and assigns the user to the action'''

        serializer.save(created_by=self.request.user)
    
    def get_queryset(self):
        '''handles the queryset and any query parameters to filter bands by category.'''

        category = self.request.query_params.get('category', None)
        queryset = self.queryset

        if category:
            queryset = queryset.filter(category__name=category).order_by('name')
        return queryset


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Album objects.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer.''

        serializer.save()


    def get_queryset(self):
        '''handles the queryset and any query parameters to filter albums by band.'''

        band = self.request.query_params.get('band', None)
        queryset = self.queryset

        if band:
            queryset = queryset.filter(band__name=band).order_by('-release_date')
        return queryset


class SongViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions for Songs.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer.'''

        serializer.save()

    def get_queryset(self):
        '''handles the queryset and any query parameters to filter Songs by Band and or Album.'''

        album = self.request.query_params.get('album', None)
        band = self.request.query_params.get('band', None)
        queryset = self.queryset

        if album:
            queryset = queryset.filter(album__name=album).order_by('track_num')
        if band:
            queryset = queryset.filter(album__band__name=band).order_by('-album__release_date', 'track_num')
        return queryset


