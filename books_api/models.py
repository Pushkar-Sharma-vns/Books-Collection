from django.db import models
from django.contrib.auth.models import User
import datetime

class Books(models.Model):
    title = models.CharField(max_length=200, blank=False)
    author = models.CharField(max_length=250, blank=False)
    publication_year = models.DateTimeField(auto_now=False, blank=False)
    created = models.DateTimeField(default=datetime.datetime.now, blank=True)
    updated = models.DateTimeField(auto_now = True, blank = True)
    
    def __str__(self):
        return self.title