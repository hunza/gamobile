# -*- coding: utf-8 -*-
from django.conf import settings

PROTOCOL_VERSION = getattr(settings, 'GOOGLE_ANALYTICS_PROTOCOL_VERSION', '1')
ENDPOINT_URL = getattr(settings, 'GOOGLE_ANALYTICS_ENDPOINT_URL', 'http://www.google-analytics.com/collect')
TRACKING_ID = getattr(settings, 'GOOGLE_ANALYTICS_TRACKING_ID', None)
COOKIE_NAME = getattr(settings, 'GOOGLE_ANALYTICS_COOKIE_NAME', 'gamobile')
COOKIE_PATH = getattr(settings, 'GOOGLE_ANALYTICS_COOKIE_PATH', '/')
COOKIE_USER_PERSISTENCE = getattr(settings, 'GOOGLE_ANALYTICS_COOKIE_USER_PERSISTENCE', 63072000)
