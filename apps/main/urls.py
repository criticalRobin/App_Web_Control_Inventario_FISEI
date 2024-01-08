from django.urls import path
from apps.main.views.computers.views import ComputerCreateView, ComputerListView
from apps.main.views.labs.views import LaboratoryCreateView, LaboratoryListView
from apps.main.views.recomms.views import (
    RecommendationCreateView,
    RecommendationListView,
)
from apps.main.views.tasks.views import TaskCreateView, TaskListView
from apps.main.views.items.views import LabItemListView


app_name = "main"

urlpatterns = [
    # LIST URLS
    path("labs/", LaboratoryListView.as_view(), name="labs_list"),
    path("labs/<int:pk>/items/", LabItemListView.as_view(), name="items_list"),
    path("computers/", ComputerListView.as_view(), name="computers_list"),
    path("recomms/", RecommendationListView.as_view(), name="recomms_list"),
    path("tasks/", TaskListView.as_view(), name="tasks_list"),
]
