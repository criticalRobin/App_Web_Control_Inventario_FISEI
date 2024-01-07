from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.main.models import Computer
from apps.main.forms import CreateComputerForm, UpdateComputerForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class ComputerListView(ListView):
    model = Computer
    template_name = "computers/list.html"
    context_object_name = "computers"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Lista de Computadoras"
        return context


class ComputerCreateView(CreateView):
    model = Computer
    form_class = CreateComputerForm
    template_name = "computers/create.html"
    success_url = reverse_lazy("main:computers_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Computadora"
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


class ComputerUpdateView(UpdateView):
    model = Computer
    form_class = UpdateComputerForm
    template_name = "computers/update.html"
    success_url = reverse_lazy("main:computers_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar Computadora"
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
