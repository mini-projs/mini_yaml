from .yaml import kls_dict

def load(repr_str):
    repr_list = repr_str.split('\n')
    yaml_tag = repr_list[0]
    kls = kls_dict[yaml_tag]
    attr_dict = {}
    for line in repr_list[1:]:
        k, v = line.split(': ')
        print(k, v)
        attr_dict[k] = v
    print(attr_dict)
    obj = kls(**attr_dict)
    return obj


def dump(obj):
    repr_list = []
    repr_list.append(f'{obj.yaml_tag}')
    for k, v in obj.__dict__.items():
        repr_list.append(f'{k}: {v}')
    res = '\n'.join(repr_list)
    return res