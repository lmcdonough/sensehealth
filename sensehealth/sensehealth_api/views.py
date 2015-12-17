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
                          IsAdminUser)


    def perform_create(self, serializer):
        '''handles the saving of the serializer, 
        and assigns the user to the action'''

        serializer.save()


class BandViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Band.objects.all()
    serializer_class = BandSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer, 
        and assigns the user to the action'''

        serializer.save(created_by=self.request.user)

    # def get_queryset(self):
    #     '''handles the queryset and any query parameters to filter reviews by establishment.'''

    #     establishment = self.request.query_params.get('establishment', None)
    #     if establishment is not None:
    #         self.queryset = self.queryset.filter(establishment=establishment).order_by('-created')
    #     return self.queryset


class AlbumViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer, 
        and assigns the user to the action'''

        serializer.save()


class SongViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Song.objects.all()
    serializer_class = SongSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly)


    def perform_create(self, serializer):
        '''handles the saving of the serializer, 
        and assigns the user to the action'''

        serializer.save()

