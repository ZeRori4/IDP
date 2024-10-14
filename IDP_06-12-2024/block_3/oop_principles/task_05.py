# -*- coding: utf-8 -*-

'''
Реализуйте свой класс CustomDict, в котором будет переопределен стандартный метод get. По умолчанию он возвращает None,
если ключа в словаре нет. Внесите правки, чтобы вместо None возвращался 0.
'''


class CustomDict(dict):
    def get(self, key, default=0):
        return dict.get(self, key, default)


custom_dict = CustomDict()
custom_dict['key_1'] = 1
custom_dict['key_2'] = 2

print(custom_dict.get('key_1'))
print(custom_dict.get('key_2'))
print(custom_dict.get('key_3'))
