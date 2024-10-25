#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import logging as log_use
import colorlog

from tqdm import *
from shutil import copyfile
from log import get_logger
from Face_recognition import detect_similarity

logging = get_logger(log_use.INFO)


def run_classification(input_work_path, confidence, body_cut):

    files_list = os.listdir(input_work_path)
    for i in tqdm(range(len(files_list))):
        file_input = files_list[i]

        base_files_list = os.listdir('Recognize_faces')
        save_file_name = ''
        contrasting_values = 1000
        for h in range(len(base_files_list)):
            try:
                base_file_input = base_files_list[h]
                judgment = detect_similarity(f'Recognize_faces\\{base_file_input}', f'{input_work_path}\\{file_input}')
                if float(judgment) < float(contrasting_values):
                    contrasting_values = judgment
                    save_file_name = base_file_input
            except Exception as error:
                logging.critical(error)

        if float(contrasting_values) <= float(confidence * 100):
            logging.info(f"confidence: {contrasting_values}")
            save_file_name = save_file_name.split('.')[0]
            file_input = file_input.split('.')[0]
            file_input = file_input
            if body_cut:
                copyfile(f'Body_cache\\{file_input}.png', f'Categories\\target_{save_file_name}\\{file_input}.png')
            if not body_cut:
                copyfile(f'Categorize_pictures\\{file_input}.png', f'Categories\\target_{save_file_name}\\{file_input}.png')
        else:
            logging.info(
                f'The highest similarity does not meet expectations, and the image will not be classified. file:{save_file_name}')
