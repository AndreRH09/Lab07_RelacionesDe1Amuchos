from django.db import models

# Create your models here.

class Destinos(models.Model):

    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    #g = 



STAR_HOTEL = (
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
)
# Se crea una tabla para agregar "hoteles" que acompañen los destinos turisticos
class Hotel(models.Model):
    name= models.CharField(max_length=100)
    img= models.ImageField(upload_to='pics')
    desc= models.TextField()
    price= models.IntegerField()
    offer= models.BooleanField(default=False)
    # Se crea una cinta de opciones para definir la cantidad de estrellas de un hotel
    stars = models.CharField(
        max_length = 20,
        choices = STAR_HOTEL,
        default = '1'
        )
    #g = 
class paqueteTurismo(models.Model):
    name = models.CharField(max_length=20)
    destino = models.ForeignKey(Destinos)
    #si se elimina la calse paquete, tambien la clase hotel(sugerido en el video)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)