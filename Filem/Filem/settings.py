"""
Django 项目的设置文件。

更多信息请参阅
https://docs.djangoproject.com/en/4.2/topics/settings/

完整的设置和其值请参阅
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path

# 构建项目的基本路径
BASE_DIR = Path(__file__).resolve(strict=True).parent.parent

SECRET_KEY = 'your_secret_key_here'


# 调试模式（生产环境中应设为 False）
DEBUG = True

ALLOWED_HOSTS = []

# 应用程序定义
INSTALLED_APPS = [
    'api',
    'rest_framework',
    'corsheaders',
    'filemanager',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',

    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_ALLOW_ALL = True
CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_HEADERS = ('*')
ROOT_URLCONF = 'Filem.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 全局模板目录
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                # 上下文处理器
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'Filem.wsgi.application'

# 数据库配置（使用 SQLite3）
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 密码验证
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
]

# 国际化
LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_TZ = True

# 静态文件（CSS、JavaScript、Images）
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'filemanager', 'static')]

# 媒体文件（上传的文件）
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# 默认主键字段类型
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',  # 允许任何人访问
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        # 移除 TokenAuthentication
    ],
}
