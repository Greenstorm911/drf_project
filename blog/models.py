from django.db import models
from django.contrib.auth.models import User

class Blog(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs', blank=True, null=True)
    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=100)
    text = models.TextField()
    
    def __str__(self):
        return self.title


class BlockUser(models.Model):
    username = models.CharField(max_length=30)

    def __str__(self):
        return self.username