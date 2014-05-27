# -*- coding: utf-8 -*-
from hashlib import md5
import requests
import struct
import time
import uuid

import gamobile_settings as settings

GIF_DATA = reduce(lambda x, y: x + struct.pack('B', y),
                  [0x47, 0x49, 0x46, 0x38, 0x39, 0x61,
                   0x01, 0x00, 0x01, 0x00, 0x80, 0x00,
                   0x00, 0x00, 0x00, 0x00, 0xff, 0xff,
                   0xff, 0x21, 0xf9, 0x04, 0x01, 0x00,
                   0x00, 0x00, 0x00, 0x2c, 0x00, 0x00,
                   0x00, 0x00, 0x01, 0x00, 0x01, 0x00,
                   0x00, 0x02, 0x01, 0x44, 0x00, 0x3b], '')

def set_cookie(response, client_id):
    localtime = time.localtime(time.time() + settings.COOKIE_USER_PERSISTENCE)

    response.set_cookie(
        settings.COOKIE_NAME,
        value=client_id,
        expires=time.strftime('%a, %d-%b-%Y %H:%M:%S %Z', localtime),
        path=settings.COOKIE_PATH,
        )

    return response

def get_client_id(guid, account, user_agent, cookie):
    if cookie:
        return cookie

    message = ''
    if guid:
        # Create the visitor id using the guid.
        message = guid + account
    else:
        # otherwise this is a new user, create a new random id.
        message = user_agent + str(uuid.uuid4())

    md5_string = md5(message).hexdigest()
    return "0x" + md5_string[:16]

def get_guid(request):
    for key in ['DCMGUID', 'UP_SUBNO', 'JPHONE_UID', 'EM_UID']:
        guid = request.META.get('HTTP_X_' + key)
        if guid:
            return guid

    return guid

def get_tracking_id():
    return settings.TRACKING_ID

def collect(request, response):
    guid = get_guid(request)
    tracking_id = get_tracking_id()
    user_agent = request.META.get('HTTP_USER_AGENT', '')
    cookie = request.COOKIES.get(settings.COOKIE_NAME)
    client_id = get_client_id(guid=guid, account=tracking_id, user_agent=user_agent, cookie=cookie)

    payload_data = {
        't': 'pageview',
        'v': settings.PROTOCOL_VERSION,
        'tid': tracking_id,
        'cid': client_id,
        'dp': request.GET.get('utmp'),
        'dr': request.GET.get('utmr'),
    }
    headers = {
        'User-Agent': user_agent,
    }
    requests.post(settings.ENDPOINT_URL, payload_data, headers=headers)

    return set_cookie(response, client_id)
