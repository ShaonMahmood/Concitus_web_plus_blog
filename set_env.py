# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals

import os
import sys
# import logger_patch
import logging
#from logging.handlers import SysLogHandler

#CLEAN_DELAY = int(os.environ.get('CB_CLEAN_DELAY', 60))
#RSYSLOG_HOST = os.environ.get('CB_RSYSLOG_HOST', 'localhost')
#RSYSLOG_PORT = int(os.environ.get('CB_RSYSLOG_PORT', 514))
CALLBLADE_ROOT = os.path.join(os.path.dirname(os.path.abspath(__file__)), '')
print(CALLBLADE_ROOT)
PACKAGE_DIR = os.path.join(CALLBLADE_ROOT, 'concitusP')
print(PACKAGE_DIR)


def execfile(path, global_vars=None, local_vars=None):
    with open(path, 'r') as f:
        code = compile(f.read(), path, 'exec')
        exec(code, global_vars, local_vars)

"""def get_logger(name='callblade-autorecharge', debug=True):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG if debug else logging.WARNING)
    ch = SysLogHandler(address=(RSYSLOG_HOST, RSYSLOG_PORT))
    ch.setLevel(logging.DEBUG if debug else logging.WARNING)
    formatter = logging.Formatter('%(hostname)s %(name)s - %(levelname)s: %(message)s')
    ch.setFormatter(formatter)
    logger.addHandler(ch)
    return logger"""


def activate_venv():

    VENV = os.path.join(CALLBLADE_ROOT, 'env_con')

    if os.path.isfile(os.path.join(VENV, 'bin/activate_this.py')):
        #activate_this = 

        #print(activate_this)
        #exec(str(open(activate_this)))
        execfile(os.path.join(VENV, 'bin/activate_this.py'), dict(__file__=os.path.join(VENV, 'bin/activate_this.py')))
        #print(sys.path.extend([CALLBLADE_ROOT, PACKAGE_DIR]))

    import django

    sys.path.extend([CALLBLADE_ROOT,PACKAGE_DIR])
    print(sys.path.extend([CALLBLADE_ROOT,PACKAGE_DIR]))
    os.environ["DJANGO_SETTINGS_MODULE"] = "concitusP.settings"
    django.setup()



