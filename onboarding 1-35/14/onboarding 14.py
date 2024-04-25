# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 14</title>
	<version>1.0</version>
    <parameter>
        <type>string</type>
        <name>email получателей</name>
        <id>EMAIL_TO</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>сообщение</name>
        <id>MESSAGE</id>
        <value></value>
    </parameter>
    <parameter>
        <type>string</type>
        <name>учётная запись email</name>
        <id>EMAIL_FROM</id>
        <value></value>
    </parameter>
</parameters>
'''

import host

GLOBALS = globals()

EMAIL_TO = GLOBALS.get("EMAIL_TO", "")
# "smart_07_08@mail.ru,smart_test_dssl@mail.ru"
MESSAGE = GLOBALS.get("MESSAGE", "")
EMAIL_FROM = GLOBALS.get("EMAIL_FROM", "")
# smart_test_dssl@mail.ru - имя учётной записи


def create_file(my_string):
    with open("hello_world.txt", "w") as my_file:
        my_file.write(my_string)


receivers = EMAIL_TO.split(",")

subject_str = "subject: Hello World!"

text_str = "text: Hello World!"

attachments = []
attachments.append(create_file(MESSAGE))

host.send_mail_from_account(
    EMAIL_FROM,
    receivers,
    subject_str,
    text_str,
    attachments
)
