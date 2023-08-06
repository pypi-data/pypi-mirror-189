import os
import sys
import logging
import logging.config
import re
from os.path import dirname
from logging.handlers import RotatingFileHandler


cur_dir = os.path.split(os.path.realpath(__file__))[0]
LOG_DIR = os.environ['LOG_DIR'] if 'LOG_DIR' in os.environ \
    and os.environ['LOG_DIR'] else os.path.join(cur_dir, "log/")
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

LEVEL = os.environ['LOG_LEVEL'] if 'LOG_LEVEL' in os.environ \
    and os.environ['LOG_LEVEL'] else "INFO"

LOG_CONFIG = {
    'version': 1, 
    'disable_existing_loggers': False, 
    'formatters': {
        'simple': {
            'format': '%(asctime)s - %(message)s'
        },
        'standard': {
            'format': '%(asctime)s \"%(pathname)s:%(lineno)d\" [%(levelname)s]- %(message)s'
        }
    }, 
    'handlers': {
        'stream_logger': {
            'level': 'DEBUG', 
            'formatter': 'simple', 
            'class': 'logging.StreamHandler',
            'stream': 'ext://sys.stdout'
        }, 

        'one_day_logger': {
            'level': 'DEBUG', 
            'formatter': 'standard', 
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'filename': os.path.join(LOG_DIR, 'wenxin_api.log'), 
            'when': 'midnight', 
            'interval': 1, 
            'encoding': 'utf-8', 
        }, 
        'half_gb_logger': {
            'level': "DEBUG",
            'formatter': 'standard', 
            'class': 'logging.handlers.RotatingFileHandler', 
            'filename': os.path.join(LOG_DIR, 'wenxin_api.log'),
            'maxBytes': 1024 * 1024 * 500, 
            # https://stackoverflow.com/questions/40150821/in-the-logging-modules-rotatingfilehandler-how-to-set-the-backupcount-to-a-pra
            # clean your logs 
            # after it grows to 500G(maxBytes * backupCount)
            # RotatingFileHandler won't do rotate anymore
            'backupCount': 1000, 
            'encoding': 'utf-8', 
        }
    }, 
    'loggers': {
         'wenxin_api': {
            'handlers': ['stream_logger', 'one_day_logger', 'half_gb_logger'], 
            # FIXME 
            'level': LEVEL, 
            'propagate': True, 
         }
    }
}

logging.config.dictConfig(LOG_CONFIG)

def get_logger(name=None):
    """ get logger """
    if name is None:
        name = "wenxin_api"
    logger = logging.getLogger(name)
    return logger
