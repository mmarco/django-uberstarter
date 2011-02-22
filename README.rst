Django UberStarter
=================

Django-uberstarter is an automated project starter that makes life easier for front-end developers. It combines the following apps/best practices to give you the most up-to-date Django setup possible:

**Back-end, environment stuff**
* python 2.6 - Easily changeable to whatever version you want (just edit bin/uberstart.sh)
* virtualenv_ - Isolate projects into a dedicated python environment so you can install things without breaking other projects.
* pip - Our favorite package installer
* django - 1.2.5 as of this release
* django-debug-toolbar_ - Makes debugging django a less painful experience. Use it.

**Front-end**
* django-css_ - A wonderful compressor that bundles all your static js/css into one file in order to minimize HTTP requests.
* CleverCSS_ - The pythonic tribute to ruby's SASS_, which lets you write indentation-based CSS in order to stay DRY. Needless to say, CSS compilers rock_.
* shpaml_ - The pythonic tribute to ruby's HAML_, which lets you write indentation-based HTML, so you can also stay DRY.
* HTML5boilerplate_ - By the wonderful wizards led by Paul Irish, it gets you an HTML5-ready markup with plenty of fallbacks for crappy/older browsers.
* 960.gs_ - Our favorite CSS framework. Period.
* jQuery - 1.5 as of this release
* Sample prototype page for quick_iterations_ - Thanks to the wonderful work of Stephen_Bau_ I use this extensively to get apps to "just work" at first, maybe you will like it too!


.. _virtualenv: http://www.arthurkoziel.com/2008/10/22/working-virtualenv/
.. _django-debug-toolbar: https://github.com/robhudson/django-debug-toolbar
.. _rock: http://blog.davidziegler.net/post/92203003/css-compilers-rock
.. _SASS: http://sass-lang.com/
.. _HAML: http://haml-lang.com/
.. _django-css: https://github.com/dziegler/django-css
.. _CleverCSS: http://github.com/dziegler/clevercss/tree/master 
.. _shpaml: http://shpaml.webfactional.com/
.. _HTML5boilerplate: http://html5boilerplate.com/
.. _960.gs: http://960.gs/
.. _quick_iterations: http://designinfluences.com/fluid960gs/
.. _Stephen_Bau: http://www.domain7.com/Team/StephenBau.html




Installation
************
* cd ALL THE WAY into /path/to/django-uberstarter/bin
* Get all the goodies setup (source uberstart.sh and wait for packages to get downloaded/installed )
* Initiate your project's virtualenv (source /path/to/django-uberstarter/env/bin/activate)
* Check out the prototype page! (python /path/to/django-uberstarter/myproject/manage.py runserver)


Usage
************
Naturally, calling your project "myproject" is a bit boring, so you will want to edit the following when you change its name to something else:

* Rename the folder inside django-uberstarter (ie. django-uberstarter/myproject/ to django-uberstarter/sweet-unicorns/)
* Change the ROOT_URLCONF variable in settings.py to reflect the new project's name (ie. ROOT_URLCONF = 'myproject.urls' to ROOT_URLCONF = 'sweet-unicorns.urls')