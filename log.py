#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging as log_use
import colorlog


def get_logger(level=log_use.DEBUG):
    # 创建logger对象
    logger = log_use.getLogger()
    logger.setLevel(level)
    # 创建控制台日志处理器
    console_handler = log_use.StreamHandler()
    console_handler.setLevel(level)
    # 定义颜色输出格式
    color_formatter = colorlog.ColoredFormatter(
        '%(log_color)s | %(asctime)s | %(levelname)s : %(message)s',
        log_colors={
            'DEBUG': 'white',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red,bg_yellow',
            'CRITICAL': 'red,bg_yellow',
        }
    )
    # 将颜色输出格式添加到控制台日志处理器
    console_handler.setFormatter(color_formatter)
    # 移除默认的handler
    for handler in logger.handlers:
        logger.removeHandler(handler)
    # 将控制台日志处理器添加到logger对象
    logger.addHandler(console_handler)
    return logger
