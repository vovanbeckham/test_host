from django.db import models

# Create your models here.
class Content(models.Model):
    name = models.CharField(max_length=255)
    content = models.TextField()
    is_published = models.BooleanField(default=True)


    def __str__(self) -> str:
        return self.name    