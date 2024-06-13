# -*- coding: utf-8 -*-
import host


def channel_name(name):
    channel_found = False
    for sett in host.settings("channels").ls():
        if sett.name == name:
            message(sett.guid)
            channel_found = True
            break
    if not channel_found:
        message("Канал не найден")


def fail():
    alert("Я передумал")


ask("Необходимо указать имя канала", channel_name, fail)
