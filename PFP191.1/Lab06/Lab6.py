import  math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        pass
    def __str__(self):
        return f"({self.x} {self.y})"
    def distance(self,x0,y0):
        x=self.x
        y=self.y
        d=math.sqrt((x-x0)*(x-x0)+(y-y0)*(y-y0))
        return round(d,2)
class listOfPoint:
    def __init__(self,list=[] ):
        self.list=list
        pass
    def f0(self,n): #enter nof Point to the list
        for i in range(1,n+1):    
            print(f"Enter point {i}")
            x=getfloat("Enter x: ")
            y=getfloat("Enter y: ")
            p=Point(x,y)
            self.list.append(p)
        pass
    def f1(self,x0,y0):
        for i in self.list:
            print(f"Distance from ({x0},{y0}) to ({i.x},{i.y}): {i.distance(x0,y0)}")     
        pass

    def f2(self):
        sum=0
        for i in self.list:
            sum+=i.x
        return round(sum/len(self.list),2)
        pass
    def getMax(self):
        max =   self.list[0].distance(0,0)
        for i in self.list:
            if i.distance(0,0) > max:
                max = i.distance(0,0)
        return max
    def f3(self):
        max=self.getMax()
        for i in self.list:
            if i.distance(0,0)==max:
                print(i,end=" ")
        pass
    def f4(self,r):
        L=[]
        for i in self.list:
            if i.x**2+i.y**2<=r**2:
                L.append(i)
        return L
        pass
def getInt(s):
    while True :
        try:
            n=int(input(s))
        except :
            print("Wrong integer number. Try again!!!\n")
        else :
            return n
def getfloat(s):
    while True :
        try :
            n=float(input(s))
        except :
            print("Wrong number. Try again!!!")
        else :
            return n
def Menu():
    print("1. Test f1")
    print("2. Test f2")
    print("3. Test f3")
    print("4. Test f4")
    print("Your selection (1 -> 4) : ")
    pass
list=listOfPoint()
Menu()
sel=getInt(" ")
num=getInt("Enter the number of Point: ")
print("OUTPUT")
list.f0(num)
print("OUTPUT")
 
if sel==1:
    x0=getfloat("Enter x0 = ")
    y0= getfloat("Enter y0 = ")
    list.f1(x0,y0)
    pass
elif sel==2:
    print(list.f2())
    pass
elif sel==3:
    list.f3()
    pass
elif sel==4:
    print(list.f4())
    pass
else :
    print("Wrong number")
print("Finish")