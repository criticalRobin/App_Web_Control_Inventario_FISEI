from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.main.models import ComputerItem
from apps.main.forms import CreateComputerItem, UpdateComputerItemForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class ComputerItemListView(ListView):
    model = ComputerItem
    template_name = "computerItems/list.html"
    context_object_name = "computerItems"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de items de computadora"
        return context

class ComputerItemsCreateView(CreateView):
    model = ComputerItem
    form_class = CreateComputerItem
    template_name = "computerItems/create.html"
    success_url = reverse_lazy("main:compitems_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Item de computadora"
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


class ComputerItemsUpdateView(UpdateView):
    model = ComputerItem
    form_class = UpdateComputerItemForm
    template_name = "computerItems/update.html"
    success_url = reverse_lazy("main:compitems_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar item de computadora"
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