from django.db import models
from cloudinary.models import CloudinaryField

class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video = CloudinaryField('video', resource_type='video', blank=True, null=True)

    def __str__(self):
        return self.title


