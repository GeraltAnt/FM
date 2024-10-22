"""
WSGI 配置用于部署项目。

它将 WSGI callable 暴露为名为 `application` 的模块级变量。
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Filem.settings')

application = get_wsgi_application()
