from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api.views import PostViewSet, CommentViewSet, GroupViewSet, FollowViewSet

router = DefaultRouter()

router.register(r'v1/posts', PostViewSet)
router.register(
    r'v1/posts/(?P<post_id>\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register(r'v1/groups', GroupViewSet)
router.register(r'v1/follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('', include(router.urls)),
]
