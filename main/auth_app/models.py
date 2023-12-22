from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import os
from django.conf import settings
from django.template.defaultfilters import slugify
from .validators import compress_image
from PIL import Image

def get_image_filename(instance, filename):
    name = instance.user.username
    slug = slugify(name)
    return f"avatars/{slug}-{filename}"

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(default='4914x3559_0xac120003_10815772101659466334.jpeg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self):
        super().save()

        img = Image.open(self.avatar.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.avatar.path)
