import os
import sys
from django.core.wsgi import get_wsgi_application

# Força o Python a encontrar a pasta core
path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if path not in sys.path:
    sys.path.insert(0, path)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

application = get_wsgi_application()
app = application # Variável que a Vercel procura



