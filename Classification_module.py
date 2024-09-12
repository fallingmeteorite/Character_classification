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


def run_classification(input_work_path, Confidence):
    files_list = os.listdir(input_work_path)
    for i in tqdm(range(len(files_list))):
        file_input = files_list[i]

        base_files_list = os.listdir('Recognize_faces')
        save_file_name = ''
        contrasting_values = 0
        for h in range(len(base_files_list)):
            base_file_input = base_files_list[h]
            judgment = detect_similarity(f'Recognize_faces\\{base_file_input}', f'{input_work_path}\\{file_input}')
            if float(judgment) < float(contrasting_values):
                contrasting_values = judgment
                save_file_name = base_file_input

        if float(contrasting_values) >= float(Confidence):
            save_file_name = save_file_name.split('.')[0]
            file_input = file_input.split('.')[0]
            file_input = file_input
            copyfile(f'Body_cache\\{file_input}.png', f'Categories\\target_{save_file_name}\\{file_input}.png')

