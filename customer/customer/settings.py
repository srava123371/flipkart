
from pathlib import Path
import os

# ==========================================
# BASE DIRECTORY
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent


# ==========================================
# SECURITY SETTINGS
# ==========================================

SECRET_KEY = 'django-insecure-change-this-for-production'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


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
]


# ==========================================
# JAZZMIN ADMIN CONFIGURATION
# ==========================================

JAZZMIN_SETTINGS = {
    "site_title": "Flipkart Admin",
    "site_header": "FLIPKART",
    "site_brand": "FLIPKART",
    "welcome_sign": "Welcome to Flipkart Admin Portal",
    "copyright": "Flipkart | Admin Dashboard",

    "show_sidebar": True,
    "navigation_expanded": True,
    "show_ui_builder": True,
    "show_search": True,
    "show_footer": True,

    "theme": "darkly",
    "dark_mode_theme": "darkly",

    "custom_css": "admin/admin_cinematic.css",

    "icons": {
        "auth": "fas fa-users-cog",
        "auth.user": "fas fa-user-circle",
        "auth.Group": "fas fa-users",
    },

    "order_with_respect_to": [
        "auth",
    ],

    "topmenu_links": [
        {
            "name": "Home",
            "url": "admin:index",
        },
        {
            "model": "auth.User",
        },
    ],

    "related_modal_active": True,
    "show_language_selector": False,
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
# TEMPLATES
# ==========================================

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,

        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ==========================================
# WSGI AND ASGI
# ==========================================

WSGI_APPLICATION = 'customer.wsgi.application'

ASGI_APPLICATION = 'customer.asgi.application'


# ==========================================
# DATABASE
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
# STATIC FILE CONFIGURATION
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


# ==========================================
# CINEMATIC GLASSMORPHISM CSS
# ==========================================

CINEMATIC_CSS = """

/* GLOBAL BACKGROUND */

body {
    background:
        radial-gradient(circle at 10% 10%, #243b65 0%, transparent 40%),
        radial-gradient(circle at 90% 90%, #512b58 0%, transparent 40%),
        linear-gradient(135deg, #080d1b, #111827) !important;

    background-attachment: fixed !important;
    color: #ffffff !important;
}

/* MAIN CONTENT */

.content-wrapper {
    background: transparent !important;
}

/* NAVBAR GLASS EFFECT */

.main-header {
    background: rgba(15, 23, 42, 0.55) !important;
    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    border-bottom: 1px solid rgba(255,255,255,0.15);
}

/* SIDEBAR GLASS EFFECT */

.main-sidebar {
    background: rgba(15, 23, 42, 0.70) !important;

    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    border-right: 1px solid rgba(255,255,255,0.15);

    box-shadow: 0 0 35px rgba(0,0,0,0.3);
}

/* BRAND LOGO AREA */

.brand-link {
    background: rgba(255,255,255,0.06) !important;
    border-bottom: 1px solid rgba(255,255,255,0.12) !important;
}

.brand-text {
    color: #38bdf8 !important;
    font-weight: bold;
    letter-spacing: 2px;
}

/* GLASS CARDS */

.card,
.info-box,
.small-box {
    background: rgba(255,255,255,0.08) !important;

    backdrop-filter: blur(22px);
    -webkit-backdrop-filter: blur(22px);

    border: 1px solid rgba(255,255,255,0.15) !important;

    border-radius: 18px !important;

    box-shadow: 0 8px 35px rgba(0,0,0,0.25);

    color: white !important;

    transition: all 0.3s ease;
}

/* CARD HOVER */

.card:hover,
.info-box:hover,
.small-box:hover {
    transform: translateY(-4px);

    border-color: rgba(0,212,255,0.5) !important;

    box-shadow: 0 12px 40px rgba(0,212,255,0.15);
}

/* CARD HEADER */

.card-header {
    background: rgba(255,255,255,0.07) !important;

    border-bottom: 1px solid rgba(255,255,255,0.12) !important;

    color: white !important;
}

/* TEXT COLORS */

h1, h2, h3, h4, h5, h6,
p, label, .nav-link, .brand-text {
    color: #f1f5f9 !important;
}

/* TABLE DESIGN */

.table,
.table td,
.table th {
    background: transparent !important;

    color: #ffffff !important;

    border-color: rgba(255,255,255,0.12) !important;
}

.table tbody tr:hover {
    background: rgba(0,212,255,0.08) !important;
}

/* INPUT FIELDS */

input,
select,
textarea,
.form-control {
    background: rgba(255,255,255,0.08) !important;

    color: white !important;

    border: 1px solid rgba(255,255,255,0.2) !important;

    border-radius: 10px !important;
}

input:focus,
select:focus,
textarea:focus {
    border-color: #00d4ff !important;

    box-shadow: 0 0 12px rgba(0,212,255,0.25) !important;
}

/* BUTTONS */

.btn-primary {
    background: linear-gradient(135deg, #00c6ff, #0072ff) !important;

    border: none !important;

    border-radius: 10px !important;

    box-shadow: 0 5px 20px rgba(0,114,255,0.25);
}

.btn-success {
    background: linear-gradient(135deg, #00d68f, #00a86b) !important;

    border: none !important;

    border-radius: 10px !important;
}

/* SIDEBAR ACTIVE MENU */

.nav-sidebar .nav-link.active {
    background: linear-gradient(
        135deg,
        rgba(0,198,255,0.3),
        rgba(0,114,255,0.3)
    ) !important;

    border: 1px solid rgba(0,198,255,0.35);

    border-radius: 10px !important;
}

/* LINKS */

a {
    color: #38bdf8;
}

/* LOGIN PAGE */

.login-box .card {
    background: rgba(255,255,255,0.09) !important;

    backdrop-filter: blur(25px);
    -webkit-backdrop-filter: blur(25px);

    border: 1px solid rgba(255,255,255,0.2) !important;

    border-radius: 22px !important;
}

/* FOOTER */

.main-footer {
    background: rgba(255,255,255,0.04) !important;

    border-top: 1px solid rgba(255,255,255,0.1);

    color: #cbd5e1 !important;
}

/* SCROLLBAR */

::-webkit-scrollbar {
    width: 7px;
}

::-webkit-scrollbar-thumb {
    background: linear-gradient(#00c6ff, #0072ff);

    border-radius: 10px;
}

/* SMOOTH ANIMATIONS */

* {
    transition-duration: 0.25s;
}

"""


# ==========================================
# AUTOMATIC CSS FILE CREATION
# ==========================================

CSS_DIR = BASE_DIR / 'static' / 'admin'

os.makedirs(CSS_DIR, exist_ok=True)

CSS_FILE = CSS_DIR / 'admin_cinematic.css'

with open(CSS_FILE, 'w', encoding='utf-8') as file:
    file.write(CINEMATIC_CSS)

