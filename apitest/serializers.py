from django.forms import widgets
from rest_framework import serializers
from apitest.models import Users

class UsersSerializer(serializers.ModelSerializer):
	class Meta:
		model = Users
		fields = ('id', 'created', 'title', 'author', 'pubDate', 'publisher', 'summary', 'price', 'link', 'coverImg')

def create(self, validated_data):
	"""
	Create and return a new 'book' instance, given the validated validated_data
	"""
	return Users.objects.create(**validated_data)

def update(self, instance, validated_data):
	"""
	Update and return an existing book instance, given the validated validated_data
	"""
	instance.created = validated_data.get('created', instance.created)
	instance.title = validated_data.get('title', instance.title)
	instance.author = validated_data.get('author', instance.author)
	instance.pubDate = validated_data.get('pubDate', instance.pubDate)
	instance.publisher = validated_data.get('publisher', instance.publisher)
	instance.summary = validated_data.get('summary', instance.summary)
	instance.price = validated_data.get('price', instance.price)
	instance.link = validated_data.get('link', instance.link)
	instance.coverImg = validated_data.get('coverImg', instance.coverImg)
	return instance