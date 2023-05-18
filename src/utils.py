import os
import yaml
from typing import Any


def give_params(configpath: str, params: dict[str, Any]):
    # чтото
    with open(file=configpath, mode='w') as file:
        yaml.dump(params, file)


def get_params(configpath: str) -> dict[str, Any]:
    """Функция для загрузки параметров отбора признаков и конфигурации всего пайплайна.


    Args:
        configpath (_type_): Путь к yaml-файлу с конфигурацией.

    Returns:
        dict[str, Any]: Параметры пайплайна и отбора признаков
    """
    if not os.path.isfile(configpath):
        raise ValueError('\033[31mAdd the configuration file\033[0m')
    with open(file=configpath, mode='r', encoding='utf-8') as file:
        config = yaml.safe_load(file)
    return config


def get_named_params(*args) -> dict[str, Any]:
    res_dict = {}
    for name, value in args:
        if value:
            res_dict[name] = value
    return res_dict
