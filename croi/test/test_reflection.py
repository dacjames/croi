import types

import croi

class AttrTest(object):
    class_field0 = 'class_field'
    class_field1 = 0

    @classmethod
    def class_method0(cls):
        pass

    @classmethod
    def class_method1(cls):
        pass

    @property
    def property0(self):
        return 'property0'

    @property
    def property1(self):
        return 'property1'

    def __init__(self):
        self.instance_field0 = 'instance_field'
        self.instance_field1 = 0

    def instance_method0(self):
        pass

    def instance_method1(self):
        pass


def test_public_attrs_field_methods():
    test = AttrTest()

    instance_fields = ['instance_field0', 'instance_field1']
    instance_properties = ['property0', 'property1']
    instance_members = ['instance_field0', 'instance_field1', 'property0', 'property1']
    instance_methods = ['instance_method0', 'instance_method1']
    instance_attrs = [
        'instance_field0', 'instance_field1',
        'instance_method0', 'instance_method1',
        'property0', 'property1',
    ]

    assert croi.instance_fields(test) == instance_fields
    assert croi.instance_properties(test) == instance_properties
    assert croi.instance_members(test) == instance_members
    assert croi.instance_methods(test) == instance_methods
    assert croi.instance_attrs(test) == instance_attrs

    class_fields = ['class_field0', 'class_field1']
    class_methods = ['class_method0', 'class_method1']

    assert croi.class_fields(test) == class_fields
    assert croi.class_methods(test) == class_methods
    assert croi.class_attrs(test) == class_fields + class_methods
