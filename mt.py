class Add:
    def sum(self, a, b): #method overloading
        print(a+b)

    def sum(self, a, b, c): #method overloading
        print(a+b+c)

class ComplexNumber:
    def __init__(self, real, img): #Operator Overloading
        self.real = real
        self.img = img

    def __add__(self, other): #Operator Overloading
        return ComplexNumber(self.real + other.real, self.img + other.img)

c1 = ComplexNumber(1,2)
c2 = ComplexNumber(3,4)
c3 = c1 + c2
print(c3.real, "r + i",c3.img)