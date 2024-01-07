from gendiff.formatters.stylish import stylish
from gendiff.formatters.json import json
from gendiff.formatters.plain import plain


def get_format(diff_list, format="stylish"):
    if format == "stylish":
        return "{\n" + stylish(diff_list) + "\n}"
    elif format == "plain":
        return plain(diff_list)
    elif format == "json":
        return "{\n" + json(diff_list) + "\n}"
