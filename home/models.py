from django.db import models


# Create your models here.

class Slider(models.Model):
    title = models.CharField(max_length=500)
    image = models.ImageField(upload_to='media')
    url = models.URLField(max_length=500, blank=True)

    def __str__(self):
        return self.title


