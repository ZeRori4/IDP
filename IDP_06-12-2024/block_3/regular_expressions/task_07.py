# -*- coding: utf-8 -*-

"""
Напишите функцию, которая принимает список строк и возвращает список, состоящий только из тех входных строк, что
являются IP-адресами (v4).
"""


import re


def filter_ips(ip_list):
    valid_ips = []
    pattern = r'^(\d{1,3}\.){3}\d{1,3}$'
    for ip in ip_list:
        if re.match(pattern, ip):
            parts = ip.split('.')
            if all(0 <= int(part) <= 255 for part in parts):
                valid_ips.append(ip)
    return valid_ips


ip_strings = ['192.168.1.1', '256.100.50.25', '10.0.0.1', 'invalid_ip', '172.16.254.1']
print(filter_ips(ip_strings))
