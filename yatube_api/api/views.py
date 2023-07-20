from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from django_filters.rest_framework import DjangoFilterBackend

from api.permissions import AuthorOrAuthenticated
from api.serializers import (CommentSerializer,
                             FollowSerializer,
                             GroupSerializer,
                             PostSerializer,
                             )
from posts.models import Comment, Follow, Group, Post, User


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


class FollowViewSet(viewsets.ModelViewSet):

    permission_classes = (permissions.IsAuthenticated,)
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    filter_backends = (DjangoFilterBackend, filters.SearchFilter)
    search_fields = ('following__username',)

    def get_queryset(self):
        queryset = Follow.objects.filter(user=self.request.user)
        return queryset

    def create(self, request):
        follower = request.user

        if 'following' not in request.data:
            return Response('"following" is requared field',
                            status.HTTP_400_BAD_REQUEST)
        following_username = request.data['following']
        following = get_object_or_404(User, username=following_username)
        if follower == following:
            return Response('You cant follow yourself',
                            status.HTTP_400_BAD_REQUEST)

        already_following = Follow.objects.filter(
            user__username=follower.username,
            following__username=following_username
        )
        if already_following:
            return Response('You already following this user',
                            status.HTTP_400_BAD_REQUEST)

        serializer = FollowSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=follower)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
