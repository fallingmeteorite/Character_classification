#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import shutil
import colorlog
import cv2

from PIL import Image
from pathlib import Path
from shutil import copyfile
from tqdm import *
from imgutils.detect import detect_faces, detection_visualize, detect_person
import logging as log_use
from log import get_logger

logging = get_logger(log_use.INFO)


# 传入是否开启该功能参数
def Initialize(body_cut):
    # 重新命名对比图片名称
    files_list = os.listdir('Recognize_faces')
    for i in tqdm(range(len(files_list))):
        try:
            file_input = files_list[i]
            formatted_number = "{:02d}".format(i)
            os.rename(f'Recognize_faces\\{file_input}', f'Recognize_faces\\{formatted_number}.png')

            # 分类对比人脸到各个文件夹
            os.mkdir(f'Categories\\target_{formatted_number}')
            copyfile(f'Recognize_faces\\{formatted_number}.png', f'Categories\\target_{formatted_number}\\{formatted_number}.png')
            logging.info(f'Categories\\target_{formatted_number} |The folder has been created')

        except Exception as error:
            logging.critical(error)


    # 开启则对多人图片进行处理，关闭则不会处理
    if body_cut:
        logging.info('Start dividing the characters...')
        files_list = os.listdir('Categorize_pictures')
        for i in tqdm(range(len(files_list))):
            try:
                file_input = files_list[i]
                img = cv2.imread(f'Categorize_pictures\\{file_input}')
                result = detect_person(f'Categorize_pictures\\{file_input}', iou_threshold=0.4)
                for h in range(len(result)):
                    coordinate_list = (result[h])[0]
                    save_img = img[int(coordinate_list[1]):int(coordinate_list[3]),
                               int(coordinate_list[0]):int(coordinate_list[2])]
                    formatted_number = "{:02d}".format(h)
                    file_input = file_input.split('.')[0]
                    cv2.imwrite(f'Body_cache\\{file_input}_{formatted_number}.png', save_img)
            except Exception as error:
                logging.critical(error)
        logging.info('The split is complete')

        # 对图片进行人脸截取，准备开始分类
        logging.info('Begin to recognize the face of the picture...')
        files_list = os.listdir('Body_cache')
        for i in tqdm(range(len(files_list))):
            try:
                file_input = files_list[i]
                img = cv2.imread(f'Body_cache\\{file_input}')
                result = detect_faces(f'Body_cache\\{file_input}', iou_threshold=0.4)
                for h in range(len(result)):
                    coordinate_list = (result[h])[0]
                    save_img = img[int(coordinate_list[1]):int(coordinate_list[3]),
                               int(coordinate_list[0]):int(coordinate_list[2])]
                    formatted_number = "{:02d}".format(h)
                    file_input = file_input.split('.')[0]
                    cv2.imwrite(f'Face_cache\\{file_input}_{formatted_number}.png', save_img)
            except Exception as error:
                logging.critical(error)

        logging.info('All pictures of the face are acquired')
    else:

        # 对图片进行人脸截取，准备开始分类
        logging.info('Begin to recognize the face of the picture...')
        files_list = os.listdir('Categorize_pictures')
        for i in tqdm(range(len(files_list))):
            try:
                file_input = files_list[i]
                img = cv2.imread(f'Categorize_pictures\\{file_input}')
                result = detect_faces(f'Categorize_pictures\\{file_input}', iou_threshold=0.4)
                for h in range(len(result)):
                    coordinate_list = (result[h])[0]
                    save_img = img[int(coordinate_list[1]):int(coordinate_list[3]),
                               int(coordinate_list[0]):int(coordinate_list[2])]
                    formatted_number = "{:02d}".format(h)
                    file_input = file_input.split('.')[0]
                    cv2.imwrite(f'Face_cache\\{file_input}_{formatted_number}.png', save_img)
            except Exception as error:
                logging.critical(error)

        logging.info('All pictures of the face are acquired')
