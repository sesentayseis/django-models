from django.db import models

# Create your models here.
class Pregunta(models.Model):
    pregunta=models.CharField(max_length=200)
    pub_date=models.DateTimeField('date published')

    def __str__(self) :
        return self.pregunta
class Opcion(models.Model):
    pregunta=models.ForeignKey(Pregunta,on_delete=models.CASCADE) 
    opcion_texto=models.CharField(max_length=200)
    votos=models.IntegerField(default=0)   
    def __str__(self) :
        return self.opcion_texto