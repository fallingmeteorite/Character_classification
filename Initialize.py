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


def Initialize():
    files_list = os.listdir('Recognize_faces')
    for i in tqdm(range(len(files_list))):
        file_input = files_list[i]
        formatted_number = "{:02d}".format(i)
        if not file_input == f'{formatted_number}.png':
            os.rename(f'Recognize_faces\\{file_input}', f'Recognize_faces\\{formatted_number}.png')

    files_list = os.listdir('Recognize_faces')
    for i in tqdm(range(len(files_list))):
        file_input = files_list[i]
        formatted_number = "{:02d}".format(i)
        os.mkdir(f'Categories\\target_{formatted_number}')
        copyfile(f'Recognize_faces\\{file_input}', f'Categories\\target_{formatted_number}\\{file_input}')
        logging.info(f'Categories\\target_{formatted_number}|The folder has been created')

    logging.info('Start dividing the characters...')
    files_list = os.listdir('Categorize_pictures')
    for i in tqdm(range(len(files_list))):
        file_input = files_list[i]
        img = cv2.imread(f'Categorize_pictures\\{file_input}')
        result = detect_person(f'Categorize_pictures\\{file_input}', iou_threshold = 0.4, max_infer_size = 896)
        for h in range(len(result)):
            coordinate_list = (result[h])[0]
            save_img = img[int(coordinate_list[1]):int(coordinate_list[3]),
                       int(coordinate_list[0]):int(coordinate_list[2])]
            formatted_number = "{:02d}".format(h)
            file_input = file_input.split('.')[0]
            cv2.imwrite(f'Body_cache\\{file_input}_{formatted_number}.png', save_img)

    logging.info('The split is complete')

    logging.info('Begin to recognize the face of the picture...')
    files_list = os.listdir('Body_cache')
    for i in tqdm(range(len(files_list))):
        file_input = files_list[i]
        img = cv2.imread(f'Body_cache\\{file_input}')
        result = detect_faces(f'Body_cache\\{file_input}', iou_threshold = 0.4, max_infer_size = 896)
        for h in range(len(result)):
            coordinate_list = (result[h])[0]
            save_img = img[int(coordinate_list[1]):int(coordinate_list[3]),
                       int(coordinate_list[0]):int(coordinate_list[2])]
            formatted_number = "{:02d}".format(h)
            file_input = file_input.split('.')[0]
            cv2.imwrite(f'Face_cache\\{file_input}_{formatted_number}.png', save_img)

    logging.info('All pictures of the face are acquired')
