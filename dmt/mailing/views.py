import re

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect, Http404
from django.urls import reverse


from .forms import SubscriberForm


def add_subscriber(request):
    if request.is_ajax() and request.POST.get('action') == 'post':
        data = {
            "name": request.POST.get('name'),
            "phone": re.sub(' ', '', request.POST.get('phone')),
            "email": request.POST.get('email'),
        }
        form = SubscriberForm(data)
        if form.is_valid():
            form.save()
            response_data = {'success': True}
            return JsonResponse(response_data)
        else:
            response_data = {'success': False, 
                             'form_errors': form.errors.get_json_data()}
            return JsonResponse(response_data, status=400)
    raise Http404

