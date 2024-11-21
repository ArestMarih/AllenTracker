from django.db import models

class task(models.Model):
    title = models.CharField(max_length=128)
    desc = models.TextField(null=True,blank=True)
    exp = models.PositiveIntegerField(default=0)
    done = models.BooleanField(default=False) 