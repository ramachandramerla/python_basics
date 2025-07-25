import pandas as pd

#create a class

class Practice:

    def __init__(self):
        pass

    # def reading(self, x,y):
    #     self.x=x
    #     self.y=y

    def chandu(self,x,y):
        return x*y
    
cha = Practice()
a = int(input("provide for x : "))
b = int(input("provide for y : "))

print(cha.chandu(a,b))


class Practice2:
    
    def chan(self,x,y):
        self.x=x
        self.y=y
        return x**y

cha2 = Practice2()

print(cha2.chan(a,b))