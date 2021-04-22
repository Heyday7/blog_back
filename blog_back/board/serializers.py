from rest_framework import serializers
from .models import *


class CommentSerializer(serializers.ModelSerializer):
	user = serializers.CharField(read_only=True)
	post = serializers.CharField(read_only=True)

	class Meta:
		model = Comment
		fields = [
			'id',
			'content',
			'created_at',
			'user',
			'post'
		]


class PostSerializer(serializers.ModelSerializer):
	user = serializers.CharField(read_only=True)
	series = serializers.CharField(read_only=True)

	comments = CommentSerializer(many=True, read_only=True)

	class Meta:
		model = Post
		fields = [
			'id',
			'title',
			'content',
			'created_at',
			'updated_at',
			'series',
			'user',
			'comments',
		]


class SeriesSerializer(serializers.ModelSerializer):
	posts = PostSerializer(many=True, read_only=True)

	class Meta:
		model = Series
		fields = [
			'id',
			'name',
			'updated_at',
			'posts',
		]