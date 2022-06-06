
# class Volume:
#     def __init__(self,l,b,h):
#         self.l=l 
#         self.b=b 
#         self.h=h 
#     def volume(this):
#         v=this.l*this.b*this.h 
#         print(v)
#     def area(this):
#         a=this.l*this.b
#         print(a)
# l=int(input("enter l= "))
# b=int(input("enter b= "))
# h=int(input("enter h= "))
# obj.volume()
# obj.area()
# print(obj.area,obj.volume)
# class Employee:
#     company="google"
#     def showDetails(self):
#         print("this is an employee")
# class Programmer(Employee):
#     language="pyhton"
#     company="youtube"
#     def getLanguage(self):
#         print("the languages is {self.language}")
#     def showDetails(self):
#         print("this is an programmer")
# e=Employee()
# e.showDetails()
# p=Programmer()
# p.showDetails()
# print(p.company)
# class Employee:
#     company="visa"
#     ecode=120
# class Freelancer:
#     company="fiver"
#     level=0
#     def upgradeLevel(self):
#         self.level=self.level+1
# class Programmer(Employee,Freelancer):
#     name="rohit"
# p=Programmer()
# p.upgradeLevel()
# print(p.level)
# print(p.company )
#MULTILEVEL INHERITANCE
# class person:
#     country="india"
#     def takeBreath(self):
#         print("i am breathing....")
# class Employee:
#     company="honda"
#     def getsalary(self):
#         print(f"salary is {self.salary}")
#     def takebreath(self):
#         print("i am an employee so i am luckly breathing")
# class programmer(Employee):
#     company="fiver"
#     def getsalary(self):
#         print(f"no salary to programmer")
# p=person()

# e=Employee()
# pr=programmer()
# p.takeBreath()

# class person:
#     def __init__(self):
#         print("installizing person")
#     country="india"
#     def takeBreath(self):
#         print("i am breathing....")
# class Employee:
#     company="honda"
#     def getsalary(self):
#         print(f"salary is {self.salary}")
#     def takebreath(self):
#         print("i am an employee so i am luckly breathing")
# class programmer(Employee):
#     company="fiver"
#     def getsalary(self):
#         print(f"no salary to programmer")
#     def takeBreath(self):
#         super().takeBreath()
#         print("i ma programme so i am breathingr")
# p=person()
# p.takeBreath()
# e=Employee()
# pr=programmer()
# p.takeBreath()

        
# class Employee:
#     company="camel"
#     salary=100
#     location="delhi"
#     # def changesalary(self,delhi):
#     #     self.__class__.salary= sal              
#     @classmethod   
#     def changeSalary(cls,sal):
#         cls.salary=sal
# e=Employee()
# print(e.salary)
# e.changeSalary(445)
# print(e.salary)
# print(Employee.salary)
# class Employee:
#     company="bharat gas"
#     salary=300
#     salarybonus=33
#     totalsalary=333
#     @property
#     def totalsalary(self):
#         return self.salary +self.salarybonus
#     @totalsalary.setter
#     def totalsalary(self,val):
#         self.salarybonus=val-self.salarybonus
# e=Employee()
# print(e.totalsalary)
# e.totalsalary=5800
# print(e.salarybonus)


# class Number:
#     def __init__(self,num):
#         self.num=num
#     def __add__(self,num2):
#         print("lets add")
#         return self.num*num2.num
#     def __mul__(self,num2):
#         print("lets multiply")
#         return self.num*num2.num
# n1=Number(4)                                             /truediv            //floordiv        *mul
# n2=Number(6)
# sum=n1+n2
# mul=n1*n2-
# print(mul)*# print(sum)


# class Number:
#     def __init__(self,num):
#         self.num=num
#     def __add__(self,num2):
#         print("lets add")
#         return self.num*num2.num
#     def __mul__(self,num2):
#         print("lets multiply")
#         return self.num*num2.num
# def __str__(self):
#     return f"decimal number: {self.num}"

# def __len__(self):
#     return 1
#     print(len(n))
# n=Number(9)
# print(n)


# class C2dvec:
#     def __init__(self,i,j):
#         self.icap=i
#         self.jcap=j
        
# class C3dv(C2dvec):
#     def __init__(self,i,j,k):
        
#         `    
#         self.c
#         /*-\
#             /347890-p=i*
#         self.jcap=j
#         self.kcap=k

# def add(a,b):
#     return a+b
# def sub(a,b):
#     return a-b
# def mul(a,b):
#     return a*b
# def div(a,b):
#     return a/b
# def cal():
#     a=int(input("enter a= "))
#     b=int(input("enter b= "))
#     o=input ("enter + - * / ")
#     if o=="+":
#         print (add(a,b))
#     elif o=='-':
#         print (sub(a,b))
#     elif o=='*':
#         print(mul(a,b))
#     elif o=='/' and b!=0:
#         print(div(a,b))
#     elif o=='/'and b==0:
#         print("the value of b can not be zero")
#     else:
#         print("invalid operator")
# cal()
             
             #  RECURSIVE FUNCTION
# def hello():
#     print("hello world")
#     hello()

# def cal():
#     p=float(input("enter p= "))
#     t=float(input("enter t= "))
#     r=float(input("enter r= "))
#     i=p*t*r
#     print(i)
#     x=input("enter y for more cal= ")
#     if x=='y':
#         cal()
# cal()
# def cal():
#     grandtotal=0
#     bill =''
   
    
#     name=input("enter name=")
#     price=int(input("enter price= "))
#     quantity=int(input("enter quantity= "))
#     total =price*quantity
#     data=f"{name} {price} {quantity} {total}\n"
#     bill=bill+data
#     print(bill)
#     grandtotal=grandtotal+total
    
#     print(grandtotal)
#     x=input("enter y for more cal")
#     if x=='y':
#         cal()

# cal()
a="ram shyam hari gita nita shyam"
if 'ram' in a:
    print('yes',a.count)
    
    