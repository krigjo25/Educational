

class StringTest():

    def _init_(self):
        return

    def hello(self, name="World"):
        return f'Hello, {name}'

    #   Testing Defaults
    def DefaultTest(self):
        assert self.hello() == 'Hello, World'
        return True

    #   Argument test

    def ArgumentToTest(self, arg):

        assert self.hello(f'{arg}') == f'Hello, {arg}'

        return True

    def HelloWorldTest(self):

        if self.DefaultTest():
            if self.ArgumentToTest('Kristoffer'): return True



srt = StringTest()
srt.HelloWorldTest()