"""
ASGI 配置用于异步服务器。

它将 ASGI callable 暴露为名为 `application` 的模块级变量。
"""

import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Filem.settings')

application = get_asgi_application()
