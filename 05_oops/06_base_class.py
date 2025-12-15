class A:
    def __init__(self , a, b):
        self.a = a 
        self.b =b

    
# 1. calling base class duplicate method 
class B ( A):

    def __init__(self , a, b , c ):
        self.a = a 
        self.b =b
        self.c = c


# 2. calling base class using class Name 
class C ( A):

    def __init__(self , a, b , c ):
       A.__init__(self, a,b)
       self.c = c


# 3.  calling using super method 
class C ( A):

    def __init__(self , a, b , c ):
       super().__init__(self ,A,B)
       self.c = c


