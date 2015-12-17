from rest_framework import serializers
# from models import Category, Establishment, Review
from django.contrib.auth.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
	'''Straight forward, serializes the User object.'''

	class Meta:
		model = User
		fields = ('url', 'username')