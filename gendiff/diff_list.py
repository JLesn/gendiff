def get_diff(f1, f2):
    res = []
    keys = sorted(f1.keys() | f2.keys())
    for key in keys:
        node = {'node': key}
        if key not in f2:
            node['type'] = 'removed'
            node['value'] = f1[key]
        elif key not in f1:
            node['type'] = 'added'
            node['value'] = f2[key]
        elif type(f1[key]) is dict and type(f2[key]) is dict:
            node['type'] = 'recursive'
            node['children'] = get_diff(f1[key], f2[key])
        elif f1[key] == f2[key]:
            node['type'] = 'unchanged'
            node['value'] = f1[key]
        else:
            node['type'] = 'changed'
            node['value_before'] = f1[key]
            node['value_after'] = f2[key]
        res.append(node)
    return res
