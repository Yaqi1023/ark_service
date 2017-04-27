from django.db import models
from django.conf import settings
import arkpy

# Create your models here.
class Minter(models.Model):
	name = models.CharField(max_length=256)
	prefix = models.CharField(max_length=7)
	template = models.CharField(max_length=25)
	active = models.BooleanField(default=True)
	date_created = models.DateField(auto_now=True)
	description = models.TextField()

	def __repr__(self):
		return '<Minter: {}>'.format(self.name)

	def _ark_exists(self, key):
		if Ark.object.filter(key=key):
			return True
		else:
			return False

	def mint(self, quantity):
		pass
			

class Ark(models.Model):
	key = models.CharField(max_length=25)
	date_created = models.DateField(auto_now=True)
	date_updated = models.DateField(auto_now=True)
	minter = models.ForeignKey(Minter)
	url = models.URLField(null=True, blank=True)

	def __repr__(self):
		return '<Ark: {}>'.format(self.key)

	def bind(self, url):
		pass