from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from apps.main.forms import CreateComputerItem
from apps.main.models import LabItem, Laboratory
from django.views.generic import ListView, CreateView, UpdateView
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

class LabItemCreateView(CreateView):
    model = LabItem
    form_class = CreateComputerItem
    template_name = "labs/create.html"
    success_url = reverse_lazy("main:labs_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Ítem de laboratorio"
        return context

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)