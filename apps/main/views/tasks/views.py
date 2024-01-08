from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from apps.main.models import Task, Recommendation
from apps.main.forms import CreateTaskForm, UpdateTaskForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.views import dashboard_stats_view


class TaskListView(ListView):
    template_name = "tasks/list.html"
    model = Task

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard_context = dashboard_stats_view(self.request)
        context.update(dashboard_context)
        return context


class TaskCreateView(CreateView):
    model = Task
    form_class = CreateTaskForm
    template_name = "tasks/create.html"
    success_url = reverse_lazy("main:tasks_list")

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


class TaskUpdateView(UpdateView):
    model = Task
    form_class = UpdateTaskForm
    template_name = "recomms/update.html"
    success_url = reverse_lazy("main:tasks_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar Tarea"
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