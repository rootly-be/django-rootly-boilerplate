from .base import *

# Activer le mode débogage pour le développement
DEBUG = True

# Autoriser les hôtes locaux uniquement
ALLOWED_HOSTS = ['*']

# Configurer la base de données pour le développement (SQLite par exemple)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Configuration de l'email en mode console pour tester les emails en dev
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

