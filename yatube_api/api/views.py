# TODO:  Напишите свой вариант
from django.shortcuts import get_object_or_404

from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, permissions, filters
from rest_framework.response import Response

from posts.models import Post, Comment, Group, Follow, User
from api.serializers import (PostSerializer,
                             CommentSerializer,
                             GroupSerializer,
                             FollowSerializer
                             )
from api.permissions import AuthorOrAuthenticated


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (AuthorOrAuthenticated,)
    pagination_class = LimitOffsetPagination

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrAuthenticated,)

    def perform_create(self, serializer):
        post = Post.objects.get(id=self.kwargs.get('post_id'))
        serializer.save(author=self.request.user, post=post)

    def perform_update(self, serializer):
        serializer.save(author=self.request.user)

    def get_queryset(self):
        post_id = self.kwargs.get('post_id')
        new_quaeryset = Comment.objects.filter(post=post_id)
        return new_quaeryset


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer


class FollowViewSet(viewsets.ViewSet):

    permission_classes = (permissions.IsAuthenticated,)

    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)

    def list(self, request):
        queryset = Follow.objects.all()
        serializer = FollowSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        follower = request.user
        following = get_object_or_404(User, username=request.data['following'])
        if follower == following:
            return Response('You cant follow yourself',
                            status.HTTP_403_FORBIDDEN)
        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=follower)
            return Response(serializer.data)
