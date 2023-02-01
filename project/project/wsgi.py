# -*- coding: utf-8 -*-

import os
import sys
import platform

#путь к проекту
sys.path.insert(0, '/home/k/kritohanzo/newsite/public_html/project')
#путь к фреймворку
sys.path.insert(0, '/home/k/kritohanzo/newsite/public_html/project/project')
#путь к виртуальному окружению
sys.path.insert(0, '/home/k/kritohanzo/newsite/venv/lib/python{0}/site-packages'.format(platform.python_version()[0:3]))
os.environ["DJANGO_SETTINGS_MODULE"] = "project.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()