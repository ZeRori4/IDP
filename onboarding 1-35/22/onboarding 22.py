# -*- coding: utf-8 -*-
'''
<parameters>
	<title>onboarding 21</title>
	<version>1.0</version>
</parameters>
'''

from datetime import datetime

import host
from __builtin__ import object as py_object


def count_without_uniform(zones):
    count = 0
    for zone in zones:
        for obj_inside in zone.objects_inside:
            # Объекты, которые носят униформу выбранных цветов, будут иметь class_id отличный от person
            # alert(obj_inside.class_id) # гуид настройки цвета униформы в Нейронном детекторе   ^^^^^^
            if obj_inside.class_id == "person":
                count += 1
    return count


def msg_alarm(channel):
    message("{date} Обнаружен человек без униформы на канале {channel}.".format(
        date=datetime.now().strftime("%Y.%m.%d %H:%M:%S"),
        channel=channel
    ))


class Handler(py_object):
    def __init__(self):
        self.data = {}

    def handler(self, event):
        count = count_without_uniform(event.zones)
        channel = host.settings("/{server}/channels/{channel}".format(
            server=event.server_guid, channel=event.channel_guid
        ))
        if count - self.data.get(channel.name, 0) > 0:
            msg_alarm(channel.name)

        self.data[channel.name] = count


handler = Handler()
host.activate_on_deep_detection_events(handler.handler)
