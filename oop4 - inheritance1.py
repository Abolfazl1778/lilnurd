class A:
    def __init__(self):
        print("Run init of A class")

    def showA(self):
        print("AAAAAAA")

#-----------------------------------------------------------------------------


class B(A):
    def __init__(self):
        #super().__init__()
        A.__init__(self)
        print("Run init of B class")

    def showB(self):
        print("BBBBBBB")

#----------------------------------------------------------------


b=B()
b.showA()
b.showB()

