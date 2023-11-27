import os
import shutil
import multiprocessing as mp
from pathlib import Path
import joblib
import numpy as np
import h52nc


pls_number = input('how many PLSs?')
run_name = input('base run name: ')



while True:
    server = input('Are you running in the server? y/n ')

    if server == 'y':
        main_path = '/home/amazonfaceme/biancarius/CAETE-DVM-alloc-allom/'

    if server == 'n'
        main_path = '/home/bianca/bianca/CAETE-DVM-alloc-allom/'

base_run = ''

attr_filename = f'pls_attrs-{pls_number}.csv'
run_path = f'{main_path}/outputs/{run_name}'
pls_path =