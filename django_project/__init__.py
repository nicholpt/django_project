# import celery
from .celery import app as celery_app

#importing celery in __init___ so it initiates from the beginning