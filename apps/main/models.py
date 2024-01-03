from django.db import models
from apps.users.models import User
from django.utils import timezone

# Create your models here.
# laboratorios
class Laboratory(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    description = models.CharField(max_length=50, verbose_name="Descripción")
    floor_number = models.IntegerField(verbose_name="Número de piso")
    table_number = models.IntegerField(verbose_name="Número de mesas")
    chair_number = models.IntegerField(verbose_name="Número de sillas")
    fire_extinguisher = models.BooleanField(verbose_name="Extintor")
    trash_can = models.BooleanField(verbose_name="Basurero")
    first_aid_kit = models.BooleanField(verbose_name="Botiquín de primeros auxilios")
    whiteboard = models.BooleanField(verbose_name="Pizarra")
    projector_screen = models.BooleanField(verbose_name="Cortina de proyector")
    responsible_user_id = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Usuario responsable",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Laboratorio"
        verbose_name_plural = "Laboratorios"


# computers
class Computer(models.Model):
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
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Usuario responsable",
    )

    class Meta:
        verbose_name = "Computadora"
        verbose_name_plural = "Computadoras"


class Projector(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=50, verbose_name="Modelo")
    lab_id = models.ForeignKey(
        Laboratory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Laboratorio",
    )

    def __str__(self):
        return self.brand + " " + self.model

    class Meta:
        verbose_name = "Proyector"
        verbose_name_plural = "Proyectores"


class Security_camera(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=50, verbose_name="Modelo")
    resolution = models.CharField(max_length=50, verbose_name="Resolución")
    sensor = models.CharField(max_length=50, verbose_name="Sensor")
    lens = models.CharField(max_length=50, verbose_name="Lente")
    dimensions = models.CharField(max_length=50, verbose_name="Dimensiones")

    lab_id = models.ForeignKey(
        Laboratory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Laboratorio",
    )

    def __str__(self):
        return self.brand + " " + self.model

    class Meta:
        verbose_name = "Cámara de seguridad"
        verbose_name_plural = "Cámaras de seguridad"


class Regulator_voltage(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=50, verbose_name="Modelo")
    capacity = models.IntegerField(verbose_name="Capacidad")
    dimensions = models.CharField(max_length=50, verbose_name="Dimensiones")
    weight = models.CharField(max_length=50, verbose_name="Peso")
    device_type = models.CharField(max_length=50, verbose_name="Tipo")
    input_voltage = models.IntegerField(verbose_name="Voltaje de entrada")
    output_voltage = models.IntegerField(verbose_name="Voltaje de salida")
    output_current = models.IntegerField(verbose_name="Corriente de salida")
    number_plugs = models.IntegerField(verbose_name="Número de enchufes")
    lab_id = models.ForeignKey(
        Laboratory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Laboratorio",
    )

    def __str__(self):
        return self.brand + " " + self.model

    class Meta:
        verbose_name = "Regulador de voltaje"
        verbose_name_plural = "Reguladores de voltaje"


class Air_Conditioner(models.Model):
    brand = models.CharField(max_length=50, verbose_name="Marca")
    model = models.CharField(max_length=50, verbose_name="Modelo")
    voltage = models.IntegerField(verbose_name="Voltaje")
    capacity = models.IntegerField(verbose_name="Capacidad")
    device_type = models.CharField(max_length=50, verbose_name="Tipo")
    potency = models.IntegerField(verbose_name="Potencia")
    consumption = models.IntegerField(verbose_name="Consumo")
    lab_id = models.ForeignKey(
        Laboratory,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Laboratorio",
    )

    def __str__(self):
        return self.brand + " " + self.model

    class Meta:
        verbose_name = "Aire acondicionado"
        verbose_name_plural = "Aires acondicionados"


# recommendations
class Recommendation(models.Model):
    description = models.CharField(max_length=50, verbose_name="Descripción")
    computer_id = models.ForeignKey(
        Computer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Computadora",
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Usuario"
    )
    date = models.DateField(default=timezone.now, verbose_name="Fecha")

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = "Recomendación"
        verbose_name_plural = "Recomendaciones"


class Task(models.Model):
    description = models.CharField(max_length=50, verbose_name="Descripción")
    recommendation_id = models.ForeignKey(
        Recommendation,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Recomendación",
    )
    user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True, verbose_name="Usuario"
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


# monitors
class Monitor(models.Model):
    model = models.CharField(max_length=50, default="", verbose_name="Modelo")
    resolution = models.CharField(max_length=50, verbose_name="Resolución")
    inches = models.IntegerField(verbose_name="Pulgadas")
    brand = models.CharField(max_length=50, verbose_name="Marca")
    HERZ_CHOICES = (
        ("60", "60"),
        ("120", "120"),
        ("144", "144"),
    )
    herz = models.CharField(
        max_length=10, choices=HERZ_CHOICES, null=True, blank=True, verbose_name="Herz"
    )
    computer_id = models.ForeignKey(
        Computer,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        verbose_name="Computadora",
    )

    def __str__(self):
        return str(self.id) + " " + self.brand

    class Meta:
        verbose_name = "Monitor"
        verbose_name_plural = "Monitores"


class Cpu(models.Model):
    brand = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Marca"
    )
    model = models.CharField(max_length=50, verbose_name="Modelo")
    computer_id = models.ForeignKey(
        Computer,
        on_delete=models.CASCADE,
        null=False,
        blank=False,
        verbose_name="Computadora",
    )

    def __str__(self):
        return self.brand + " " + self.model

    class Meta:
        verbose_name = "CPU"
        verbose_name_plural = "CPUs"


class Ram(models.Model):
    brand = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Marca"
    )
    capacity = models.IntegerField(verbose_name="Capacidad")
    speed = models.IntegerField(verbose_name="Velocidad")
    TYPE_CHOICES = (
        ("ddr3", "DDR3"),
        ("ddr4", "DDR4"),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        null=False,
        blank=False,
        verbose_name="Tipo",
    )
    cpu_id = models.ForeignKey(
        Cpu, on_delete=models.CASCADE, null=False, blank=False, verbose_name="CPU"
    )

    def __str__(self):
        return self.brand + " " + str(self.capacity) + "GB"

    class Meta:
        verbose_name = "RAM"
        verbose_name_plural = "RAMs"


class Disk(models.Model):
    brand = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Marca"
    )
    capacity = models.IntegerField(verbose_name="Capacidad")
    TYPE_CHOICES = (
        ("ssd", "SSD"),
        ("hdd", "HDD"),
    )
    type = models.CharField(
        max_length=10,
        choices=TYPE_CHOICES,
        null=False,
        blank=False,
        verbose_name="Tipo",
    )
    write_speed = models.IntegerField(verbose_name="Velocidad de escritura")
    read_speed = models.IntegerField(verbose_name="Velocidad de lectura")
    cpu_id = models.ForeignKey(
        Cpu, on_delete=models.CASCADE, null=True, blank=True, verbose_name="CPU"
    )

    def __str__(self):
        return self.brand + " " + str(self.capacity) + "GB"

    class Meta:
        verbose_name = "Disco"
        verbose_name_plural = "Discos"


class Processor(models.Model):
    brand = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Marca"
    )
    model = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Modelo"
    )
    generation = models.IntegerField(verbose_name="Generación")
    ARCH_CHOICES = (("x86", "x86"), ("x64", "x64"), ("X32", "X32"))
    architecture = models.CharField(
        max_length=10,
        choices=ARCH_CHOICES,
        null=False,
        blank=False,
        verbose_name="Arquitectura",
    )
    speed = models.IntegerField(verbose_name="Velocidad")
    cores = models.IntegerField(verbose_name="Núcleos")
    threads = models.IntegerField(verbose_name="Hilos")
    cpu_id = models.ForeignKey(
        Cpu, on_delete=models.CASCADE, null=False, blank=False, verbose_name="CPU"
    )

    def __str__(self):
        return self.brand + " " + self.model

    class Meta:
        verbose_name = "Procesador"
        verbose_name_plural = "Procesadores"