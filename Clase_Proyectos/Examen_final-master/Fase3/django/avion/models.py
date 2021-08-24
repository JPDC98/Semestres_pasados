from django.db import models

# Create your models here.

class costos(models.Model):
    subtotal=models.IntegerField()
    descuento=models.CharField(max_length=3)
    total=models.IntegerField()
    def __str__(self):
        return "Sub total %s, descuento %s total %s"%(self.subtotal,self.descuento,self.total)