from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

from django.http import HttpResponse
from django.template import loader

from .models import Application


def index(request):
    latest_application_list = Application.objects.order_by('-company_name')[:50]
    template = loader.get_template('applications/index.html')
    context = {
        'latest_application_list': latest_application_list,
    }
    return HttpResponse(template.render(context, request))