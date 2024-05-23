# -*- coding: utf-8 -*-
# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 33</title>
	<version>1.0</version>
    <parameter>
        <type>string_from_list</type>
        <id>HOT_KEY</id>
        <name>Горячая клавиша</name>
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

resources = {
    "database/base.py": """
        eNqNVE2L2zAQvRv8H4R7cULicwkY2mXbU1tasrdSjGyPsyKylB3J2c2/78iSEiUbSn2S3puP
        Nx/yB7Zerlmne6F2GzbZYf3RIXk2oB4JlxI6K7QyTIwHjZYpPkJvp4OEs42y8GalaKNJQEau
        +A4wz/IsEOZFctk9w3hi3DDD7xCVxnEmdQifUPDWxRTbX98+e/QLosZ7trbqoZMcuRVHiH4J
        1LTcQCLuWRvrrnk2guU9t5zVpLH6TrdHupWLPNuCMdQMR+jKdPoAfWM8VjrEH0e+BywXF/sG
        gfeA/+2WZw+kjcxv5ZZRWh0Ps/Wn2473MLCYoJPaQP2EE6wYwqiPUH/l0tBtudy/ctyZxSbP
        GH1FUfxEfRQ9MM4scmX4PHsu2SyacdST6ok0gAIM0wMj2OmjBanI3cdR8BrLoxpCD8pzNm9k
        8RTSuu8kQPap44VKwKrT4yhsGULQPsDh3S647QHEzf0ISBvd8m4fY7gPuaBuk4+HBkEVy1Sd
        GNjcxQR6p8zxaVDy8d2+cdpGITNZLvzKuQVr/cwvD6wMY3l8KFbsdxGKfAJj6V6EzMmxeZkA
        T8WfPAtR3RoIJWzTtyWonVBQ/9CKJk/7MojdfInDJ73ehAnDHJHoDkQ9v5FqBxQw6G0okvJ/
        CF/K3ED3FmnPSS2PDy8RH80SqPKCKIM/eIPteeoOmxDKVqi+9moWVzbhhf3TND6ZylGUypOe
        u+rgZWlD2PI2Qke4hYbW5FI1gp1QsTjJMilvFeOvrhOR718bAsSB
    """,
    "database/schema.py": """
        eNqNjcEKwjAQRO+B/MPeWqH0A4QeVBC89x627arBbFKz6aF/b0p6VHD3MjAzb7SyPIeYQN4O
        3fgkXgEFBLXS6h4DQzugEOypc9abMzoUgVMp9CSp3pzDUSvIZ0zCwZFHJmOgg2onm5STVcnY
        KRuC7SW4hX2d1c0nelBsYI6WMa7mRWvXx4Ua8ItzG7G7osszhZAsZxzy/BP0tRbRT4GN9en/
        XvkPSY5gmg==
    """,
    "database/__init__.py": """
        eNpLK8rPVdBLSixOVcjMLcgvKlHIzMssiU9J4uUCAIlsCWk=
    """,
}
t1utils.resources_check(script_path, resources)


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
