from django.db import models

# Create your models here.
class Poema(models.Model):
    titulo = models.CharField(max_length=255)
    imagen = models.URLField()
    contenido = models.TextField()
    categoria = models.CharField(max_length=100)
    likes = models.PositiveIntegerField(default=0)

    def obtenerParrafos(self):
        return self.contenido.split("\n\n")