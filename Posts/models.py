from django.db import models
from django.conf import settings
from django.utils import timezone

# Create your models here.
class Posts(models.Model):
    content = models.TextField()
    media = models.ImageField(default=None, blank=True)
    published_date = models.DateField(default=timezone.now)
    slug = models.SlugField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, default=None, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.content[:20] + "..."
    