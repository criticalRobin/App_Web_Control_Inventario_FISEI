from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class User(AbstractUser):
    ROL_CHOICES = (
    ('estudiante', 'Estudiante'),
    ('tecnico', 'Técnico'),
    )
    celular = models.CharField(max_length=10, null=False, blank=False)
    direccion = models.CharField(max_length=50, null=False, blank=False)
    rol = models.CharField(max_length=10, choices=ROL_CHOICES, null=False, blank=False)
    

#laboratorios
class Laboratorio(models.Model):
    nombre = models.CharField(max_length=50)
    descripcion = models.CharField(max_length=50)
    num_piso = models.IntegerField()
    num_mesas = models.IntegerField()
    num_sillas = models.IntegerField()
    extintor = models.BooleanField()
    basurero = models.BooleanField()
    botiquin = models.BooleanField()
    aire_acondicionado = models.BooleanField()
    camara_seguiridad = models.BooleanField()
    pizzara = models.BooleanField()
    cortina_proyector = models.BooleanField()
    id_user_encargado = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.nombre

#computadoras
class Computadora(models.Model):
    mouse = models.BooleanField()
    teclado = models.BooleanField()
    id_lab = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, related_name='proyectores')
    id_user_encargado = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    
    
class Proyector(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    id_lab = models.ForeignKey(Laboratorio, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.marca + " " + self.modelo   
    
#recomendaciones
class Recomendacion(models.Model):
    descripcion = models.CharField(max_length=50)
    id_computadora = models.ForeignKey(Computadora, on_delete=models.CASCADE, null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.descripcion

class Tarea(models.Model):
    descripcion = models.CharField(max_length=50)
    id_recomendacion = models.ForeignKey(Recomendacion, on_delete=models.CASCADE, null=True, blank=True)
    id_user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    ESTADO_CHOICES = (
    ('pendiente', 'Pendiente'),
    ('en proceso', 'En proceso'),
    ('finalizada', 'Finalizada'),
    )
    
    def __str__(self):
        return self.descripcion
  
#monitores
class Monitor(models.Model):
    modelo = models.CharField(max_length=50, default="")
    resolucion = models.CharField(max_length=50)
    pulgadas = models.IntegerField()
    marca = models.CharField(max_length=50)
    HERZ_CHOICES = (
    ('60', '60'),
    ('120', '120'),
    ('144', '144'),
    )
    herz = models.CharField(max_length=10, choices=HERZ_CHOICES, null=True, blank=True)
    id_comp_pert = models.ForeignKey(Computadora, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return str(self.id) + " " + self.marca
    
    
class Cpu(models.Model):
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50)
    id_comp_pert = models.ForeignKey(Computadora, on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.marca + " " + self.modelo

class Ram(models.Model):
    marca = models.CharField(max_length=50, null=False, blank=False)
    capacidad = models.IntegerField()
    velocidad = models.IntegerField()
    TIPO_CHOICES = (
    ('ddr3', 'DDR3'),
    ('ddr4', 'DDR4'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES,null=False, blank=False)
    id_cpu_pert = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.marca + " " + self.capacidad + "GB"
    
class Disco(models.Model):
    marca = models.CharField(max_length=50, null=False, blank=False)
    capacidad = models.IntegerField()
    TIPO_CHOICES = (
    ('ssd', 'SSD'),
    ('hdd', 'HDD'),
    )
    tipo = models.CharField(max_length=10, choices=TIPO_CHOICES, null=False, blank=False)
    velocidad_escritura = models.IntegerField()
    velocidad_lectura = models.IntegerField()
    id_cpu_pert = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return self.marca + " " + self.capacidad + "GB"

class Procesador(models.Model):
    marca = models.CharField(max_length=50, null=False, blank=False)
    modelo = models.CharField(max_length=50, null=False, blank=False)
    generacion = models.IntegerField()
    ARQUI_CHOICES = (
    ('x86', 'x86'),
    ('x64', 'x64'),
    ('X32', 'X32')
    )
    arquitectura = models.CharField(max_length=10, choices=ARQUI_CHOICES, null=False, blank=False)
    velocidad = models.IntegerField()
    nucleos = models.IntegerField()
    hilos = models.IntegerField()
    id_cpu_pert = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return self.marca + " " + self.modelo