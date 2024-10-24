#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import shutil
import time
import logging as log_use
import colorlog

from Initialize import Initialize
from Classification_module import run_classification
from threading import Thread
from log import get_logger

logging = get_logger(log_use.INFO)


def Thread_calls(process_src, process_number, confidence, body_cut):
    # 图片预处理开始
    Initialize(body_cut)

    # 将图片放置缓存文件夹用于线程分类处理
    new_file_path = ("Cache\\")
    list_ = os.listdir(process_src)
    num = int(float(len(list_)) / float(process_number))

    if int(len(list_) % num) == 0:
        num_file = int(len(list_) / num)
    else:
        num_file = int(len(list_) / num) + 1

    cnt = 0
    for n in range(1, num_file + 1):
        try:
            new_file = os.path.join(new_file_path + str(n))
            logging.info(f'Create a folder with the following folder name:{new_file}')
            os.mkdir(new_file)
            list_n = list_[num * cnt:num * (cnt + 1)]

            for m in list_n:
                old_path = os.path.join(process_src, m)
                new_path = os.path.join(new_file, m)
                shutil.copy(old_path, new_path)
            cnt += 1
        except Exception as error:
            logging.critical(error)

    for index in range(int(cnt)):
        _processes = (Thread(target=start_processes, args=(str(index + 1), confidence)))
        _processes.start()


# 开启线程处理文件
def start_processes(index, confidence):
    time1 = time.time()

    input_work_path = (f'Cache\\{index}')

    run_classification(input_work_path, confidence)

    time2 = time.time()
    logging.info(f"process{index}：The time spent on this thread{time2 - time1}s")
