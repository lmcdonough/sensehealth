from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)

	class Meta:
		ordering = ('name',)
		app_label = 'sensehealth_api'


	def __unicode__(self):
		return self.name

class Band(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	created_by = models.ForeignKey(User, related_name='band')
	active = models.BooleanField(default=True)
	origin = models.CharField(max_length=10, blank=False, null=False)
	category = models.ForeignKey(Category, related_name='band', null=False, blank=False)

	class Meta:
		ordering = ('name',)
		app_label = 'sensehealth_api'

	def __unicode__(self):
		return self.name

class Album(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	band = models.ForeignKey(Band, related_name='album')
	release_date = models.DateTimeField(auto_now_add=True)


	class Meta:
		ordering = ('release_date',)
		app_label = 'sensehealth_api'


	def __unicode__(self):
		return self.name


class Song(models.Model):
	name = models.CharField(max_length=200, blank=False, null=False)
	album = models.ForeignKey(Album, related_name='song', null=True, blank=True)
	track_num = models.IntegerField(blank=False, null=False)
	length = models.IntegerField(blank=False, null=False)


	class Meta:
		ordering = ('album', 'track_num',)
		app_label = 'sensehealth_api'


	def __unicode__(self):
		return self.name

