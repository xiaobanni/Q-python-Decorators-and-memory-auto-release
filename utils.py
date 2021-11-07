"""
@Project : code
@File    : utils
@Author  : XiaoBanni
@Date    : 2021-11-06 18:38
@Desc    : 
"""
import argparse
import os
import psutil


def count_memory(func):
    def start(*args, **kwargs):
        pid = os.getpid()
        p = psutil.Process(pid)
        info_start = p.memory_full_info().uss / 1024
        ret = func(*args, **kwargs)
        info_end = p.memory_full_info().uss / 1024
        print('the storage used for mining the rules is ' + str(info_end - info_start) + ' KB.')
        return ret

    return start


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--alg", help="choose algorithm", default="baseline",
                        choices=["baseline", "apriori", "fp-growth"], type=str)
    parser.add_argument("--dataset", help="choose dataset, 1: GroceryStore, 2: UNIX_usage", default=1, choices=[1, 2],
                        type=int)
    parser.add_argument("--support", help="P(A and B)", default=0.01, type=float)
    parser.add_argument("--confidence", help="P(B|A)", default=0.6, type=float)
    return parser.parse_args()
