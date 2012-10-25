# -*- encoding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CenterForm, SystemForm, ComponentForm, LinpackForm
from models import Center, System, Component, Linpack
from django.http import Http404

def panel(request):
    center = CenterForm()
    system = SystemForm()
    coponent = ComponentForm()
    linpack = LinpackForm()
    return render_to_response('supercomputers/panel.html', locals(),
                             context_instance=RequestContext(request))

#----- Centers -----#

@login_required
def create_center(request):
    if request.method == 'POST':
        form = CenterForm(request.POST)
        if form.is_valid():
            center = form.save(commit=False)
            center.user = request.user
            center.save()
            return redirect('show_center', center=center.pk)
    else:
        form = CenterForm
    return render_to_response('supercomputers/create_center.html', locals(),
                             context_instance=RequestContext(request))

@login_required
def show_center(request, center):
    try:
        center = Center.objects.get(pk=center, user=request.user)
    except Center.DoesNotExist:
        raise Http404
    return render_to_response('supercomputers/show_center.html', locals(),
                             context_instance=RequestContext(request))
        

@login_required
def edit_center(request, center):
    try:
        center = Center.objects.get(pk=center, user=request.user)
    except Center.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            center = form.save()
            return redirect('show_center', center=center.pk)
    else:
        form = CenterForm(instance=center)
    return render_to_response('supercomputers/edit_center.html', locals(),
                             context_instance=RequestContext(request))

#----- Systems -----#

@login_required
def create_system(request, center):
    try:
        center = Center.objects.get(pk=center, user=request.user)
    except Center.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.center = center
            system.save()
            return redirect('show_system', system=system.pk)
    else:
        form = SystemForm()
    return render_to_response('supercomputers/create_system.html', locals(),
                             context_instance=RequestContext(request))

@login_required
def show_system(request, system):
    try:
        system = System.objects.get(pk=system, center__user=request.user)
    except System.DoesNotExist:
        raise Http404
    return render_to_response('supercomputers/show_system.html', locals(),
                             context_instance=RequestContext(request))
        
@login_required
def edit_system(request, system):
    try:
        system = System.objects.get(pk=system, center__user=request.user)
    except System.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            system = form.save()
            return redirect('show_system', system=center.pk)
    else:
        form = SystemForm(instance=system)
    return render_to_response('supercomputers/edit_system.html', locals(),
                             context_instance=RequestContext(request))

#----- Components -----#

@login_required
def create_component(request, system):
    system = get_object_or_404(System, pk=system, center__user=request.user)

    if request.method == 'POST':
        form = ComponentForm(request.POST)
        if form.is_valid():
            component = form.save(commit=False)
            component.system = system
            component.save()
            return redirect('show_component', system=system.pk)
    else:
        form = ComponentForm()
    return render_to_response('supercomputers/create_component.html', locals(),
                             context_instance=RequestContext(request))

@login_required
def show_component(request, component):
    component = get_object_or_404(Component, pk=component,
                                 system__center__user=request.user)

    return render_to_response('supercomputers/show_component.html', locals(),
                             context_instance=RequestContext(request))
        
@login_required
def edit_component(request, component):
    component = get_object_or_404(System, pk=component,
                                 system__center__user=request.user)

    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            component = form.save()
            return redirect('show_component', component=component.pk)
    else:
        form = ComponentForm(instance=component)
    return render_to_response('supercomputers/edit_component.html', locals(),
                             context_instance=RequestContext(request))

