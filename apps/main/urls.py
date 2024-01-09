from django.urls import path
from apps.main.views.computers.views import *

from apps.main.views.labs.views import *
from apps.main.views.computerItems.views import *

from apps.main.views.recomms.views import *
from apps.main.views.tasks.views import *
from apps.main.views.labItems.views import *


app_name = "main"

urlpatterns = [
    path("lab/create/", LaboratoryCreateView.as_view(), name="laboratory_create"),
    path("lab/list/", LaboratoryListView.as_view(), name="labs_list"),
    path(
        "lab/update/<int:pk>/", LaboratoryUpdateView.as_view(), name="laboratory_update"
    ),
    path("computer/create/", ComputerCreateView.as_view(), name="computer_create"),
    path("computer/list/", ComputerListView.as_view(), name="computers_list"),
    path(
        "computer/update/<int:pk>/",
        ComputerUpdateView.as_view(),
        name="computer_update",
    ),
    path("compitem/create/", ComputerItemsCreateView.as_view(), name="compitem_create"),
    path("compitem/list/", ComputerItemListView.as_view(), name="compitems_list"),
    path(
        "compitem/update/<int:pk>/",
        ComputerItemsUpdateView.as_view(),
        name="compitem_update",
    ),
    path("labitem/create/", LabItemCreateView.as_view(), name="labitem_create"),
    path("labitem/list/", LabItemListView.as_view(), name="labitems_list"),
    path(
        "labitem/update/<int:pk>/", LabItemUpdateView.as_view(), name="labitem_update"
    ),
    path("recomm/create/", RecommendationCreateView.as_view(), name="recomm_create"),
    path("recomm/list/", RecommendationAllListView.as_view(), name="recomms_list"),
    path(
        "recomm/update/<int:pk>/",
        RecommendationUpdateView.as_view(),
        name="recomm_update",
    ),
    path("task/create/", TaskCreateView.as_view(), name="task_create"),
    path("task/list/", TaskAllListView.as_view(), name="tasks_list"),
    path("task/update/<int:pk>/", TaskUpdateView.as_view(), name="task_update"),
    path("labs/", LaboratoryDashboardListView.as_view(), name="labsd_list"),
    path(
        "labs/<int:pk>/items/", LabItemListDasboardView.as_view(), name="labitemsd_list"
    ),
    path("computers/", ComputerListDasboardView.as_view(), name="computersd_list"),
    path("recomms/", RecommendationListView.as_view(), name="recommsd_list"),
    path("tasks/", TaskListView.as_view(), name="tasksd_list"),
    path(
        "computer/<int:pk>/list_items/",
        ComputerItemsByPcList.as_view(),
        name="comp_items",
    ),
]
