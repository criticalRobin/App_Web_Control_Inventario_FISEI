from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.main.models import Laboratory
from apps.main.forms import CreateLaboratoryForm, UpdateLaboratoryForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.views import dashboard_stats_view


class LaboratoryListView(ListView):
    model = Laboratory
    template_name = "labs/list.html"
    context_object_name = 'laboratories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Laboratorios'
        return context

class LaboratoryDashboardListView(ListView):
    model = Laboratory
    template_name = "labs/list_dashboard.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard_context = dashboard_stats_view(self.request)
        context.update(dashboard_context)
        return context

class LaboratoryCreateView(CreateView):
    model = Laboratory
    form_class = CreateLaboratoryForm
    template_name = "labs/create.html"
    success_url = reverse_lazy("main:labs_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Laboratorio"
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


class LaboratoryUpdateView(UpdateView):
    model = Laboratory
    form_class = UpdateLaboratoryForm
    template_name = "labs/update.html"
    success_url = reverse_lazy("main:labs_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Laboratorio'
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.form_class(request.POST, instance=self.object)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(self.success_url)
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)
