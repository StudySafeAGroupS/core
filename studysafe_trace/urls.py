from django.urls import path
from studysafe_trace import views

urlpatterns = [
    path('base/<str:id>/<str:date>', views.query, name="query"),
    path('base', views.base, name="base"),
    path('contacts', views.contacts, name="contacts"),
    path('venues', views.venues, name="venues"),
]