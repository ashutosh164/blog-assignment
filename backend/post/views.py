from django.shortcuts import render
from .models import Posts, Comment
from .serializers import PostSerializer, CommentsSerializer
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Posts.objects.all()
    serializer_class = PostSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentsSerializer
    authentication_classes = [TokenAuthentication,]
    permission_classes = [IsAuthenticated,]



