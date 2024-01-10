from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from apps.main.forms import *
from apps.main.models import LabItem, Laboratory
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.views import dashboard_stats_view


class LabItemListView(ListView):
    model = LabItem
    template_name = "items/list_all.html"
    context_object_name = "Items"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Items de laboratorio"
        return context

class LabItemCreateView(CreateView):
    model = LabItem
    form_class = CreateLabItemForm
    template_name = "items/create.html"
    success_url = reverse_lazy("main:labitems_list")

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

class LabItemUpdateView(UpdateView):
    model = LabItem
    form_class = UpdateLabItemForm
    template_name = "items/update.html"
    success_url = reverse_lazy("main:labitems_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Actualizar Ítem de laboratorio'
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

class LabItemListDasboardView(ListView):
    model = LabItem
    template_name = "items/list.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        labid = self.kwargs['pk']
        computers = Computer.objects.filter(lab_id=labid, responsible_user_id=self.request.user)
        items = LabItem.objects.filter(id_laboratory=labid, responsible_user_id=self.request.user)
        computer_items_grouped = {
            computer.id: ComputerItem.objects.filter(id_computer=computer)
            for computer in computers
        }

        dashboard_context = dashboard_stats_view(self.request)
        context.update(dashboard_context)
        
        context["lab_items"] = items
        context["computers"] = computers
        context["computer_items_grouped"] = computer_items_grouped
        print(context["computers"])
        # print(context["computer_items_grouped"])
        return context