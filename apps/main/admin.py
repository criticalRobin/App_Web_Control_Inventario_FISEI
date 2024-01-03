from django.contrib import admin
from .models import (
    Computer,
    Laboratory,
    Projector,
    Recommendation,
    Cpu,
    Monitor,
    Task,
    Processor,
    Disk,
    Ram,
    Air_Conditioner,
    Regulator_voltage,
    Security_camera,
)

# Register your models here.
admin.site.register(Computer)
admin.site.register(Laboratory)
admin.site.register(Projector)
admin.site.register(Recommendation)
admin.site.register(Cpu)
admin.site.register(Monitor)
admin.site.register(Task)
admin.site.register(Processor)
admin.site.register(Disk)
admin.site.register(Ram)
admin.site.register(Air_Conditioner)
admin.site.register(Regulator_voltage)
admin.site.register(Security_camera)
