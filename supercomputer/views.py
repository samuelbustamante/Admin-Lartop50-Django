# -*- encoding: utf-8 -*-

from django.template import RequestContext
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from forms import CenterForm, SystemForm, ComponentForm, LinpackForm
from models import Center, System, Component, Linpack

#----- Centers -----#

@login_required
def all_centers(request):
    centers = Center.objects.filter(user=request.user)
    return render_to_response('supercomputer/all_centers.html', locals(),\
                             context_instance=RequestContext(request))

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
    systems = System.objects.filter(center=center.pk)

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

@login_required
def delete_center(request, center):
    center = get_object_or_404(Center, pk=center, user=request.user)

    systems = System.objects.filter(center=center.pk)

    if systems:
        for system in systems:
            Component.objects.filter(system=system.pk).delete()
            Linpack.objects.filter(system=system.pk).delete()
        systems.delete()

    center.delete()

    return redirect('all_centers')

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
    components = Component.objects.filter(system=system.pk)
    linpacks = Linpack.objects.filter(system=system.pk)

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

@login_required
def delete_system(request, system):
    system = get_object_or_404(System, pk=system, center__user=request.user)

    Component.objects.filter(system=system.pk).delete()
    Linpack.objects.filter(system=system.pk).delete()

    center = system.center
    system.delete()

    return redirect('show_center', center=center.pk)

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
            return redirect('show_component', component=component.pk)
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
    component = get_object_or_404(Component, pk=component,\
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

@login_required
def delete_component(request, component):
    component = get_object_or_404(Component, pk=component,\
                                  system__center__user=request.user)

    system = component.system
    component.delete()

    return redirect('show_system', system=system.pk)

#----- Linpacks -----#

@login_required
def add_linpack(request, system):
    system = get_object_or_404(System, pk=system, center__user=request.user)

    if request.method == 'POST':
        form = LinpackForm(request.POST)
        if form.is_valid():
            linpak = form.save(commit=False)
            linpak.system = system
            linpak.save()
            return redirect('show_system', system=system.pk)
    else:
        form = LinpackForm()
    return render_to_response('supercomputer/add_linpack.html', locals(),\
                              context_instance=RequestContext(request))

@login_required
def show_linpack(request, linpack):
    linpack = get_object_or_404(Linpack, pk=linpack,\
                               system__center__user=request.user)

    return render_to_response('supercomputer/show_linpack.html', locals(),\
                              context_instance=RequestContext(request))
        
@login_required
def edit_linpack(request, id_linpack):
    linpack = get_object_or_404(Linpack, pk=id_linpack,\
                               system__center__user=request.user)

    if request.method == 'POST':
        form = LinpackForm(request.POST, instance=linpack)
        if form.is_valid():
            linpak = form.save()
            return redirect('show_linpack', linpack=linpack.pk)
    else:
        form = LinpackForm(instance=linpack)
    return render_to_response('supercomputer/edit_linpack.html', locals(),\
                              context_instance=RequestContext(request))

@login_required
def delete_linpack(request, linpack):
    linpack = get_object_or_404(Linpack, pk=linpack,\
                               system__center__user=request.user)

    system = linpack.system
    linpack.delete()

    return redirect('show_system', system=system.pk)
