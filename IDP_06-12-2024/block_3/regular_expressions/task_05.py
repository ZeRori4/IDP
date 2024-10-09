# -*- coding: utf-8 -*-

'''
Напишите функцию, которая принимает строку и возвращает список всех email адресов из неё.
'''


import re


def extract_emails(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    emails = re.findall(email_pattern, text)
    return emails


input_text = "Вы можете связаться со мной по адресу example@example.com или https://jiradev.trassir.com/."
print(extract_emails(input_text))
