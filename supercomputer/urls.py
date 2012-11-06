# -*- encoding: utf-8 -*-

from django.conf.urls.defaults import patterns, include, url

urlpatterns = patterns('',

    # Centers
    url(r'^$',
        'supercomputer.views.all_centers',
        name='all_centers'
    ),
    url(r'^center/add/$',
        'supercomputer.views.add_center',
        name='add_center'
    ),
    url(r'^center/(?P<center>\d+)/$',
        'supercomputer.views.show_center',
        name='show_center'
    ),
    url(r'^center/(?P<center>\d+)/edit/$',
        'supercomputer.views.edit_center',
        name='edit_center'
    ),
    url(r'^center/(?P<center>\d+)/delete/$',
        'supercomputer.views.delete_center',
        name='delete_center'
    ),

    # Systems
    url(r'^center/(?P<center>\d+)/add/system/$',
        'supercomputer.views.add_system',
        name='add_system'
    ),
    url(r'^system/(?P<system>\d+)/$',
        'supercomputer.views.show_system',
        name='show_system'
    ),
    url(r'^system/(?P<system>\d+)/edit/$',
        'supercomputer.views.edit_system',
        name='edit_system'
    ),
    url(r'^system/(?P<system>\d+)/delete/$',
        'supercomputer.views.delete_system',
        name='delete_system'
    ),

    # Components
    url(r'^system/(?P<system>\d+)/add/component/$',
        'supercomputer.views.add_component',
        name='add_component'
    ),
    url(r'^component/(?P<component>\d+)/$',
        'supercomputer.views.show_component',
        name='show_component'
    ),
    url(r'^component/(?P<component>\d+)/edit/$',
        'supercomputer.views.edit_component',
        name='edit_component'
    ),
    url(r'^component/(?P<component>\d+)/delete/$',
        'supercomputer.views.delete_component',
        name='delete_component'
    ),

    # Linpacks
    url(r'^linpack/(?P<system>\d+)/add/linpack/$',
        'supercomputer.views.add_linpack',
        name='add_linpack'
    ),
    url(r'^linpack/(?P<linpack>\d+)/$',
        'supercomputer.views.show_linpack',
        name='show_linpack'
    ),
    url(r'^linpack/(?P<id_linpack>\d+)/edit/$',
        'supercomputer.views.edit_linpack',
        name='edit_linpack'
    ),
    url(r'^linpack/(?P<linpack>\d+)/delete/$',
        'supercomputer.views.delete_linpack',
        name='delete_linpack'
    ),

)
