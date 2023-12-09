from django.db import models
from apps.users.models import User


# Create your models here.
# laboratorios
class Laboratory(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=50)
    floor_number = models.IntegerField()
    table_number = models.IntegerField()
    chair_number = models.IntegerField()
    fire_extinguisher = models.BooleanField()
    trash_can = models.BooleanField()
    first_aid_kit = models.BooleanField()
    air_conditioning = models.BooleanField()
    security_camera = models.BooleanField()
    whiteboard = models.BooleanField()
    projector_screen = models.BooleanField()
    responsible_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.name


# computers
class Computer(models.Model):
    mouse = models.BooleanField()
    keyboard = models.BooleanField()
    lab_id = models.ForeignKey(
        Laboratory, on_delete=models.CASCADE, related_name="projectors"
    )
    responsible_user_id = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True
    )


class Projector(models.Model):
    brand = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    lab_id = models.ForeignKey(
        Laboratory, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return self.brand + " " + self.model


# recommendations
class Recommendation(models.Model):
    description = models.CharField(max_length=50)
    computer_id = models.ForeignKey(
        Computer, on_delete=models.CASCADE, null=True, blank=True
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.description


class Task(models.Model):
    description = models.CharField(max_length=50)
    recommendation_id = models.ForeignKey(
        Recommendation, on_delete=models.CASCADE, null=True, blank=True
    )
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    STATUS_CHOICES = (
        ("pending", "Pending"),
        ("in progress", "In Progress"),
        ("completed", "Completed"),
    )

    def __str__(self):
        return self.description


# monitors
class Monitor(models.Model):
    model = models.CharField(max_length=50, default="")
    resolution = models.CharField(max_length=50)
    inches = models.IntegerField()
    brand = models.CharField(max_length=50)
    HERZ_CHOICES = (
        ("60", "60"),
        ("120", "120"),
        ("144", "144"),
    )
    herz = models.CharField(max_length=10, choices=HERZ_CHOICES, null=True, blank=True)
    computer_id = models.ForeignKey(
        Computer, on_delete=models.CASCADE, null=True, blank=True
    )

    def __str__(self):
        return str(self.id) + " " + self.brand


class Cpu(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50)
    computer_id = models.ForeignKey(
        Computer, on_delete=models.CASCADE, null=False, blank=False
    )

    def __str__(self):
        return self.brand + " " + self.model


class Ram(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    capacity = models.IntegerField()
    speed = models.IntegerField()
    TYPE_CHOICES = (
        ("ddr3", "DDR3"),
        ("ddr4", "DDR4"),
    )
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, null=False, blank=False
    )
    cpu_id = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.brand + " " + str(self.capacity) + "GB"


class Disk(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    capacity = models.IntegerField()
    TYPE_CHOICES = (
        ("ssd", "SSD"),
        ("hdd", "HDD"),
    )
    type = models.CharField(
        max_length=10, choices=TYPE_CHOICES, null=False, blank=False
    )
    write_speed = models.IntegerField()
    read_speed = models.IntegerField()
    cpu_id = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.brand + " " + str(self.capacity) + "GB"


class Processor(models.Model):
    brand = models.CharField(max_length=50, null=False, blank=False)
    model = models.CharField(max_length=50, null=False, blank=False)
    generation = models.IntegerField()
    ARCH_CHOICES = (("x86", "x86"), ("x64", "x64"), ("X32", "X32"))
    architecture = models.CharField(
        max_length=10, choices=ARCH_CHOICES, null=False, blank=False
    )
    speed = models.IntegerField()
    cores = models.IntegerField()
    threads = models.IntegerField()
    cpu_id = models.ForeignKey(Cpu, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return self.brand + " " + self.model
