from rest_framework import viewsets
from .models import *
from .serializers import *


class PostViewSet(viewsets.ModelViewSet):
	queryset = Post.objects.all()
	serializers = PostSerializer

	def perform_create(self, serializer):
		serializers.save(user=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
	queryset = Comment.objects.all()
	serializers = CommentSerializer

	def perform_create(self, serializer):
		serializers.save(user=self.request.user, post=Post.objects.get(id=self.kwargs['post_id']))


class SeriesViewSet(viewsets.ModelViewSet):
	queryset = Series.objects.all()
	serializers = SeriesSerializer

# Create your views here.
