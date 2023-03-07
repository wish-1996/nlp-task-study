#!/usr/bin/env python
# -*- coding:utf8 -*-
import os
import sys
import threading
import uuid
from flask import Response, json, request
from . import apis
# 到根目录
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../')))
from flask_apscheduler import APScheduler
# from core import Spider_main
from app_logging import get_logger
logger = get_logger()

scheduler = APScheduler()


# @scheduler.task('interval', id='do_job_1', minutes=75, misfire_grace_time=900)
# def job1():
#     print('Job 1 executed')
#     Spider_main.main()


# @scheduler.task('cron', id='do_job_2',day_of_week='*',hour=12,minute=30)
# # @scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
# def job1():
#     print('job1')
#     Spider_main.main()
#
#
# @scheduler.task('cron', id='do_job_2',day_of_week='*',hour=14,minute=30)
# # @scheduler.task('interval', id='do_job_1', seconds=30, misfire_grace_time=900)
# def job1():
#     print('job1')
#     Spider_main.main()
#
#
# @scheduler.task('cron', id='do_job_3',day_of_week='*',hour=20,minute=30)
# def job2():
#     print('job2')
#     Spider_main.main()