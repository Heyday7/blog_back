from django.db import models
from django.contrib.auth.models import User

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    series = models.ForeignKey(
        'Series', 
        on_delete=models.SET_NULL,
        related_name='posts',
        related_query_name='post',
        null=True)
    user = models.ForeignKey(
      	User,
        on_delete=models.CASCADE,
        related_name='posts',
        related_query_name='post'
    )

    def __str__(self):
      	return self.title


class Comment(models.Model):
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	user = models.ForeignKey(
		User,
		on_delete=models.CASCADE,
		related_name='comments',
		related_query_name='comment' 
	)
	post = models.ForeignKey(
		Post, 
		on_delete=models.CASCADE,
		related_name='comments',
		related_query_name='comment' 
	)
	
	def __str__(self):
		return self.content



class Series(models.Model):
	name = models.CharField(max_length=100, unique=True)
	updated_at = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name


# Create your models here.
