from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
import datetime

from django.http import HttpResponse
from django.template import loader


def interact(request):
    now = datetime.datetime.now()
    template = loader.get_template('interact.html')
    context = {
        'time' : now,
    }
    return HttpResponse(template.render(context, request))


def split(request):
    template = loader.get_template('split.html')
    context = {}
    return HttpResponse(template.render( context, request )  )


def split2(request):
    template = loader.get_template('split2.html')
    context = {}
    return HttpResponse(template.render( context, request )  )



def sort(request):
    template = loader.get_template('sort.html')
    context = {}
    return HttpResponse(template.render(context, request))
