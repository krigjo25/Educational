
def main():
    return TestSquare()

class Geometry():

    def _init_(self):
        pass

    def main(self):

        x = int(input('What is x?: '))

        return print (f'x squared is {self.Square(x)}')

    def Square(self, x):

        return x + x


class TestingSquare():

    def _init_(self, cls):

        self.cls = cls


    def TestPositive(self):

        assert self.cls.Square(2) == 4
        assert self.cls.Square(3) == 9

        return

    def TestNegative(self):

        assert self.cls.Square(-2) == 4
        assert self.cls.Square(-3) == 9

        return

    def TestZero(self):

        assert self.cls.Square(0) == 0

        return

    def TestSquare(self):

        if self.TestPositive():
            pass
        else: return 'Does not return positive'

        if self.TestNegative(): pass
        else: return 'Does not return Negative'

        if self.TestZero(): pass
        else:return 'Does not return Zero'

        return True

    def DemoPyTest(self):

    #   Assigning classes to variables


        assert self.cls.Square(2) == 4
        assert self.cls.Square(3) == 9
        assert self.cls.Square(-2) == 4
        assert self.cls.Square(-3) == 9
        assert self.cls.Square(0) == 0

        return

if __name__ == "__main__":
    test = TestingSquare()
    test.cls = Geometry()
    test.TestSquare()