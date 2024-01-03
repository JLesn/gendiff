from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import json


def get_format(diff_list, format='stylish'):
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'json':
        return json(diff_list)
