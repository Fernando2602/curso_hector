from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=50, verbose_name = 'Titulo')
    description = models.TextField(verbose_name = 'Descripcion')
    image = models.ImageField(verbose_name = 'Imagen', upload_to = 'projects')
    autor = models.CharField(max_length=50, default='', verbose_name = 'Autor')
    link = models.URLField(max_length=100, null=True, blank=True)
    updated = models.DateTimeField(auto_now_add=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'projecto'
        verbose_name_plural = 'projectos'
        ordering = ['-created']

    def __str__(self):
        return self.title

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    email2 = models.EmailField(default="hola@hotmail.com")

    def __str__(self):
        return self.name
