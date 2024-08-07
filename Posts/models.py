from django.db import models

# Create your models here.
class Posts(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    snippet = models.TextField(null=True)
    image = models.ImageField(default=None, blank=True)

    def __str__(self) -> str:
        return self.title