#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random


def range_symbols(count_up_case, count_low_case, count_numbers, count_special_char):
    pass_simple = ""
    symbol_dict = {
        count_up_case: tuple('QWERTYUPASDFGHJKLZXCVBNM'),
        count_low_case: tuple('qwertyuiopasdfghjklzxcvbnm'),
        count_numbers: tuple('1234567890'),
        count_special_char: tuple('!@#$%&;:<>?/*()'),
    }
    for key, value in symbol_dict.items():
        for i in range(key):
            n = random.randrange(len(value))
            pass_simple += value[n]
    pass_simple_res = list(pass_simple)
    return pass_simple_res


def shuffle_pass(new_list: list) -> str:
    random.shuffle(new_list)
    res_pass = "".join(new_list)
    return res_pass


def main(c_up_case: int, c_low_case: int, c_numbers: int, c_special_char: int) -> str:
    pass_simple_res = range_symbols(c_up_case, c_low_case, c_numbers, c_special_char)
    r = shuffle_pass(pass_simple_res)
    return f'Your strong password {r} with {c_up_case + c_low_case + c_numbers + c_special_char} symbols'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password generator')

    parser.add_argument('-u', action="store", dest="upper_case", default=5, type=int)
    parser.add_argument('-l', action="store", dest="lower_case", default=4, type=int)
    parser.add_argument('-n', action="store", dest="numbers", default=3, type=int)
    parser.add_argument('-s', action="store", dest="special_char", default=2, type=int)

    args = parser.parse_args()

    print(main(args.upper_case, args.lower_case, args.numbers, args.special_char))
