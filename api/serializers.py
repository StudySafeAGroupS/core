import imp
from pyexpat import model
from rest_framework import serializers
from .models import *

class MemberSerializer (serializers.Serializer):
    hku_id = serializers.CharField(max_length=10)
    name = serializers.CharField(max_length=150)
    is_close_contact = serializers.BooleanField()
    class Meta:
        model = Member
        fields='__all__'

class VenueSerializer (serializers.Serializer):
    venue_code = serializers.CharField(max_length=20)
    location = serializers.CharField(max_length=150)
    venue_type = serializers.CharField(max_length=2)
    capacity = serializers.IntegerField()
    is_poorly_ventilated_area = serializers.BooleanField()
    class Meta:
        model = Venue
        fields='__all__'

class DeviceSerializer (serializers.Serializer):
    hku_id = serializers.CharField(max_length=10)
    venue_code = serializers.CharField(max_length=150)
    time_of_record = serializers.DateTimeField()
    is_an_entry_record = serializers.BooleanField()
    class Meta:
        model = Device
        fields='__all__'

class UserSerializer (serializers.Serializer):
    username = serializers.CharField(max_length=50)
    password = serializers.CharField(max_length=50)
    first_name = serializers.CharField(max_length=50)
    last_name = serializers.CharField(max_length=50)
    email = serializers.CharField(max_length=100)
    is_admin = serializers.BooleanField()
    class Meta:
        model = User
        fields='__all__'