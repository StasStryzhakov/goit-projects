class Meta(type):
    
    children_number = None
    
    def __new__(cls, name, bases, dict):
        dict.update(class_number=cls.children_number)
        cls.children_number += 1
        instance = super().__new__(cls, name, bases, dict)
        return instance
        


Meta.children_number = 0

class Cls1(metaclass=Meta):
    def __init__(self, data):
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        self.data = data


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')

assert (a.class_number, b.class_number) == (0, 1)