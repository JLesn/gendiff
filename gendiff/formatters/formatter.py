from gendiff.formatters.stylish import stylish
from gendiff.formatters.plain import plain


def get_format(diff_list, format='stylish'):
    if format == 'stylish':
        return stylish(diff_list)
    elif format == 'plain':
        return plain(diff_list)
