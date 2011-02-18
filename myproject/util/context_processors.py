"""
    Common context exposes relevant settings to templates
    
"""
import random
import datetime

from django.conf import settings as dj_settings
from django.db import connection
from django.contrib.auth.models import SiteProfileNotAvailable
from django.core.exceptions import ObjectDoesNotExist

def common(request):
    """
    Insert common items
    """
    import settings, local_settings

    context_extras = {

        'MEDIA_URL': settings.MEDIA_URL,
        'DEBUG' :settings.DEBUG,

        }
    return context_extras

