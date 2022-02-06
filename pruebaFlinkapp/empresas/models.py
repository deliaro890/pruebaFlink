from django.db import models
import uuid

class Empresa(models.Model):
  #id = models.IntegerField() #uuid-4
  #uuid_ = models.UUIDField(primary_key=True,default=uuid.uuid4,unique=True)
  nombre = models.CharField(max_length=50)
  descripcion = models.CharField(max_length=100)
  simbolo = models.CharField(max_length=10,unique=True)
  is_active = models.BooleanField(default = True)
  valores = models.CharField(max_length=400,default='')

  def __str__(self):
    return self.nombre

    
