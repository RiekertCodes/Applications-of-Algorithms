import numpy as np
import matplotlib.pyplot as plt
import math
import time

def minimum_y_coordinate(cords):
    n = len(cords)
    m = 0
    for i in range(0, n):
        if cords[i][1] < cords[m][1] or (cords[i][0] < cords[m][0] and cords[i][1] == cords[m][1]):
            m = i
    return m

def sort_polar_angle(cords, cp):
    n = len(cords)
    n_list = []
    r = []
    cos_v = []
    for i in range(0, n):
        p = cords[i]
        p = [p[0] - cp[0], p[1] - cp[1]]
        r.append(i)
        nValue = math.sqrt(np.power(p[0],2) + np.power(p[1],2))
        n_list.append(nValue)
        if nValue == 0:
            cos_v.append(1)
        else:
            cos_v.append(p[0] / nValue)
    for i in range(0, n - 1):
        idx = i + 1
        while idx > 0:
            if cos_v[idx] > cos_v[idx - 1] or (
                    cos_v[idx] == cos_v[idx - 1]
                    and n_list[idx] > n_list[idx - 1]):
                temp = cos_v[idx]
                temp_rank = r[idx]
                temp_norm = n_list[idx]
                cos_v[idx] = cos_v[idx - 1]
                r[idx] = r[idx - 1]
                n_list[idx] = n_list[idx - 1]
                cos_v[idx - 1] = temp
                r[idx - 1] = temp_rank
                n_list[idx - 1] = temp_norm
                idx = idx - 1
            else:
                break
    sorted_points = []
    for i in r:
        sorted_points.append(cords[i])
    return sorted_points

def get_vect_angle(v):
    norm_ = math.sqrt(v[0] * v[0] + v[1] * v[1])
    if norm_ == 0:
        return 0
    angle = math.acos(v[0] / norm_)
    if v[1] >= 0:
        return angle
    else:
        return 2 * math.pi - angle

def coss_multi(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]





