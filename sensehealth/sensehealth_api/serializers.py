from rest_framework import serializers
from django.contrib.auth.models import User
from sensehealth_api.models import Category, Band, Album, Song

class UserSerializer(serializers.HyperlinkedModelSerializer):
	'''Straight forward, serializes the User object.'''

	class Meta:
		model = User
		fields = ('url', 'username')


class CategorySerializer(serializers.ModelSerializer):
	'''The Category Serializer, serializes the Category objects.'''

	pk = serializers.CharField(read_only=True)
	name = serializers.CharField(required=True, allow_blank=False, max_length=200)

	class Meta:
			model = Category
			fields = ('pk', 'name')   


class BandSerializer(serializers.ModelSerializer): 
	'''The Band serializer, pretty straight forward, serializes and deserializes Band objects.'''

	pk = serializers.CharField(read_only=True)   
	created_by = serializers.ReadOnlyField(source='user.username')
	category = serializers.HyperlinkedRelatedField(view_name='category-detail', queryset=Category.objects.all())

	class Meta:
			model = Band
			fields = ('pk', 'name', 'created_by', 'active', 'origin', 'category')


class AlbumSerializer(serializers.ModelSerializer): 
	'''The Album serializer, pretty straight forward, serializes and deserializes Album objects.'''

	pk = serializers.CharField(read_only=True)   
	band = serializers.HyperlinkedRelatedField(view_name='band-detail', queryset=Band.objects.all())

	class Meta:
			model = Album
			fields = ('pk', 'name', 'band', 'release_date')


class SongSerializer(serializers.ModelSerializer): 
	'''The Song serializer, pretty straight forward, serializes and deserializes Song objects.'''

	pk = serializers.CharField(read_only=True)   
	album = serializers.HyperlinkedRelatedField(view_name='album-detail', queryset=Album.objects.all())

	class Meta:
			model = Song
			fields = ('pk', 'name', 'album', 'track_num', 'length')


