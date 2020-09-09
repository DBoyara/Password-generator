#!/usr/bin/env python
# -*- coding: utf-8 -*-

import argparse
import random


def range_symbols(symbol_dict: dict) -> str:
    pass_simple = ""

    for key, value in symbol_dict.items():
        for i in range(value):
            n = random.randrange(len(key))
            pass_simple += key[n]

    new_list = list(pass_simple)
    random.shuffle(new_list)
    res_pass = "".join(new_list)

    return res_pass


def main(c_up_case: int, c_low_case: int, c_numbers: int, c_special_char: int, only_pass: bool) -> str:
    """
    The function takes arguments from the command line, creates a dictionary from them,
    and runs the password creation function.
    :param c_up_case: The number of upper case characters
    :param c_low_case: Number of lowercase characters
    :param c_numbers: Number of digits
    :param c_special_char: Number of special characters
    :return: String with a random password
    """
    symbol_dict = {
        'QWERTYUPASDFGHJKLZXCVBNM': c_up_case,
        'qwertyuiopasdfghjklzxcvbnm': c_low_case,
        '1234567890': c_numbers,
        '!@#$%&;:<>"?/*()': c_special_char,
    }

    r = range_symbols(symbol_dict)

    if only_pass:
        return r
    return f'Your strong password {r} with {c_up_case + c_low_case + c_numbers + c_special_char} symbols'


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Password generator')

    parser.add_argument('-u', action="store", dest="upper_case", default=5, type=int)
    parser.add_argument('-l', action="store", dest="lower_case", default=4, type=int)
    parser.add_argument('-n', action="store", dest="numbers", default=3, type=int)
    parser.add_argument('-s', action="store", dest="special_char", default=2, type=int)
    parser.add_argument('-o', action="store_true", dest="only_pass")

    args = parser.parse_args()

    print(main(args.upper_case, args.lower_case, args.numbers, args.special_char, args.only_pass))
