from django.db import models

class fxNews(models.Model):
    title = models.CharField(max_length=500)
