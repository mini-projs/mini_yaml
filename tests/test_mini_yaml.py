import sys
sys.path.append('/Users/lei/workspace/program/mini_yaml/')

from src.mini_yaml import load, dump, YAMLObject

class ExampleClass(YAMLObject):
    def __init__(self, key1, key2):
        self.key1 = key1
        self.key2 = key2
    yaml_tag = '!example'  # 对象需要定义 yaml_tag 属性


def test_load():
    # 测试 load 函数
    yaml_str = "!example\nkey1: value1\nkey2: value2"
    expected_dict = {'key1': 'value1', 'key2': 'value2'}
    # 进行 load 函数的调用
    obj = load(yaml_str)
    assert obj.__dict__ == expected_dict

def test_dump():
    # 创建 ExampleClass 的实例
    obj = ExampleClass('value1', 'value2')
    expected_yaml = "!example\nkey1: value1\nkey2: value2"
    # 进行 dump 函数的调用
    yaml_output = dump(obj)
    assert yaml_output == expected_yaml

def test_load_dump_integration():
    # 测试 load 和 dump 的集成

    obj = ExampleClass('value1', 'value2')
    yaml_output = dump(obj)
    loaded_obj = load(yaml_output)
    assert obj.__dict__ == loaded_obj.__dict__
