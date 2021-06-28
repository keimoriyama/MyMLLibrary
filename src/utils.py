import numpy as np
from tqdm import tqdm
import time

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
