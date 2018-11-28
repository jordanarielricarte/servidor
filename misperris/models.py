from django.db import models

class Perro(models.Model):
    estados_mascota_choices = (
        ('rescatado','Rescatado'),
        ('disponible','Disponible'),
        ('adoptado','Adoptado'),
        )
    id_mascota = models.AutoField(primary_key=True)
    imagen_mascota = models.ImageField(blank=True, null=True,
                     upload_to="perros/%Y/%m/%D/")##esto es para que al guardar no sea el mismo nombre de imagen y no tenga conflictos al momento de guardar un img
                      ## asi se  guarda una imagen segun la carpeta de su dia mes y año
    nombre_mascota = models.CharField(max_length=15)
    raza_mascota = models.CharField(max_length=30)
    descripcion_mascota = models.TextField()
    estado_mascota = models.CharField(max_length=15, choices = estados_mascota_choices)

    def __str__(self):
        return self.nombre_mascota