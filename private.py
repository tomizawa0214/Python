class Foo:
    def __init__(self, name):
        self.__name = name # _nameはプライベート
    def get_name(self):
        return self.__name
    def set_name(self, new_name):
        self.__name = new_name
    def show_attr(self):
        print(dir(self))

foo = Foo('deep insider')
# print(foo.get_name())
foo.set_name('atmarkit')
# print(foo.__name)
# foo.show_attr()

class Foo1:
    def __init__(self):
        self.__mynum = 0
    def get_num(self):
        return self.__mynum
    def set_num(self, new_value):
        if 0 < new_value < 101:
            self.__mynum = new_value
        else:
            raise ValueError('value out of range(0-100)')
    mynum = property(get_num, set_num)

foo = Foo1()
foo.mynum = 50
print(foo.mynum)
foo.mynum = 101