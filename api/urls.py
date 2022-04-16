from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import *

router = DefaultRouter()
router.register(r'members', MemberViewSet, 'member')
router.register(r'venues', VenueViewSet, 'venue')
router.register(r'devices', DeviceViewSet, 'device')
router.register(r'users', UserViewSet, 'user')

urlpatterns = [
    path('api/',include(router.urls)),
]
