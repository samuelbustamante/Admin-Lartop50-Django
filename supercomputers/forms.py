# -*- encoding: utf-8 -*-

from django import forms
from models import Center, System, Component, Linpack
from choices import SEGMENTS, COUNTRIES, AREAS, YEARS
from django.utils.translation import ugettext_lazy as _

class CenterForm(forms.ModelForm):
    name = forms.CharField(max_length=50,
        verbose_name=_('Name'),
        help_text=_('Insert name of center')
    )
    acronym = forms.CharField(max_length=25,
        verbose_name=_('Acronym'),
        help_text=_('Insert acronym of center')
    )
    segment = forms.ChoiceField(choices=SEGMENTS,
        verbose_name=_('Segment'),
        help_text=_('Select the segment from the center')
    )
    country = forms.ChoiceField(choices=COUNTRIES,
        verbose_name=_('Countrie'),
        help_text=_('Select the countrie of center')
    )
    city = forms.CharField(max_length=50,
        verbose_name=_('City'),
        help_text=_('Select the city of center')
    )
    url = forms.URLField(
        verbose_name=_('Website'),
        help_text=_('Input website of center')
    )
    description = forms.CharField(widget=forms.Textarea,
        verbose_name=_('Description'),
        help_text=_('Input a short description')
    )

    class Meta:
        model = Center
        exclude = ('user',)
