import imp
from pyexpat import model
from rest_framework import serializers
from .models import *

class MemberSerializer (serializers.ModelSerializer):
    class Meta:
        model = Member
        fields='__all__'

class VenueSerializer (serializers.ModelSerializer):
    class Meta:
        model = Venue
        fields='__all__'

class DeviceSerializer (serializers.ModelSerializer):
    class Meta:
        model = Device
        fields='__all__'

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields='__all__'
