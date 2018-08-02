from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView
from django.conf.urls import url,include
from django.contrib.auth.models import User
from rest_framework import routers

from aims.serializers import UserSerializer
from aims.viewsets import UserViewSet

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [

    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api/token/$', TokenObtainPairView.as_view(), name='token_obtain_pair'), #issue token route
    url(r'^api/token/refresh/$', TokenRefreshView.as_view(), name='token_refresh'), #refresh token route
    url(r'^api/token/verify/$', TokenVerifyView.as_view(), name='token_verify'), #token evrification for users route
]

