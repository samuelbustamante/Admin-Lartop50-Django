# -*- encoding: utf-8 -*-

from django import forms
from models import Center, System, Component, Linpack
from choices import SEGMENTS, COUNTRIES, AREAS, YEARS
from django.utils.translation import ugettext_lazy as _

class CenterForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
        label=_('Name')
    )
    acronym = forms.CharField(max_length=25,
        label=_('Acronym')
    )
    segment = forms.ChoiceField(choices=SEGMENTS,
        label=_('Segment')
    )
    country = forms.ChoiceField(choices=COUNTRIES,
        label=_('Countrie')
    )
    city = forms.CharField(max_length=50,
        label=_('City')
    )
    url = forms.URLField(
        label=_('Website')
    )
    description = forms.CharField(widget=forms.Textarea,
        label=_('Description')
    )

    class Meta:
        model = Center
        exclude = ('user',)

class SystemForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
        label=_('Name')
    )
    status = forms.BooleanField(
        label=_('Status')
    )
    area = forms.ChoiceField(choices=AREAS,
        label=_('Area')
    )
    description = forms.CharField(widget=forms.Textarea,
        label=_('Decription')
    )
    vendor = forms.CharField(max_length=50,
        label=_('Vendor')
    )
    year_install = forms.ChoiceField(choices=YEARS,
        label=_('Year install')
    )

    class Meta:
        model = System
        exclude = ('center',)

class ComponentForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
        label=_('Name')
    )
    model = forms.CharField(max_length=50,
        label=_('Model')
    )
    vendor = forms.CharField(max_length=50,
        label=_('Vendor')
    )
    nodes = forms.IntegerField(
        label=_('Number of nodes')
    )
    memory_node = forms.IntegerField(
        label=_('Memory per node (in Mb)')
    )
    processor_name = forms.CharField(max_length=50,
        label=_('Processor name')
    )
    processor_model = forms.CharField(max_length=50,
        label=_('Processor model')
    )
    processor_number = forms.IntegerField(
        label=_('Number of processors')
    )
    processor_num_cores = forms.IntegerField(
        label=_('Number of cores per processor')
    )
    processor_speed = forms.FloatField(
        label=_('Speed processor')
    )
    accelerator_name = forms.CharField(max_length=50,
        label=_('Accelerator name')
    )
    accelerator_model = forms.CharField(max_length=50,
        label=_('Accelerator model')
    )
    accelerator_number = forms.IntegerField(
        label=_('Number of accelarators')
    )
    accelerator_num_cores = forms.IntegerField(
        label=_('Number of cores per accelerator')
    )
    accelerator_speed = forms.FloatField(
        label=_('Aceletator speed')
    )
    peak_power = forms.FloatField(
        label=_('Peak power')
    )
    measured_power = forms.FloatField(
        label=_('Measured power')
    )
    interconection = forms.CharField(max_length=50,
        label=_('Interconnection')
    )
    operating_system = forms.CharField(max_length=50,
        label=_('Operating system')
    )

    class Meta:
        model = Component
        exclude = ('system',)

class LinpackForm(forms.ModelForm):
    benchmark_date = forms.DateField(
        label=_('Benchmark date')
    )
    number_cores = forms.IntegerField(
        label=_('Number of cores')
    )
    number_accelerator = forms.IntegerField(
        label=_('Number of accelerators')
    )
    rmax = forms.FloatField(
        label=_('rmax')
    )
    rpeak = forms.FloatField(
        label=_('rpeak')
    )
    nmax = forms.FloatField(
        label=_('nmax')
    )
    nhalf = forms.FloatField(
        label=_('nhalft')
    )
    compiler_name = forms.CharField(max_length=50,
        label=_('Compiler name')
    )
    compiler_options = forms.CharField(max_length=50,
        label=_('Compier options')
    )
    math_library = forms.CharField(max_length=50,
        label=_('Math library')
    )
    mpi_library = forms.CharField(max_length=50,
        label=_('mpi library')
    )
    hpl_input = forms.CharField(widget=forms.Textarea,
        label=_('hpl input')
    )
    hpl_output = forms.CharField(widget=forms.Textarea,
        label=_('hpl output')
    )

    class Meta:
        model = Linpack
        exclude = ('system',)
