from django.db import models

class URL(models.Model):
    long_url = models.URLField()
    short_url = models.CharField(max_length=8, unique=True)

    def __str__(self):
        return f"{self.short_url} -> {self.long_url}"
