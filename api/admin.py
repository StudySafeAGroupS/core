from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Member)
admin.site.register(Venue)
admin.site.register(Device)
admin.site.register(User)