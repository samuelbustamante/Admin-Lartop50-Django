# -*- encoding: utf-8 -*-

from django.contrib import admin
from models import *

class CenterAdmin(admin.ModelAdmin):
    pass

class SystemAdmin(admin.ModelAdmin):
    pass

class ComponentAdmin(admin.ModelAdmin):
    pass

class LinpackAdmin(admin.ModelAdmin):
    pass

admin.site.register(Center, CenterAdmin)
admin.site.register(System, SystemAdmin)
admin.site.register(Component, ComponentAdmin)
admin.site.register(Linpack, LinpackAdmin)
