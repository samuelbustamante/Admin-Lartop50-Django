# -*- encoding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CenterForm, SystemForm, ComponentForm, LinpackForm
from models import Center, System, Component, Linpack

#----- Centers -----#

@login_required
def add_center(request):
    if request.method == 'POST':
        form = CenterForm(request.POST)
        if form.is_valid():
            center = form.save(commit=False)
            center.user = request.user
            center.save()
            return redirect('show_center', center=center.pk)
    else:
        form = CenterForm
    return render_to_response('supercomputer/add_center.html', locals(),\
                             context_instance=RequestContext(request))

@login_required
def show_center(request, center):
    center = get_object_or_404(Center, pk=center, user=request.user)

    return render_to_response('supercomputer/show_center.html', locals(),\
                             context_instance=RequestContext(request))
        

@login_required
def edit_center(request, center):
    center = get_object_or_404(Center, pk=center, user=request.user)

    if request.method == 'POST':
        form = CenterForm(request.POST, instance=center)
        if form.is_valid():
            center = form.save()
            return redirect('show_center', center=center.pk)
    else:
        form = CenterForm(instance=center)
    return render_to_response('supercomputer/edit_center.html', locals(),\
                             context_instance=RequestContext(request))

#----- Systems -----#

@login_required
def add_system(request, center):
    center = get_object_or_404(Center, pk=center, user=request.user)

    if request.method == 'POST':
        form = SystemForm(request.POST)
        if form.is_valid():
            system = form.save(commit=False)
            system.center = center
            system.save()
            return redirect('show_system', system=system.pk)
    else:
        form = SystemForm()
    return render_to_response('supercomputer/add_system.html', locals(),\
                             context_instance=RequestContext(request))

@login_required
def show_system(request, system):
    system = get_object_or_404(System, pk=system, center__user=request.user)

    return render_to_response('supercomputer/show_system.html', locals(),\
                             context_instance=RequestContext(request))

@login_required
def edit_system(request, system):
    system = get_object_or_404(System, pk=system, center__user=request.user)

    if request.method == 'POST':
        form = SystemForm(request.POST, instance=system)
        if form.is_valid():
            system = form.save()
            return redirect('show_system', system=center.pk)
    else:
        form = SystemForm(instance=system)
    return render_to_response('supercomputer/edit_system.html', locals(),\
                             context_instance=RequestContext(request))

#----- Components -----#

@login_required
def add_component(request, system):
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
    return render_to_response('supercomputer/add_component.html', locals(),\
                              context_instance=RequestContext(request))

@login_required
def show_component(request, component):
    component = get_object_or_404(Component, pk=component,\
                                  system__center__user=request.user)

    return render_to_response('supercomputer/show_component.html', locals(),\
                              context_instance=RequestContext(request))
        
@login_required
def edit_component(request, component):
    component = get_object_or_404(System, pk=component,\
                                  system__center__user=request.user)

    if request.method == 'POST':
        form = ComponentForm(request.POST, instance=component)
        if form.is_valid():
            component = form.save()
            return redirect('show_component', component=component.pk)
    else:
        form = ComponentForm(instance=component)
    return render_to_response('supercomputer/edit_component.html', locals(),\
                              context_instance=RequestContext(request))

#----- Linpaks -----#

@login_required
def add_linpak(request, system):
    system = get_object_or_404(System, pk=system, center__user=request.user)

    if request.method == 'POST':
        form = LinpakForm(request.POST)
        if form.is_valid():
            linpak = form.save(commit=False)
            linpak.system = system
            linpak.save()
            return redirect('show_system', system=system.pk)
    else:
        form = LinpakForm()
    return render_to_response('supercomputer/add_linpak.html', locals(),\
                              context_instance=RequestContext(request))

@login_required
def show_linpak(request, linpak):
    system = get_object_or_404(Linpak, pk=linpak,\
                               system__center__user=request.user)

    return render_to_response('supercomputer/show_linpak.html', locals(),\
                              context_instance=RequestContext(request))
        
@login_required
def edit_linpak(request, id_linpak):
    linpak = get_object_or_404(Linpak, pk=id_linpak,\
                               system__center__user=request.user)

    if request.method == 'POST':
        form = LinpakForm(request.POST, instance=linpak)
        if form.is_valid():
            linpak = form.save()
            return redirect('show_linpak', id_linpak=linpak.pk)
    else:
        form = LinpakForm(instance=linpak)
    return render_to_response('supercomputer/edit_linpak.html', locals(),\
                              context_instance=RequestContext(request))

