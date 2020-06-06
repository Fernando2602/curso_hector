from django.db import models

class Link(models.Model):
    key = models.SlugField(verbose_name="Nombre clave", max_length=100, unique=True)
    name = models.CharField(verbose_name="Nombre", max_length=200)
    url = models.URLField(verbose_name="Enlace", null=True, blank=True)
    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = "Encale"
        verbose_name_plural = "Enlaces"
        ordering = ["name"]

    def __str__(self):
        return self.name
