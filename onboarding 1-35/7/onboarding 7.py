# Напишите здесь описание скрипта
'''
<parameters>
	<title>onboarding 7</title>
	<version>1.0</version>
	<parameter>
    <type>objects</type>
    <id>IP_DEVICE</id>
    <name>ip_device</name>
    <value></value>
</parameter>
</parameters>
'''

import host
import random
import string


GLOBALS = globals()

IP_DEVICE = GLOBALS.get("IP_DEVICE", "")


def generate_random_name():
    letters_and_digits = string.ascii_letters + string.digits
    return ''.join(random.choice(letters_and_digits) for i in range(8))



def name_ip_device():
    ip_device_list = IP_DEVICE.split(',')
    for x in host.objects_list("IP Device"):
        sett = host.settings("/%s/ip_cameras/%s" % (x[3][:-1], x[1]))
        if x[0] in ip_device_list:
            sett["name"] = generate_random_name()


name_ip_device()
