from django.db import models

# Create your models here.

class Solicitudes(models.Model):
     name = models.CharField(max_length=40)
     lastname = models.CharField(max_length=40)
     email = models.EmailField()
     content = models.TextField (max_length=200)
     curriculum_vitae = models.FileField(upload_to='cvs/')
     
     class Meta:
        verbose_name="Solicitud"
        verbose_name_plural="Solicitudes"