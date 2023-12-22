from django.db import models

from django.db import models

class Task(models.Model):
    text = models.TextField()
    solution = models.TextField()
    answer = models.TextField()
    is_approved = models.BooleanField(default=False)
    topic = models.CharField(max_length=100, default='')
    difficulty = models.IntegerField(default=0)