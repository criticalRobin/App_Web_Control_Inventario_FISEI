from apps.main.models import LabItem
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.views import dashboard_stats_view


class LaboratoryListView(ListView):
    model = LabItem
    template_name = "items/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard_context = dashboard_stats_view(self.request)
        context.update(dashboard_context)
        return context