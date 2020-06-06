from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Titulo", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(verbose_name="Fecha de creacion", auto_now_add=True)
    updated = models.DateTimeField(verbose_name="Fecha de modificacion", auto_now=True)

    class Meta:
        verbose_name = "Pagina"
        verbose_name_plural = "Paginas"
        ordering = ["order", "title"]

    def __str__(self):
        return self.title
