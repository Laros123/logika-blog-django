from django.db import models
from django.utils import timezone
from datetime import timedelta

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=127)
    bio = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=127)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)

    author = models.ForeignKey(Author, on_delete=models.DO_NOTHING, related_name='post')

    def __str__(self) -> str:
        return self.title
    
    def published_recently(self):        
        return self.published_date >= timezone.now() - timedelta(days=7)
