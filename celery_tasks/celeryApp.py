# 使用celery
from django.conf import settings
from celery import Celery
import time

# 在任务处理者一端加这几句
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dailyfresh.settings")
django.setup()

# 创建一个Celery类的实例对象
app = Celery(main='celery_app', broker='redis://192.168.3.94:6379/8')
app.autodiscover_tasks(settings.INSTALLED_APPS) # 参数为task.py所在包
