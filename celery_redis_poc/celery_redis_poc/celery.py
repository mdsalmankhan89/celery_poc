from __future__ import absolute_import, unicode_literals

import os
import time
import shutil
import os
from celery import Celery
from datetime import datetime

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_redis_poc.settings')

app = Celery('celery_redis_poc')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print("in debug task")
    #print('Request: {0!r}'.format(self.request))

@app.task(bind=True)
def copy_file(self):
    #src = "C:\\Users\\salman\\Desktop\\LinkedIn Learning\\Python\\Ex_Files_Learning_Python_Upd\\Exercise Files\\source\\file.txt"
    #dest = "C:\\Users\\salman\\Desktop\\LinkedIn Learning\\Python\\Ex_Files_Learning_Python_Upd\\Exercise Files\\destination\\file.txt" 
    #dir = "fff"
    curDT = datetime.now()
    date_time = curDT.strftime("%m-%d-%Y %H_%M_%S")
    dest = "C:\\Users\\salman\\Desktop\\LinkedIn Learning\\Python\\Ex_Files_Learning_Python_Upd\\Exercise Files\\destination"
    path = os.path.join(dest, date_time)
    time.sleep(10);
    os.mkdir(path)
    #shutil.copyfile(src, dest)
    print("hello1")