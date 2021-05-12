from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='book_photos', blank=True)
    description = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    writer = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    read = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
