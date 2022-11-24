# recetas/models.py
from django.db import models
from django.core.validators import RegexValidator
my_validator = RegexValidator(r"\b[A-Z]\w*", "Your string should contain letter A in it.")


class Receta(models.Model):
  nombre       = models.CharField(max_length=200, validators=[my_validator])
  preparacion  = models.TextField(max_length=5000, validators=[my_validator])
  foto         = models.FileField(upload_to='media/fotos')
  
  
  def __str__(self):
    return self.nombre
  
class Ingrediente(models.Model):
  nombre        = models.CharField(max_length=100)
  cantidad      = models.PositiveSmallIntegerField()
  unidades      = models.CharField(max_length=5)
  receta        = models.ForeignKey(Receta, on_delete=models.CASCADE)
  

  def __str__(self):
    return self.nombre
