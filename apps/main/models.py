from django.db import models
from apps.users.models import User
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Laboratory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre", unique=True)
    description = models.CharField(max_length=100, verbose_name="Descripción")
    floor_number = models.IntegerField(
    verbose_name="Número de piso", 
    validators=[MinValueValidator(0), MaxValueValidator(3)]
    )
    table_number = models.IntegerField(
    verbose_name="Número de mesas", 
    validators=[MinValueValidator(0), MaxValueValidator(50)]
    )
    chair_number = models.IntegerField(
    verbose_name="Número de sillas", 
    validators=[MinValueValidator(0), MaxValueValidator(100)]
    )
    fire_extinguisher = models.BooleanField(verbose_name="Extintor")
    trash_can = models.BooleanField(verbose_name="Basurero")
    first_aid_kit = models.BooleanField(verbose_name="Botiquín de primeros auxilios")
    whiteboard = models.BooleanField(verbose_name="Pizarra")
    projector_screen = models.BooleanField(verbose_name="Cortina de proyector")
    responsible_user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Usuario responsable",
    )
    def __str__(self):
        return self.name+" Piso:"+self.floor_number.__str__()
    class Meta:
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"

class LabItem(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Código")
    brand = models.CharField(max_length=20, verbose_name="Marca")
    model = models.CharField(max_length=20, verbose_name="Modelo")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    TYPES_CHOICES = (
        ('projector', 'Proyector'),
        ('security_camera', 'Cámara de seguridad'),
        ('voltage_regulator', 'Regulador de voltaje'),
        ('air_conditioner', 'Aire acondicionado'),
    )
    type = models.CharField(max_length=20, choices=TYPES_CHOICES, verbose_name="Tipo")
    id_laboratory = models.ForeignKey(Laboratory, on_delete=models.PROTECT, verbose_name="Laboratorio")
    responsible_user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Usuario responsable",
    )
    
    def __str__(self):
        return self.code + " " + self.type
    
    class Meta:
        verbose_name = "Bien de laboratorio"
        verbose_name_plural = "Bienes de laboratorio"   
    
class Computer(models.Model):
    #agregar codigo computadora, nombre lab unico y ese va a ser el id.
    code = models.CharField(max_length=20, unique=True, verbose_name="Código")
    mouse = models.BooleanField(verbose_name="Mouse")
    keyboard = models.BooleanField(verbose_name="Teclado")
    lab_id = models.ForeignKey(
        Laboratory,
        on_delete=models.CASCADE,
        related_name="computadoras",
        verbose_name="Laboratorio",
    )
    responsible_user_id = models.ForeignKey(
        User,
        on_delete=models.PROTECT,
        verbose_name="Usuario responsable",
    )
    
    def __str__(self):
        return self.code
    
    class Meta:
        verbose_name = "Computadora"
        verbose_name_plural = "Computadoras"

class ComputerItem(models.Model):
    code = models.CharField(max_length=20, unique=True, verbose_name="Código")
    brand = models.CharField(max_length=20, verbose_name="Marca")
    model = models.CharField(max_length=20, verbose_name="Modelo")
    description = models.CharField(max_length=100, verbose_name="Descripción")
    TYPE_CHOICES = (
        ('monitor', 'Monitor'),
        ('cpu', 'CPU'),
        ('ram', 'RAM'),
        ('disk', 'Disco'),
    )
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name="Tipo")
    id_computer = models.ForeignKey(Computer, on_delete=models.PROTECT, verbose_name="Computadora")
    
    def __str__(self):
        return self.code + " " + self.type

class Recommendation(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Usuario" , default = 3
    )
    
    id_lab = models.ForeignKey(Laboratory, on_delete=models.PROTECT, verbose_name="Laboratorio perteneciente")
    date = models.DateField(default=timezone.now, verbose_name="Fecha")
    
    
    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Recomendación"
        verbose_name_plural = "Recomendaciones"
        

class Task(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    recommendation_id = models.ForeignKey(
        Recommendation,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        verbose_name="Recomendación",
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name="Responsable"
    )
    STATUS_CHOICES = (
        ("pending", "Pendiente"),
        ("in progress", "En progreso"),
        ("completed", "Completada"),
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=20, default="pending")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Tarea"
        verbose_name_plural = "Tareas"