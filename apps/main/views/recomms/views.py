from django.shortcuts import render
from django.http import HttpResponseRedirect
from apps.main.models import Recommendation
from apps.main.forms import CreateRecommendationForm, UpdateRecommendationForm
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from home.views import dashboard_stats_view


class RecommendationListView(ListView):
    model = Recommendation
    template_name = "recomms/list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        dashboard_context = dashboard_stats_view(self.request)
        context.update(dashboard_context)
        return context


class RecommendationCreateView(CreateView):
    model = Recommendation
    form_class = CreateRecommendationForm
    template_name = "recomms/create.html"
    success_url = reverse_lazy("main:recomms_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Recomendación'
        return context
    
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            user = request.user
            form.user_id = user
            form.save()
            return HttpResponseRedirect(self.success_url)
        self.object = None
        context = self.get_context_data(**kwargs)
        context["form"] = form
        return render(request, self.template_name, context)


class RecommendationUpdateView(UpdateView):
    model = Recommendation
    form_class = UpdateRecommendationForm
    template_name = "recomms/update.html"
    success_url = reverse_lazy("main:recomms_list")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["title"] = "Actualizar Recomendación"
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