# !/usr/bin/python
# -*- coding: utf-8 -*-

"""
< Código responsável por pegar a comunicação com o arduino >

author: Cassiano Kunsch das Neves
last edited: <22/01/2016>
"""

from serial import Serial

def start_communication():
    comport = Serial('COM3', 9600, timeout=5, rtscts=True)

    return comport