# -*- coding: utf-8 -*-
#!/usr/bin/env python


count_bs = 4  # Количество символов с верхним регистром
count_ls = 6  # Количество символов с нижним регистром
count_ns = 3  # Количество цифр
count_ss = 2  # Количество спец символов

symbol_dict = {
    count_bs : tuple('QWERTYUPASDFGHJKLZXCVBNM'),
    count_ls : tuple('qwertyuiopasdfghjklzxcvbnm'),
    count_ns : tuple('1234567890'),
    count_ss : tuple('!@#$%&;:<>?/*()'),
}
