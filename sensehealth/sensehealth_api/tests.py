from django.test import TestCase
from django.core.urlresolvers import reverse
from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, APITestCase
from django.contrib.auth.models import User
from sensehealth_api.models import Category, Band, Album, Song
from sensehealth_api.views import UserViewSet, CategoryViewSet, BandViewSet, AlbumViewSet, SongViewSet


class RootTests(APITestCase):
	
	def setUp(self):
   		self.client = APIClient()
   		self.domain = 'testserver'
   		self.response = self.client.get('/')
   		self.data = {
   		    "bands": "http://{}/bands/".format(self.domain), 
    		"albums": "http://{}/albums/".format(self.domain),
    		"users": "http://{}/users/".format(self.domain), 
    		"categories": "http://{}/categories/".format(self.domain),
    		"songs": "http://{}/songs/".format(self.domain)
    		}

   	def test_status(self):   		
   		self.assertEqual(self.response.status_code, 200)

   	def test_endpoints_data(self):
   		self.assertEqual(self.response.data, self.data)



class BandTests(APITestCase):
	
	def setUp(self):
   		self.client = APIClient()  
   		self.domain = 'testserver' 
   		self.test_user = User.objects.create_user("test_user", "test@user.com", "123456")		 				
		self.client.force_authenticate(user=self.test_user)
		self.category = Category(name='rock')		
		self.category.save()
		self.url = reverse('band-list')
		self.response = self.client.get(self.url)
		
   	def test_status(self):

   		self.assertEqual(self.response.status_code, 200)

   	def test_create(self):
   		band_data = {
   			'name': 'Test Band',
   			'active': True,
   			'origin': 'USA',
   			'category': 'http://{}/category/{}/'.format(self.domain, self.category.id)
   			}
   
   		response = self.client.post(self.url, band_data, format='json')
   		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   		band = Band.objects.all()
   		self.assertEqual(band.count(), 1)
   		self.assertEqual(band.get().name, 'Test Band')
   	   	band_url = reverse('band-detail', kwargs={'pk': band.get().pk})  	
 		read_response = self.client.get(band_url)   	
   		self.assertEqual(read_response.data['pk'], unicode(band.get().pk))



class AlbumTests(APITestCase):
	
	def setUp(self):
   		self.client = APIClient()  
   		self.domain = 'testserver' 
   		self.test_user = User.objects.create_user("test_user", "test@user.com", "123456")		 				
		self.client.force_authenticate(user=self.test_user)
		self.category = Category(name='rock')		
		self.category.save()
		self.band = Band(name='Test Band',
						created_by=self.test_user, 
						active=True, 
						origin='USA', 
						category=self.category)
		self.band.save()
		self.url = reverse('album-list')
		self.response = self.client.get(self.url)
		
   	def test_status(self):

   		self.assertEqual(self.response.status_code, 200)

   	def test_create(self):
   		album_data = {
   			'name': 'Test Album',
   			'band': 'http://{}/band/{}/'.format(self.domain, self.band.id)
   			}
   
   		response = self.client.post(self.url, album_data, format='json')
   		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   		album = Album.objects.all()
   		self.assertEqual(album.count(), 1)
   		self.assertEqual(album.get().name, 'Test Album')
   	   	album_url = reverse('album-detail', kwargs={'pk': album.get().pk})  	
 		read_response = self.client.get(album_url)   	
   		self.assertEqual(read_response.data['pk'], unicode(album.get().pk))



class SongTests(APITestCase):
	
	def setUp(self):
   		self.client = APIClient()  
   		self.domain = 'testserver' 
   		self.test_user = User.objects.create_user("test_user", "test@user.com", "123456")		 				
		self.client.force_authenticate(user=self.test_user)
		self.category = Category(name='rock')		
		self.category.save()
		self.band = Band(name='Test Band',
						created_by=self.test_user, 
						active=True, 
						origin='USA', 
						category=self.category)
		self.band.save()
		self.album = Album(name='Test Album', band=self.band)
		self.album.save()
		self.url = reverse('song-list')
		self.response = self.client.get(self.url)
		
   	def test_status(self):

   		self.assertEqual(self.response.status_code, 200)

   	def test_create(self):
   		song_data = {
   			'name': 'Test Song',
   			'album': 'http://{}/album/{}/'.format(self.domain, self.album.id),
   			'track_num': 1,
   			'length': 185
   			}
   
   		response = self.client.post(self.url, song_data, format='json')
   		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
   		song = Song.objects.all()
   		self.assertEqual(song.count(), 1)
   		self.assertEqual(song.get().name, 'Test Song')
   	   	song_url = reverse('song-detail', kwargs={'pk': song.get().pk})  	
 		read_response = self.client.get(song_url)   	
   		self.assertEqual(read_response.data['pk'], unicode(song.get().pk))
