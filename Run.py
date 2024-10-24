#!/usr/bin/env python
# -*- coding: utf-8 -*-
from Thread_scheduling import Thread_calls
from log import get_logger
import logging as log_use
import shutil
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-process_number', type=int, help='开启线程数', default=1)
parser.add_argument('-confidence', type=float, help='置信度', default=0.5)
parser.add_argument('-body_cut', type=bool, help='开启多人裁剪', default=False)
args = parser.parse_args()

logging = get_logger(log_use.INFO)
logging.info('Delete the folder')
if os.path.isdir('Categories'):
    shutil.rmtree('Categories')
if os.path.isdir('Cache'):
    shutil.rmtree('Cache')
if os.path.isdir('Face_cache'):
    shutil.rmtree('Face_cache')
if os.path.isdir('Body_cache'):
    shutil.rmtree('Body_cache')
logging.info('Build folder')
os.mkdir('Categories')
os.mkdir('Cache')
os.mkdir('Face_cache')
os.mkdir('Body_cache')

try:
    Thread_calls(process_src='Body_cache', process_number=args.process_number, confidence=args.confidence,
                 body_cut=args.body_cut)
except Exception as error:
    logging.critical(error)
