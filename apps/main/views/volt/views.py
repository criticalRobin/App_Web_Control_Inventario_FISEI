from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.main.models import Regulator_voltage
from apps.main.forms import CreateRegulatorVoltageForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class RegulatorVoltageCreateView(CreateView):
    model = Regulator_voltage
    form_class = CreateRegulatorVoltageForm
    template_name = "volt/create.html"
    success_url = reverse_lazy("main:labs_list")

    
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