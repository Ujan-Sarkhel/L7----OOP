class points:
    def __init__(self,a):
        self.a=a
    def __lt__(self,other):
        if(self.a<other.a):
            return "ob1 is less than ob2"
        else: 
            return "ob2 is less than ob1"
    def __eq__(self,other):
        if(self.a==other.a):
            return "ob1 is equal to ob2"
        else: 
            return "ob2 is not equal to ob1"
ob1=points(2)
ob2=points(3)
print(ob1<ob2)
ob3=points(4)
ob4=points(4)
print(ob3==ob4)


