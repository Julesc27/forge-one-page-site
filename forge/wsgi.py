"""
WSGI config for forge project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os
import sys
sys.path.append('/var/www/forge_django')
sys.path.append('/var/www/forge/forge_django')

from django.core.wsgi import get_wsgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'forge.settings')
os.environ.setdefault('GOOGLE_API_KEY', 'AIzaSyD1me8o2Z-3GgEp0tVp2F2ZQMsOoM5vlXw')
os.environ.setdefault('SENDGRID_API_KEY', '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')
os.environ.setdefault('SITE_URL', 'www.rpiforge.dev')
application = get_wsgi_application()
