from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class StudyTable(models.Model):
    Firstname = models.CharField(max_length=100)
    Mob = models.CharField(max_length=15)  # Mobile number as a string to handle different formats
    Username = models.CharField(max_length=100, unique=True)  # Ensure unique username
    Password = models.CharField(max_length=100)  # Store hashed password (not plain text)
    def save(self, *args, **kwargs):
        # Ensure password is hashed before saving
        if not self.pk:  # Only hash the password when creating a new instance
            self.Password = make_password(self.Password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        # Check if the raw password matches the hashed password
        return check_password(raw_password, self.Password)
# Create your models here.
