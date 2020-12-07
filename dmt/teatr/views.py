from django.shortcuts import render
from .models import Actor, Repertoire
from django.views.generic import TemplateView
from mailing.forms import SubscriberForm


class HomeView(TemplateView):

    template_name = 'teatr_dmt/index.html'

    def post(self, request, *args, **kwargs):
        context = self.get_context_data()
        if context['mailing_form'].is_valid():
            context['mailing_form'].save()
            context['form_status'] = 'success'
        return super().render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["actors_2"] = Actor.objects.all()
        context['repertoire'] = Repertoire.objects.all()
        context['mailing_form'] = SubscriberForm(self.request.POST or None)
        return context