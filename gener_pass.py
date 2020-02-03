# -*- coding: utf-8 -*-
#!/usr/bin/env python

import random

from data import *


def range_symbols():
    Pass = ""
    PassA = ""
    for key, value in symbol_dict.items():
        for i in range(key):
            n = random.randrange(len(value))
            Pass += value[n]
    PassA = list(Pass)
    return PassA


def ready_pass(new_list):
    random.shuffle(new_list)
    PassEnd = ""
    for i in range(len(new_list)):
        PassEnd += new_list[i]
    return PassEnd


def main():
    PassA = range_symbols()
    return ready_pass(PassA)


if __name__ == '__main__':
    count_res = count_bs + count_ls + count_ns + count_ss
    pass_result = main()
    print(f'Your password: {pass_result} with {count_res} symbols')
