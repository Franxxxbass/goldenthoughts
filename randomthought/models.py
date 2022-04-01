from django.db import models


class Sentence(models.Model):
    body = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
