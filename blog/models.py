from django.db import models
from django.utils import timezone

# Create your models here.
class Category(models.Model):
	title = models.CharField(max_length=200)
	author = models.ForeignKey('auth.User',on_delete = models.PROTECT)
	created_date = models.DateTimeField(default = timezone.now)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title

class Post(models.Model):
	category = models.ForeignKey(Category, on_delete = models.PROTECT)
	author = models.ForeignKey('auth.User',on_delete = models.PROTECT)
	title = models.CharField(max_length=200)
	text = models.TextField()
	created_date = models.DateTimeField(default = timezone.now)
	published_date = models.DateTimeField(blank = True, null = True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title