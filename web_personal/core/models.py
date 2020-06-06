from django.db import models

class sample(models.Model):
    titulo = models.CharField(max_length=100)
