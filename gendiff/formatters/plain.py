def format_value(value):
    if value is True:
        return "true"
    elif value is False:
        return "false"
    elif value is None:
        return "null"
    elif type(value) is dict:
        return "[complex value]"
    else:
        return "'" + str(value) + "'"


def plain(diff, path=""):
    res = []
    for node in diff:
        if node["type"] == "recursive":
            new_path = path + node["node"] + "."
            res.append(plain(node["children"], new_path))
        elif node["type"] == "added":
            new_path = path + node["node"]
            res.append(
                f"Property '{new_path}' was added with value: "
                f'{format_value(node["value"])}'
            )
        elif node["type"] == "removed":
            new_path = path + node["node"]
            res.append(f"Property '{new_path}' was removed")
        elif node["type"] == "changed":
            new_path = path + node["node"]
            res.append(
                f"Property '{new_path}' was updated. "
                f'From {format_value(node["value_before"])} to '
                f'{format_value(node["value_after"])}'
            )
    return "\n".join(res)
