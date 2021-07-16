"""
Configuration settings for the iAHO data capture tool (DCT) developed for AFRO.
"""
from django.utils.translation import ugettext_lazy as _
import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jz&%c@07o%z_mo&qs2t@-io)vm5ul_0j*kwm@#&m0m4nf7j5a^'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['localhost','af-aho-datacapturetool.azurewebsites.net']


# Application definition
INSTALLED_APPS = [
    'admin_menu',
    'admin_reorder',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'parler', #language translation package
    'smart_selects',
	'import_export',
    'authentication',
    'home',
    'indicators',
    'elements',
    'publications',
    'regions',
    'facilities',
    'health_workforce',
    'data_wizard',
    'data_wizard.sources',
    'rest_framework', # register Django
    'rest_framework_swagger',
    'django_admin_listfilter_dropdown',
]

DATA_WIZARD = {
    'BACKEND': 'data_wizard.backends.threading',
    'LOADER': 'data_wizard.loaders.FileLoader',
    'PERMISSION': 'rest_framework.permissions.IsAdminUser',
}

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
        'rest_framework.parsers.FileUploadParser',

    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'rest_framework.filters.OrderingFilter',
    ],
    'DEFAULT_THROTTLE_CLASSES': [
        'rest_framework.throttling.UserRateThrottle',
        'rest_framework.throttling.AnonRateThrottle'
    ],
    'DEFAULT_THROTTLE_RATES': {
        'user': '10000/day',
        'anon': '10000/day'
    },
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.LimitOffsetPagination',
    'PAGE_SIZE': 50,
    'DATETIME_FORMAT': 'iso-8601',
    'DATE_FORMAT': 'iso-8601',
    'TIME_FORMAT': 'iso-8601',
}

MIDDLEWARE = [
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware', # added
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'admin_reorder.middleware.ModelAdminReorder', # added
]

ROOT_URLCONF = 'aho_datacapturetool.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # 'django.template.context_processors.media',
            ],
        },
    },
]

WSGI_APPLICATION = 'aho_datacapturetool.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'aho_stage_database', #temporary
		'HOST': 'localhost',
		'USER': 'ahodbadmin',
		'PASSWORD': 'Aho@1234',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
            'ssl': {'ca': '/site/cert/BaltimoreCyberTrustRoot.crt.pem'}
            },
    }
}

# custom user authentication and Password validation settings
AUTH_USER_MODEL = 'authentication.CustomUser'

# Password validation
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


# Internationalization
LANGUAGE_CODE ='en'

LANGUAGES = ( #added
('en',_('English')),
('fr', _('French')),
('pt',_('Portuguese')),
)

PARLER_LANGUAGES = {
None: (
{'code': 'en'},
{'code': 'fr'},
{'code': 'pt'},
),
'default': {
# Changed to fallbacks to fill missing list_display name in change form 15/10/2020
'fallbacks': ['fr','pt','en'],
'hide_untranslated': False, #show default as English
}
}

TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_URL = '/static/'

LOCALE_PATHS = (os.path.join(BASE_DIR, 'locale/'), # for UI language translations
)
# Base url to serve media files

# Set the diretory a path outside the project folder
MEDIA_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../..")
)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(MEDIA_DIR, 'repository') # directory where media is stored

#display the AHO logo on the login screen and admin page
ADMIN_LOGO = 'dashboard_logo.png'
LOGOUT_REDIRECT_URL='/'

ADMIN_STYLE = {
    'background': 'white',
    'primary-color': '#205280',
    'primary-text': '#d6d5d2',
    'secondary-color': '#3B75AD',
    'secondary-text': 'white',
    'tertiary-color': '#F2F9FC',
    'tertiary-text': 'black',
    'breadcrumb-color': 'whitesmoke',
    'breadcrumb-text': 'black',
    'focus-color': '#eaeaea',
    'focus-text': '#666',
    'primary-button': '#26904A',
    'primary-button-text':' white',
    'secondary-button': '#999',
    'secondary-button-text': 'white',
    'link-color': '#333',
    'link-color-hover': 'lighten($link-color, 20%)',
    'logo-width': 'auto',
    'logo-height': '35px'
}


ADMIN_REORDER = (
    # Cross-linked models
    {'app': 'home', 'models': ('home.StgDatasource','home.StgCategoryoption',
    'home.StgCategoryParent','home.StgMeasuremethod','home.StgValueDatatype')},

    {'app': 'indicators', 'models': ('indicators.FactDataIndicator',
    'indicators.IndicatorProxy','indicators.StgIndicator','indicators.StgIndicatorDomain',
    'indicators.StgIndicatorReference','indicators.aho_factsindicator_archive',
    'indicators.StgIndicatorNarrative','indicators.StgAnalyticsNarrative',
    'indicators.StgNarrative_Type','indicators.AhoDoamain_Lookup',)},

    {'app': 'publications', 'models': ('publications.StgKnowledgeProduct',
    'publications.StgProductDomain','publications.StgResourceCategory',
    'publications.StgResourceType')},

    {'app': 'facilities', 'models': ('facilities.StgHealthFacility',
    'facilities.StgFacilityType','facilities.StgFacilityOwnership',
    'facilities.StgFacilityInfrastructure','facilities.StgServiceDomain')},

    {'app': 'health_workforce', 'models': ('health_workforce.StgHealthWorkforceFacts',
    'health_workforce.StgHealthCadre','health_workforce.StgTrainingInstitution',
    'health_workforce.StgInstitutionType','health_workforce.StgInstitutionProgrammes',
    'health_workforce.StgAnnouncements','health_workforce.StgRecurringEvent',
    'health_workforce.ResourceTypeProxy','health_workforce.HumanWorkforceResourceProxy')},

    {'app': 'elements', 'models': ('elements.FactDataElement','elements.DataElementProxy',
    'elements.StgDataElement','elements.StgDataElementGroup')},

    {'app': 'regions', 'models': ('regions.StgLocation','regions.StgLocationLevel',
    'regions.StgEconomicZones','regions.StgWorldbankIncomegroups',
    'regions.StgSpecialcategorization')},

)
