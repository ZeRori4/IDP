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


def set_new_ip_device_names():
    ip_device_list = IP_DEVICE.split(',')
    if not IP_DEVICE:
        for sett in host.settings("ip_cameras").ls():
            if sett.type == "Grabber" and sett["grabber_enabled"]:
                sett["name"] = generate_random_name()
    else:
        for ip_device in ip_device_list:
            for sett in host.settings("ip_cameras").ls():
                if (
                        sett.type == "Grabber"
                        and sett["grabber_enabled"]
                        and sett["name"] == ip_device
                ):
                    sett["name"] = generate_random_name()


set_new_ip_device_names()
