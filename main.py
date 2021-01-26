#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests


def play_radio(ip: str, url: str) -> bool:
    """
    Включает радио по url
    http://IP/httpapi.asp?command=setPlayerCmd:play:http://nashe1.hostingradio.ru/nashe-256
    :param ip: str
    :param url: str
    :return: bool
    """
    return True


def play_stop(ip: str) -> None:
    """
    Останавливает воспроизведение
    Остановка делается с помощью следующего запроса:
    http://IP/httpapi.asp?command=setPlayerCmd:stop
    :param ip:
    :return:
    """
    pass






# http://192.168.1.182//httpapi.asp?command=setPlayerCmd:play:http://nashe1.hostingradio.ru/nashe-256