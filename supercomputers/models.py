# -*- encoding: utf-8 -*-

from django.contrib.auth.models import User
from django.db import models
from choices import *

class Center(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=50)
    acronym = models.CharField(max_length=25)
    segment = models.CharField(max_length=1, choices=SEGMENTS)
    country = models.CharField(max_length=2, choices=COUNTRIES)
    city = models.CharField(max_length=50)
    url = models.URLField(blank=True)
    description = models.TextField(blank=True)

class System(models.Model):
    center = models.ForeignKey(Center)
    name = models.CharField(max_length=50)
    status = models.BooleanField()
    area = models.CharField(max_length=1, choices=AREAS)
    description = models.TextField()
    vendor = models.CharField(max_length=50)
    year_install = models.CharField(max_length=2, choices=YEARS)

class Component(models.Model):
    system = models.ForeignKey(System)
    name = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    vendor = models.CharField(max_length=50)
    nodes = models.IntegerField()
    memory_node = models.IntegerField()
    # PROCESSOR
    processor_name = models.CharField(max_length=50)
    processor_model = models.CharField(max_length=50)
    processor_number = models.IntegerField()
    processor_num_cores = models.IntegerField()
    processor_speed = models.FloatField()
    # ACCELERATOR
    accelerator_name = models.CharField(max_length=50 )
    accelerator_model = models.CharField(max_length=50)
    accelerator_number = models.IntegerField()
    accelerator_num_cores = models.IntegerField()
    accelerator_speed = models.FloatField()
    # POWER
    peak_power = models.FloatField()
    measured_power = models.FloatField()
    # CONFIGURATION
    interconection = models.CharField(max_length=50)
    operating_system = models.CharField(max_length=50)

class Linpack(models.Model):
    system = models.ForeignKey(System, unique=True)
    benchmark_date = models.DateField()
    number_cores = models.IntegerField()
    number_gpu_cores = models.IntegerField()
    rmax = models.FloatField()
    rpeak = models.FloatField()
    nmax = models.FloatField()
    nhalf = models.FloatField()
    compiler_name = models.CharField(max_length=50)
    compiler_options = models.CharField(max_length=50)
    math_library = models.CharField(max_length=50)
    mpi_library = models.CharField(max_length=50)
    hpl_input = models.TextField()
    hpl_output = models.TextField()
