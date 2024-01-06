from django.urls import path
from apps.main.views.air.views import AirConditionerCreateView
from apps.main.views.camera.views import SecurityCameraCreateView
from apps.main.views.computers.views import ComputerCreateView
from apps.main.views.cpus.views import CpuCreateView
from apps.main.views.disks.views import DiskCreateView
from apps.main.views.labs.views import LaboratoryCreateView
from apps.main.views.monitors.views import MonitorCreateView
from apps.main.views.processors.views import ProcessorCreateView
from apps.main.views.projectors.views import ProjectorCreateView
from apps.main.views.rams.views import RamCreateView
from apps.main.views.recomms.views import RecommendationCreateView
from apps.main.views.tasks.views import TaskCreateView
from apps.main.views.volt.views import RegulatorVoltageCreateView


app_name = "main"

urlpatterns = [
    # CREATE

]
