# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import patterns, url

urlpatterns = patterns(
    '',
    url(r'^ga/$', 'gamobile.views.google_analytics', name='google_analytics'),
)
