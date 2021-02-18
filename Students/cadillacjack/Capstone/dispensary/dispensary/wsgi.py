"""
WSGI config for dispensary project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dispensary.settings')
project_folder = os.path.expanduser('dispensary')
load_dotenv(os.path.join(project_folder, '.env'))

application = get_wsgi_application()
