# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views.decorators.cache import never_cache

from .utils import collect, GIF_DATA

@never_cache
def google_analytics(request):
    response = HttpResponse('', 'image/gif', 200)
    response.write(GIF_DATA)
    return collect(request, response)
