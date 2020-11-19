from django.shortcuts import render
from .models import Actor, Repertoire
from django.views.generic import TemplateView


def index(request):
    context = {
        'actors': Actor.objects.all(),
        'repertoire': Repertoire.objects.all()
    }
    template_name = 'teatr/index.html'
    return render(request, template_name, context=context)

class HomeView(TemplateView):

    template_name = 'teatr_dmt/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['actors'] = Actor.objects.all()
        context['repertoire'] = Repertoire.objects.all()
        return context