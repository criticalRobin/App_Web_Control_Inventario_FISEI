from django.urls import path
from apps.main.views.computers.views import ComputerCreateView

from apps.main.views.labs.views import *

from apps.main.views.recomms.views import RecommendationCreateView
from apps.main.views.tasks.views import TaskCreateView



app_name = "main"

urlpatterns = [
    path('lab/create/', LaboratoryCreateView.as_view(), name='laboratory_create'),
    path('lab/list/', LaboratoryListView.as_view(), name='labs_list'),
    path('lab/update/<int:pk>/', LaboratoryUpdateView.as_view(), name='laboratory_update'),

]
