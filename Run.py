#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Thread_scheduling import Thread_calls
from log import get_logger
import logging as log_use
import shutil
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-process_number', type=int, help='Number of threads enabled', default=1)
parser.add_argument('-confidence', type=float, help='Confidence', default=0.5)
parser.add_argument('-body_cut', type=bool, help='Turn on multi-person cropping', default=False)

args = parser.parse_args()

logging = get_logger(log_use.INFO)
logging.info('Delete the folder')

# 判断文件夹是否存在并删除缓存文件夹
if os.path.isdir('Categories'):
    shutil.rmtree('Categories')
if os.path.isdir('Cache'):
    shutil.rmtree('Cache')
if os.path.isdir('Face_cache'):
    shutil.rmtree('Face_cache')
if os.path.isdir('Body_cache'):
    shutil.rmtree('Body_cache')

# 重新建立文件夹
logging.info('Build folder')
os.mkdir('Categories')
os.mkdir('Cache')
os.mkdir('Face_cache')
os.mkdir('Body_cache')

try:
    if args.body_cut:
        Thread_calls(process_src='Body_cache', process_number=args.process_number, confidence=args.confidence,
                     body_cut=args.body_cut)

    if not args.body_cut:
        Thread_calls(process_src='Categorize_pictures', process_number=args.process_number, confidence=args.confidence,
                     body_cut=args.body_cut)

except Exception as error:
    logging.critical(error)
