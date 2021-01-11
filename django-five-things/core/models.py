from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import AbstractUser
from django.shortcuts import reverse

class User(AbstractUser):
    pass


class Topic(models.Model):
    title = models.CharField(max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='topics')

    class Meta:
        verbose_name = 'topic'
        verbose_name_plural = 'topics'

    def get_absolute_url(self):
        return reverse('topic-detail', args=[str(self.id)])


class Thing(models.Model):
    text = models.CharField(max_length=255)
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE, related_name="things")

