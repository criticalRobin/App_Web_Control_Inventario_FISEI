from django.urls import path
from apps.main.views.computers.views import ComputerCreateView
from apps.main.views.labs.views import LaboratoryCreateView, LaboratoryListView
from apps.main.views.recomms.views import RecommendationCreateView
from apps.main.views.tasks.views import TaskCreateView
from apps.main.views.items.views import LabItemListView


app_name = "main"

urlpatterns = [
    # LIST URLS
    path("labs/", LaboratoryListView.as_view(), name="labs_list"),
    path("labs/<int:pk>/items/", LabItemListView.as_view(), name="items_list"),
]
