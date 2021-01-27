#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
from typing import Any, Dict

import requests
import configparser

commands = {"play": "setPlayerCmd:play:",
            "play_pause": "setPlayerCmd:onepause",
            "stop": "setPlayerCmd:stop",
            "next": "setPlayerCmd:next",
            "pause": "setPlayerCmd:pause",
            "vol_down": "setPlayerCmd:vol--",
            "voldown": "key_id_press:voldown",
            "vol_up": "setPlayerCmd:vol++",
            "mute": "setPlayerCmd:mute:1",
            "unmute": "setPlayerCmd:mute:0",
            "channel_next": "setPlayerCmd:channel_next",
            "shutdown": "shutdown",
            "get_play_status": "setPlayerCmd:ext_getPlayStatus",
            "get_player_status": "getPlayerStatus",
            "vol_get": "setPlayerCmd:ext_vol_get",
            "mute_get": "setPlayerCmd:mute_get",
            "get_play_mode": "setPlayerCmd:ext_getPlayMode",
            }


def get_config() -> dict:
    """
    Получает конфиг если он есть, если нет то создает файл с дефаулт конфигом
    Испорченный конфиг тоже починит
    :return: dict
    """
    host = {}
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "conf.ini")
    cfg = configparser.ConfigParser()

    def write_file():
        cfg.write(open('conf.ini', 'w'))

    if not os.path.exists(config_path):
        cfg["DEFAULT"] = {"server": '192.168.1.4', "url": "httpapi.asp?command="}
        write_file()
    try:
        cfg.read(config_path)
        host["ip"] = cfg.get("DEFAULT", "server")
        host["url"] = f'http://{host["ip"]}/{cfg.get("DEFAULT", "url")}'
    # except Exception as e:
    except configparser.NoOptionError:
        cfg["DEFAULT"] = {"server": '192.168.1.4', "url": "httpapi.asp?command="}
        write_file()
        host["ip"] = cfg.get("DEFAULT", "server")
        host["url"] = f'http://{host["ip"]}/{cfg.get("DEFAULT", "url")}'
    return host


def set_player(url: str, command: str) -> Any:
    """
    Выполнение команды
    :param url: str
    :param command: str
    :return: Any
    """
    res = requests.post(url+command)
    if res.status_code == 200:
        return res.content


def get_player_status(url: str) -> Dict:
    """
    TODO: надо сделать словарь только нужного status vol mute curpos totlen Title Album Artist
    есть еще команда getStatus
    Получение статуса пример ответа
    {'type': '0', 'ch': '0', 'mode': '10', 'loop': '0', 'eq': '0', 'status': 'play', 'curpos': '786542',
    'totlen': '0', 'Title': 'http://nashe1.hostingradio.ru/nashe-256', 'Artist': '556E6B6E6F776E',
     'Album': '556E6B6E6F776E', 'alarmflag': '0', 'plicount': '0',
     'plicurr': '0', 'vol': '100', 'mute': '0'}

    :param url: str
    :return: Dict
    """
    res = requests.get(url+commands["get_player_status"])
    if res.status_code == 200:
        result = res.json()
        print(bytes.fromhex(result["Artist"]).decode("utf-8"))
        print(result["Title"])
        print(bytes.fromhex(result["Album"]).decode("utf-8"))
        # return


def main():
    host = get_config()
    url = host["url"]
    # print(get_player_status(url))
    set_player(host["url"], commands["play"] + "http://nashe1.hostingradio.ru/nashe-256")
    # print(set_player(url, "getStatus"))
    print(get_player_status(url))


if __name__ == '__main__':
    main()

