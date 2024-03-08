from django.db import models

# Create your models here.
class Fruta(models.Model):
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    presentacion=models.CharField(max_length=30,choices=[("Bolsa","Bolsa"),("Caja","Caja"),("Unidad","Unidad")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.color}-{self.fecha_creado}"
class Queso(models.Model):
    nombre=models.CharField(max_length=30)
    peso=models.IntegerField()
    presentacion=models.CharField(max_length=30,choices=[("Bolsa","Bolsa"),("Paquete","Paquete")])
    fecha_creado=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre}-{self.peso}-{self.fecha_creado}"