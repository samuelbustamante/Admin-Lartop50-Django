# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from choices import *

from django.utils.translation import ugettext_lazy as _

class Center(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50,
        verbose_name=_('Name')
    )
    acronym = models.CharField(max_length=25,
        verbose_name=_('Acronym')
    )
    segment = models.CharField(max_length=1, choices=SEGMENTS,
        verbose_name=_('Segment')
    )
    country = models.CharField(max_length=2, choices=COUNTRIES,
        verbose_name=_('Country')
    )
    city = models.CharField(max_length=50,
        verbose_name=_('City')
    )
    url = models.URLField(blank=True,
        verbose_name=_('Website')
    )
    description = models.TextField(blank=True,
        verbose_name=_('Description')
    )

class System(models.Model):
    center = models.ForeignKey(Center)
    name = models.CharField(max_length=50,
        verbose_name=_('Name')
    )
    status = models.BooleanField(
        verbose_name=_('Status')
    )
    area = models.CharField(max_length=1, choices=AREAS,
        verbose_name=_('Areas')
    )
    description = models.TextField(
        verbose_name=_('Description')
    )
    vendor = models.CharField(max_length=50,
        verbose_name=_('Vendor')
    )
    year_install = models.CharField(max_length=2, choices=YEARS,
        verbose_name=_('Year install')
    )

class Component(models.Model):
    system = models.ForeignKey(System)
    name = models.CharField(max_length=50,
        verbose_name=_('Name')
    )
    model = models.CharField(max_length=50,
        verbose_name=_('Model')
    )
    vendor = models.CharField(max_length=50,
        verbose_name=_('Vendor')
    )
    nodes = models.IntegerField(
        verbose_name=_('Number of nodes')
    )
    memory_node = models.IntegerField(
        verbose_name=_('Memory per node (in Mb)')
    )
    # PROCESSOR
    processor_name = models.CharField(max_length=50,
        verbose_name=_('Processor name')
    )
    processor_model = models.CharField(max_length=50,
        verbose_name=_('Processor model')
    )
    processor_number = models.IntegerField(
        verbose_name=_('Number of processors')
    )
    processor_num_cores = models.IntegerField(
        verbose_name=_('Number of cores per processor')
    )
    processor_speed = models.FloatField(
        verbose_name=_('Speed processor')
    )
    # ACCELERATOR
    accelerator_name = models.CharField(max_length=50,
        verbose_name=_('Accelerator name')
    )
    accelerator_model = models.CharField(max_length=50,
        verbose_name=_('Accelerator model')
    )
    accelerator_number = models.IntegerField(
        verbose_name=_('Number of accelarators')
    )
    accelerator_num_cores = models.IntegerField(
        verbose_name=_('Number of cores per accelerator')
    )
    accelerator_speed = models.FloatField(
        verbose_name=_('Aceletator speed')
    )
    # POWER
    peak_power = models.FloatField(
        verbose_name=_('Peak power')
    )
    measured_power = models.FloatField(
        verbose_name=_('Measured power')
    )
    # CONFIGURATION
    interconection = models.CharField(max_length=50,
        verbose_name=_('Interconnection')
    )
    operating_system = models.CharField(max_length=50,
        verbose_name=_('Operating system')
    )

class Linpack(models.Model):
    system = models.ForeignKey(System, unique=True)
    benchmark_date = models.DateField(
        verbose_name=_('Benchmark date')
    )
    number_cores = models.IntegerField(
        verbose_name=_('Number of cores')
    )
    number_accelerator = models.IntegerField(
        verbose_name=_('Number of accelerators')
    )
    rmax = models.FloatField(
        verbose_name=_('rmax')
    )
    rpeak = models.FloatField(
        verbose_name=_('rpeak')
    )
    nmax = models.FloatField(
        verbose_name=_('nmax')
    )
    nhalf = models.FloatField(
        verbose_name=_('nhalft')
    )
    compiler_name = models.CharField(max_length=50,
        verbose_name=_('Compiler name')
    )
    compiler_options = models.CharField(max_length=50,
        verbose_name=_('Compier options')
    )
    math_library = models.CharField(max_length=50,
        verbose_name=_('Math library')
    )
    mpi_library = models.CharField(max_length=50,
        verbose_name=_('mpi library')
    )
    hpl_input = models.TextField(
        verbose_name=_('hpl input')
    )
    hpl_output = models.TextField(
        verbose_name=_('hpl output')
    )
