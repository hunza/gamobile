# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import urllib

from django import template
from django.core.urlresolvers import reverse
from ..utils import get_tracking_id

register = template.Library()

@register.assignment_tag
def enable_tracking():
    return get_tracking_id() is not None

@register.simple_tag(takes_context=True)
def google_analytics_image_url(context):
    request = context.get('request')
    if not request:
        raise RuntimeError('request does not exist')

    params = {
        'GUID': 'ON',
        'utmr': request.META.get('HTTP_REFERER', '-'),
    }
    if request.path:
        params['utmp'] = request.path

    return "{0}?{1}".format(reverse('google_analytics'), urllib.urlencode(params))
