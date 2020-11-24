from django.shortcuts import render
from .models import Actor, Repertoire
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = 'teatr_dmt/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        actors_count = Actor.objects.all().count()
        acacac = []

        for i in range(0, actors_count, 2):
            if i + 1 < actors_count:
                acacac.append((Actor.objects.all()[i], Actor.objects.all()[i+1]))
            else:
                acacac.append((Actor.objects.all()[i],))
        print(acacac)
        context['actors'] = acacac
        context['repertoire'] = Repertoire.objects.all()
        return context