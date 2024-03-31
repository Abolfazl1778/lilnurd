class A:
    def __init__(self):
        print("Run init of A class")

    def showA(self):
        print("AAAAAAA")

#-----------------------------------------------------------------------------


class B(A):
    def __init__(self):
        A.__init__(self)
        print("Run init of B class")

    def showB(self):
        print("BBBBBBB")
#----------------------------------------------------------------

class C(B):
    def __init__(self):
        B.__init__(self)
        print("Run init of C class")

    def showC(self):
        print("CCCCCCC")
#------------------------------------------------

c=C()
c.showC()
c.showA()

