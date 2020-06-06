from django.db import models
from django.utils.timezone import now
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Categoria"
        verbose_name_plural = "Categorias"
        ordering = ["-created"]

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=50, verbose_name="Titulo")
    content = models.TextField(verbose_name="Contenido")
    published = models.DateTimeField(default=now, verbose_name="Fecha de publicacion")
    image = models.ImageField(null=True, blank=True, verbose_name="Imagen")
    author = models.ForeignKey(User, on_delete="CASCADE", verbose_name="Autor")
    categories = models.ManyToManyField(Category, verbose_name="Categoria", related_name="get_posts")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Entrada"
        verbose_name_plural = "Entradas"
        ordering = ["-created"]

    def __str__(self):
        return self.title
