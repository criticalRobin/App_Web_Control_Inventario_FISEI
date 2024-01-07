from apps.main.models import LabItem, Laboratory
from django.views.generic import ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.views import dashboard_stats_view


class LabItemListView(ListView):
    model = LabItem
    template_name = "items/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        lab = self.kwargs["pk"]
        laboratory = Laboratory.objects.get(id=lab)
        lab_items = LabItem.objects.filter(id_laboratory=laboratory)
        context["lab_items"] = lab_items
        dashboard_context = dashboard_stats_view(self.request)
        context.update(dashboard_context)
        return context
