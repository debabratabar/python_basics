class A:
    def show(self): print("A")

    @staticmethod
    def print():
        print('I am class A')


class B(A):

    @staticmethod
    def print():
        print('I am overidding class A ')

A.print()

objA = A()

objA.print()


objB = B()
objB.print()

