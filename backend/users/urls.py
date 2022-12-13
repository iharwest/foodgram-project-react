from django.urls import include, path

from users.views import FollowerView, FollowViewSet

urlpatterns = [
    path('users/subscriptions/', FollowViewSet.as_view()),
    path('', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/<int:pk>/subscribe/', FollowerView.as_view())
]
