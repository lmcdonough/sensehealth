from django.shortcuts import render
from rest_framework import generics, permissions, viewsets
# from models import Category, Review, Establishment
from serializers import UserSerializer #, CategorySerializer, ReviewSerializer, EstablishmentSerializer
from django.contrib.auth.models import User
from permissions import IsOwnerOrReadOnly, IsOwner
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
        # 'categories': reverse('category-list', request=request, format=format),
        # 'reviews': reverse('review-list', request=request, format=format),
        # 'establishments': reverse('establishment-list', request=request, format=format)        
    })

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset handles all the actions (list create, retreive, update, destroy)
    for the User viewset.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwner)
    