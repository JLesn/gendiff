def get_indent(depth):
    return " " * (depth * 4 - 2)


def format_value(value, depth):
    if value is True:
        return "true"
    if value is False:
        return "false"
    if value is None:
        return "null"
    if type(value) is dict:
        lst = []
        for k, v in value.items():
            lst.append(
                f"{get_indent(depth + 1)}  "
                f"{k}: {format_value(v, depth + 1)}")
            res = "\n".join(lst)
        return f"{{\n{res}\n  {get_indent(depth)}}}"
    else:
        return str(value)


def stylish(diff, depth=1):
    types = {
        "added": "+ ",
        "removed": "- ",
        "unchanged": "  ",
    }
    res = []
    for node in diff:
        if node["type"] == "recursive":
            value = stylish(node["children"], depth + 1)
            res.append(
                f"{get_indent(depth)}  {node['node']}: "
                f"{{\n{value}\n{get_indent(depth)}  }}"
            )
        elif node["type"] == "changed":
            value_before = format_value(node["value_before"], depth)
            value_after = format_value(node["value_after"], depth)
            res.append(
                f"{get_indent(depth)}{types['removed']}"
                f"{node['node']}: {value_before}"
            )
            res.append(
                f"{get_indent(depth)}{types['added']}"
                f"{node['node']}: {value_after}"
            )
        else:
            value = format_value(node["value"], depth)
            res.append(
                f"{get_indent(depth)}{types[node['type']]}"
                f"{node['node']}: {value}"
            )
    return "\n".join(res)
