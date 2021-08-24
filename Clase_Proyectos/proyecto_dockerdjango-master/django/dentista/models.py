from django.db import models

# Create your models here.
class cliente_dentista(models.Model):
    nombre=models.CharField(max_length=50)
    edad=models.CharField(max_length=3)
    peso=models.CharField(max_length=4)
    altura=models.CharField(max_length=4)
    fecha=models.DateField()
    hora=models.TimeField()
    def __str__(self):
        return "%s tiene la cital a las %s el %s"%(self.nombre,self.hora,self.fecha)
        
    
