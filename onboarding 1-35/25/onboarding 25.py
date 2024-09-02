# -*- coding: utf-8 -*-
import host

def yes():
	host.message("Да")


def no():
	host.message("Нет")


def other():
	host.message("Только начинаю свое знакомство")


host.question("Знакомы ли вы с работой ПО Trassir?",
    "Да", yes,
    "Нет", no,
    "Только начинаю свое знакомство", other,
    60)
