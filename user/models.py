from django.db import models
# Create your models here.
#tecnicos
class tecnicos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    celula = models.CharField(max_length=50)
    id_tecnico_supervisor = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre


#laboratorios
class laboratorios(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    num_piso = models.IntegerField()
    num_mesas = models.IntegerField()
    num_sillas = models.IntegerField()
    extintor = models.BooleanField()
    basurero = models.BooleanField()
    botiquin = models.BooleanField()
    aire_acondicionado = models.BooleanField()
    proyector = models.BooleanField()
    camara_seguiridad = models.BooleanField()
    pizzara = models.BooleanField()
    cortina_proyector = models.BooleanField()
    id_tec_enc = models.ForeignKey(tecnicos, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre

#computadoras
class computadoras(models.Model):
    mouse = models.BooleanField()
    teclado = models.BooleanField()
    id_lab_pertenece = models.ForeignKey(laboratorios, on_delete=models.CASCADE, null=True, blank=True)
    id_tec_enc = models.ForeignKey(tecnicos, on_delete=models.CASCADE, null=True, blank=True)
    
    
#recomendaciones
class recomendaciones(models.Model):
    descripcion = models.CharField(max_length=50)
    id_computadora = models.ForeignKey(computadoras, on_delete=models.CASCADE, null=True, blank=True)
    #id_persona
    def __str__(self):
        return self.descripcion

#estudiantes
class estudiantes(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    celuda = models.CharField(max_length=10)
    
    def __str__(self):
        return self.apellido + " " + self.nombre


#monitores
class monitores (models.Model):
    resolucion = models.CharField(max_length=50)
    pulgadas = models.IntegerField()
    marca = models.CharField(max_length=50)
    herzios = models
    


#cpus