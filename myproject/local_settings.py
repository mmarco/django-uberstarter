import os
DEBUG = True

MEDIA_ROOT = os.path.dirname(__file__) +'/media/'
MEDIA_URL = '/media/'

TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.dirname(__file__) + "/templates",
)
