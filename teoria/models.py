from django.db import models

# Create your models here.
class Objeto(models.Model):
    nombreObjeto=models.CharField(max_length=150)
    colorObjeto=models.CharField(max_length=100,null=True)
    tipoObjeto=models.CharField(max_length=150,null=True)
    
class Conocimiento(models.Model):
    sujeto=models.ForeignKey('Sujeto',on_delete=models.CASCADE)
    objeto=models.ForeignKey(Objeto,on_delete=models.CASCADE)
    aprehendimiento=models.TextField()
    sujetoComoObjetoDeConocimiento=models.ForeignKey('Sujeto',on_delete=models.CASCADE)

class Sujeto(models.Model):
    MASCULINO='M'
    FEMENINO='F'
    OPCIONES_SEXO=[
        (MASCULINO, 'Masculino'),
        (FEMENINO, 'Femenino'),
    ]
    nombreSujeto=models.CharField(max_length=150)
    apellidoSujeto=models.CharField(max_length=150)
    edadSujeto=models.IntegerField()
    alturaSujeto=models.DecimalField(max_digits=3,decimal_places=2,null=True)
    etniaSujeto=models.CharField(max_length=150,null=True)
    sexoBiologicoSujeto=models.CharField(max_length=1, choices=OPCIONES_SEXO)
    autopercepcionSexual=models.CharField(max_length=150,null=True)
    profesionSujeto=models.CharField(max_length=150,null=True)
    partidoPoliticoSujeto=models.CharField(max_length=150,null=True)

    def getSexoBiologico(self):
        return dict(self.OPCIONES_SEXO)[self.sexoBiologicoSujeto]   

