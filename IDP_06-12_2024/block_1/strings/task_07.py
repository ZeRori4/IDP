# -*- coding: utf-8 -*-

'''
Реализуйте функцию, которая принимает на вход список символов, а возвращает
строку из этих символов, разделенных символом подчеркивания.
'''

def list_to_string_hieroglyph_underlining(list_hieroglyph):
    return '_'.join(map(str, list_hieroglyph))

list_hieroglyph_1 = ['q', 'w', 'y', 'b', 's']


print(list_to_string_hieroglyph_underlining(list_hieroglyph_1))
