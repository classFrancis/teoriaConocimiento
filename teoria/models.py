from django.db import models

# Create your models here.
class Objeto(models.Model):
    nombreObjeto=models.CharField(max_length=150)
    colorObjeto=models.CharField(max_length=100,null=True)
    tipoObjeto=models.CharField(max_length=150,null=True)
    
class Conocimiento(models.Model):
    sujeto=models.ForeignKey('Sujeto', on_delete=models.CASCADE)
    objeto=models.ForeignKey(Objeto, on_delete=models.CASCADE)
    aprehendimiento=models.TextField()
    sujetoComoOjbeto=models.ForeignKey('Suejeto', on_delete=models.CASCADE)

class Sujeto(models.Model):
    nombreSujeto=models.CharField(max_length=150)
    apellidoSujeto=models.CharField(max_length=150)
    edadSujeto=models.IntegerField()
    alturaSujeto=models.DecimalField(max_digits=3,decimal_places=2,null=True)
    etniaSujeto=models.CharField(max_length=150,null=True)

