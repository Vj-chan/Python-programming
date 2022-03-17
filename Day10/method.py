# Python program using method

class marks:
    def __init__(self,eng: float,tam: float,mat: float,sci: float,ss: float):
        self.eng = eng
        self.tam = tam
        self.mat = mat
        self.sci = sci
        self.ss = ss
    
    # Create a method to calculate the total marks
        
    def totalmarks(self):
        return self.eng+self.tam+self.mat+self.sci+self.ss
    
vijay = marks(90,93,94,83,85)
ajith = marks(87,98,92,95,100)
rajinikanth = marks(100,100,100,100,100)

print('Total marks of vijay is : ',vijay.totalmarks())
print('Total marks of ajith is : ',ajith.totalmarks())
print('Total marks of rajinikanth is : ',rajinikanth.totalmarks())