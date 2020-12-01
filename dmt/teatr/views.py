from django.shortcuts import render
from .models import Actor, Repertoire
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'teatr_dmt/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actors_count = Actor.objects.all().count()
        context["actors_2"] = Actor.objects.all()
        context['repertoire'] = Repertoire.objects.all()
        return context