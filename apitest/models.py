from django.db import models


##choices in (human, machine) format
#USER_CHOICES = [('')]

class Users(models.Model):
	created = models.DateTimeField(auto_now_add=True)
	title = models.CharField(max_length=200)
	author = models.CharField(max_length=200)
	pubDate = models.CharField(max_length=200)
	publisher = models.CharField(max_length=200)
	summary = models.CharField(max_length=200)
	price = models.CharField(max_length=200)
	link = models.CharField(max_length=200)
	coverImg = models.CharField(max_length=200)