
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# SECURITY SETTINGS
# ==========================================

# Keep your existing SECRET_KEY here
SECRET_KEY = 'replace-with-your-existing-secret-key'

DEBUG = True

ALLOWED_HOSTS = [
    '127.0.0.1',
    'localhost',
]


# ==========================================
# INSTALLED APPLICATIONS
# ==========================================

INSTALLED_APPS = [
    'jazzmin',

    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Add your own Django apps here
]


# ==========================================
# JAZZMIN ADMIN CONFIGURATION
# ==========================================

JAZZMIN_SETTINGS = {
    "site_title": "Flipkart Admin",
    "site_header": "Flipkart",
    "site_brand": "Flipkart Dashboard",
    "welcome_sign": "Welcome to Flipkart Admin Portal",
    "copyright": "Flipkart Management System",

    "search_model": [
        "auth.User",
    ],

    "show_sidebar": True,
    "navigation_expanded": True,
    "show_ui_builder": True,

    "topmenu_links": [
        {
            "name": "Home",
            "url": "admin:index",
            "permissions": ["auth.view_user"],
        },
        {
            "name": "View Website",
            "url": "/",
            "new_window": True,
        },
    ],

    "usermenu_links": [
        {
            "name": "Website",
            "url": "/",
            "new_window": True,
        },
    ],

    "order_with_respect_to": [
        "auth",
    ],

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user",
        "auth.group": "fas fa-users",
        "sites": "fas fa-globe",
    },

    "default_icon_parents": "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    "related_modal_active": True,
    "use_google_fonts_cdn": True,
    "show_language_chooser": True,
}


# ==========================================
# JAZZMIN UI DESIGN / THEME
# ==========================================

JAZZMIN_UI_TWEAKS = {
    "theme": "cosmo",
    "dark_mode_theme": "darkly",

    "navbar": "navbar-dark",
    "navbar_fixed": True,
    "navbar_small_text": False,

    "brand_colour": "navbar-primary",
    "accent": "accent-primary",

    "sidebar": "sidebar-dark-primary",
    "sidebar_fixed": True,
    "sidebar_nav_small_text": False,

    "sidebar_nav_legacy_style": True,
    "sidebar_nav_flat_style": True,
    "sidebar_nav_compact_style": False,

    "footer_fixed": False,
    "body_small_text": False,

    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-secondary",
        "success": "btn-success",
        "danger": "btn-danger",
        "warning": "btn-warning",
        "info": "btn-info",
    },
}


# ==========================================
# MIDDLEWARE
# ==========================================

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ==========================================
# URL CONFIGURATION
# ==========================================

ROOT_URLCONF = 'customer.urls'


# ==========================================
# TEMPLATE CONFIGURATION
# ==========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==========================================
# WSGI / ASGI CONFIGURATION
# ==========================================

WSGI_APPLICATION = 'customer.wsgi.application'
ASGI_APPLICATION = 'customer.asgi.application'


# ==========================================
# DATABASE CONFIGURATION
# ==========================================

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ==========================================
# PASSWORD VALIDATION
# ==========================================

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# ==========================================
# LANGUAGE AND TIME
# ==========================================

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# ==========================================
# STATIC FILES
# ==========================================

STATIC_URL = 'static/'

STATIC_ROOT = BASE_DIR / 'staticfiles'

STATICFILES_DIRS = [
    BASE_DIR / 'static',
]


# ==========================================
# DEFAULT PRIMARY KEY
# ==========================================

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


