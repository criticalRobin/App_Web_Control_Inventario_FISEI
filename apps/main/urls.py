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
    path("air/create/", AirConditionerCreateView.as_view(), name="air_create"),
    path("camera/create/", SecurityCameraCreateView.as_view(), name="camera_create"),
    path("computer/create/", ComputerCreateView.as_view(), name="computer_create"),
    path("cpu/create/", CpuCreateView.as_view(), name="cpu_create"),
    path("disk/create/", DiskCreateView.as_view(), name="disk_create"),
    path("lab/create/", LaboratoryCreateView.as_view(), name="lab_create"),
    path("monitor/create/", MonitorCreateView.as_view(), name="monitor_create"),
    path("processor/create/", ProcessorCreateView.as_view(), name="processor_create"),
    path("projector/create/", ProjectorCreateView.as_view(), name="projector_create"),
    path("ram/create/", RamCreateView.as_view(), name="ram_create"),
    path("recomm/create/", RecommendationCreateView.as_view(), name="recomm_create"),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("volt/create/", RegulatorVoltageCreateView.as_view(), name="volt_create"),
]
