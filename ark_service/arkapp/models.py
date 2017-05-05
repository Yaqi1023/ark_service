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

	def mint(self, quantity = 1):
		ark_list = []
		for x in quantity
		    key = arkpy.mint(authority = setting.NAAN, prefix = self.prefix, template = seif.template)
		    while _ark_exists(key):
		       key = arkpy.mint()
		    ark = Ark.object.create(key = key, minter = self)
		    ark.save()
		    ark_list.appreal(ark)
		 if quantity = 1
		    return ark_list(0)
		 return ark_list

			

class Ark(models.Model):
	key = models.CharField(max_length=25)
	date_created = models.DateField(auto_now=True)
	date_updated = models.DateField(auto_now=True)
	minter = models.ForeignKey(Minter)
	url = models.URLField(null=True, blank=True)

	def __repr__(self):
		return '<Ark: {}>'.format(self.key)

	def bind(request, key, url):
		self.url = url