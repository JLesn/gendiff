def plain(diff):
    res = []
    for node in diff:
        if node['type'] == 'removed':
            res.append(f"  - {node['node']}: {node['value']}")
        if node['type'] == 'added':
            res.append(f"  + {node['node']}: {node['value']}")
        if node['type'] == 'unchanged':
            res.append(f"    {node['node']}: {node['value']}")
        if node['type'] == 'changed':
            res.append(f"  - {node['node']}: {node['value_before']}")
            res.append(f"  + {node['node']}: {node['value_after']}")
    return '\n'.join(res).lower()
