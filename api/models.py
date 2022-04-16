from django.db import models

# Create your models here.

class Member(models.Model):
    hku_id = models.CharField(max_length=10)
    name = models.CharField(max_length=150)
    is_close_contact = models.BooleanField()
    def __str__(self) -> str:
        return self.name

class Venue(models.Model):
    venue_code = models.CharField(max_length=20)
    location = models.CharField(max_length=150)
    venue_type = models.CharField(max_length=2)
    capacity = models.IntegerField()
    is_poorly_ventilated_area = models.BooleanField()
    def __str__(self) -> str:
        return f"{self.venue_code}:{self.location}"

class Device(models.Model):
    hku_id = models.ForeignKey(Member, on_delete=models.CASCADE)
    venue_code = models.ForeignKey(Venue, on_delete=models.CASCADE)
    time_of_record = models.DateTimeField()
    is_an_entry_record = models.BooleanField()
    def __str__(self) -> str:
        record_type = "Entry" if self.is_an_entry_record else "Exit"
        return f"{record_type} record with venue code {self.venue_code} at {self.time_of_record} "
    
class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    is_admin = models.BooleanField()
    def __str__(self) -> str:
        return self.username