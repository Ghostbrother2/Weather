from django.db import models

class PageReloadCounter(models.Model):
    count = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"Reload Count: {self.count}"