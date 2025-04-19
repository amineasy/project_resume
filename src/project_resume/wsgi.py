import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project_resume.settings')

application = get_wsgi_application()
