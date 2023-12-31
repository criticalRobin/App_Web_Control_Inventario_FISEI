from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from apps.main.models import Task, Recommendation
from apps.main.forms import CreateTaskForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("main:labs_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Tareas'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        recomm_id = kwargs["pk"]
        recomm = get_object_or_404(Recommendation, pk=recomm_id)
        form = self.form_class(request.POST)

        if form.is_valid():
            form = form.save(commit=False)
            form.recommendation_id = recomm
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)
