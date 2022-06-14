from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken import views

from api.views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet


router = routers.DefaultRouter()
router.register(r'posts', PostViewSet, basename='posts')
router.register(r'groups', GroupViewSet, basename='group')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments'
                )
router.register(r'follow', FollowViewSet, basename='follow')                

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]

