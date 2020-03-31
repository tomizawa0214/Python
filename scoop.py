class Foo:
    def hello(self):
        print('Hello from Foo')
    def hello_goodbye(self):
        self.hello()
        print('Goodbye from Foo')
    def show_attr(self):
        print(f'{self.__class__}: {dir(self)}')

class Bar(Foo):
    def hello(self):
        print('Hello from Bar')
    def goodbye(self):
        print('Goodbye from Bar')

foo = Foo()
# foo.show_attr()
bar = Bar()
# bar.show_attr()

# foo.hello()
# bar.hello()

foo.hello_goodbye()
bar.hello_goodbye()