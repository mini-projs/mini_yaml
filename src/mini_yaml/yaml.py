
kls_dict = {}

class YAMLMeta(type):
    def __new__(cls, name, bases, attrs):
        # print(f"YAMLMeta.__new__({cls}, {name}, {bases}, {attrs})")
        kls = super().__new__(cls, name, bases, attrs)
        if name != 'YAMLObject':
            yaml_tag = attrs.get('yaml_tag', f'!{name.lower()}')
            kls_dict[yaml_tag] = kls
        return kls


class YAMLObject(metaclass=YAMLMeta):
    pass

