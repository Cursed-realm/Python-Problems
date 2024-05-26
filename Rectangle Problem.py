class Rectangle:
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    
    def Area(self):
        return self.length*self.breath

    def Perimeter(self):
        return 2*(self.length+self.breath)
    
a = eval(input("ENTER A LENGTH:"))
b = eval(input("ENTER A BREATH:"))
obj = Rectangle(a,b)
print("AREA OF RECTANGLE IS:",obj.Area())
print("PERIMETER OF RECTANGLE IS:",obj.Perimeter())