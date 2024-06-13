# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 33</title>
	<version>1.0</version>
    <parameter>
        <type>string_from_list</type>
        <id>HOT_KEY</id>
        <name>Пользовательская функция</name>
        <value>F3</value>
        <string_list>F1,F2,F3,F4,F5,F6,F7,F8,F9,F10,F11,F12</string_list>
    </parameter>

    <resources>
        <resource>database/base.py</resource>
        <resource>database/schema.py</resource>
        <resource>database/__init__.py</resource>
    </resources>

</parameters>
'''


import random
import time
from database.base import Session
from database.schema import AlchemyTest
from database.base import init_db

import host


GLOBALS = globals()

HOT_KEY = GLOBALS.get("HOT_KEY", "F3")

db = init_db()


def func_hot_key():
    new_entry = AlchemyTest(timestamp=int(time.time()), random_int=random.randint(1, 1000))
    Session.add(new_entry)
    Session.commit()


host.activate_on_shortcut(HOT_KEY, func_hot_key)
