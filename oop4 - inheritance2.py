class A:
    def __init__(self):
        print("Run init of A class")

    def showA(self):
        print("AAAAAAA")

#-----------------------------------------------------------------------------


class B:
    def __init__(self):
        print("Run init of B class")

    def showB(self):
        print("BBBBBBB")
#----------------------------------------------------------------

class D:
    def __init__(self):
        print("Run init of D class")

    def showB(self):
        print("DDDDDDD")

#----------------------------------------------------------------

class C(A,B,D):
    def __init__(self):
        A.__init__(self)
        B.__init__(self)
        D.__init__(self)
        print("Run init of C class")

    def showC(self):
        print("CCCCCCC")
#------------------------------------------------

c=C()
c.showC()
