import settings
import os
from django.conf.urls.defaults import *

from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^project/', include('project.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^$', 'django.views.generic.simple.direct_to_template', {'template': 'base/demo.html'}),
)




urlpatterns += patterns('',
                        
    # Apache config will serve these from the static server.
    # These are used only in dev runsrever mode 
    (r'^files/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root':os.path.dirname(__file__) + "/files"}),

    # care of them. use only in dev runsrever mode 
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
          {'document_root':os.path.dirname(__file__) + "/static"}),  
          
)
