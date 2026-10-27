from django.db import models

class URLMapping(models.Model):
    original_url = models.URLField()
    code = models.CharField(unique=True, max_length=7)
