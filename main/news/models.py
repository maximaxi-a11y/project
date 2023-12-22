from django.contrib.auth.models import User
from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date = models.DateField(db_comment="Date and time when the article was published")
