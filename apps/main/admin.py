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
