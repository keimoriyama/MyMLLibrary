import numpy as np
from tqdm import tqdm
import time
import os

import torch

def get_elapsed_time(start, end):
    t = end-start
    h,m,s = 0, 0, 0
    if t >= 3600:
        h = int(t / 3600)
        t = t - h * 3600
    if t >= 60:
        m = int(t / 60)
        t = t - m * 60
    if t >= 0:
        s = t
    return [h, m, s]

def get_env():
    env = ""
    os_env = set(os.environ.keys())
    if 'COLAB_GPU' in os_env:
        env = 'colab'
    elif 'KAGGLE_URL_BASE' in os_env:
        env = 'kaggle'
    else:
        env = 'local'

    return env
