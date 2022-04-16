from xml.etree.ElementInclude import include
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .api_views import *

router = DefaultRouter()
router.register(r'members', MemberViewSet, 'member')
router.register(r'venues', MemberViewSet, 'venue')
router.register(r'devices', MemberViewSet, 'device')
router.register(r'users', MemberViewSet, 'user')

urlpatterns = [
    path('api/',include(router.urls)),
]