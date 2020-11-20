from .settings import *


DEBUG = False

ALLOWED_HOSTS = ['soil7800.pythonanywhere.com']

STATIC_URL =  '/static/'
STATIC_ROOT =  os.path.join(BASE_DIR, 'static')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

