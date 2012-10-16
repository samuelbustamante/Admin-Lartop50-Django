# -*- encoding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import CenterForm, SystemForm, ComponentForm, LinpackForm

def panel(request):
    center = CenterForm()
    system = SystemForm()
    coponent = ComponentForm()
    linpack = LinpackForm()
    return render_to_response('supercomputers/panel.html', locals(), context_instance=RequestContext(request))
