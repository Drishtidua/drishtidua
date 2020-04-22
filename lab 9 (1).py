#!/usr/bin/env python
# coding: utf-8

# # lab 9

# In[1]:


class triangle:
    a=0
    b=0
    c=0
    def create_triangle(self,side1 ,side2 , side3):
        self.a=side1
        self.b=side2
        self.c=side3
    def print_sides(self):
        print(self.a)
        print(self.b)
        print(self.c)
triangle1 = triangle()              
triangle1.create_triangle(10,20,30)             
triangle1.print_sides()      


# In[6]:


class Rectangle:
    w=0.0
    l=0.0
    def perimeter(self):
        self.l=int(input("Enter The Length :"))
        self.w=int(input("Enter The width : "))
        return (2*(self.l+self.w))
r1=Rectangle()
print("The Perimeter of Rectangle is",r1.perimeter())


# In[2]:


class Circle():
    def __init__(self, radius):
        self.radius = radius
    def perimeter(self):
        return (2*3.14*self.radius)
    def area(self):
        return (3.14*self.radius*self.radius)
r=int(input("enter radius of circle "))        
Circle1 = Circle(r)   
print("the perimeter of circle " , Circle1.perimeter())
print("the area of circle ", Circle1.area())


# In[14]:


class Student:
    name=""
    rollno=""
    marks=100
    def basic_profile(self):
        return(self.name,self.rollno,self.marks)
stu1=Student()
stu1.name="dd"
stu1.rollno="1000"
stu1.marks=200
print(stu1.basic_profile())


# In[13]:


class abcd:
    def inputstr(self):
        print("string")
    def printstr(self):
        print("string")

                   
abcd1=abcd()
abcd1.printstr()
abcd1.inputstr()


# In[7]:


class Temp:
    f=0.0
    c=0.0
    def convertf(self):
        self.f=int(input("Enter the Temp in F"))
        return ((self.f-32)/1.8)
    def convertc(self):
        self.c=int(input("Enter The Temp in c"))
        return ((self.c*1.8)+32)
t1=Temp()
print("The Conversion of F to C is",t1.convertf())
print("The Conversion of C to F is", t1.convertc())


# In[12]:


class Time:
    hour = 0
    hour1 = 0
    min = 0
    min1 = 0
    tothr=0
    totmin=0

    def addTime(self):
        self.hour = int(input("Enter The Hour "))
        self.min = int(input("Enter the minute"))
        self.hour1 = int(input("Enter Another hour"))
        self.min1 = int(input("Enter Another Minute"))

    def displaytime(self):
        self.tothr=self.hour + self.hour1
        self.totmin=self.min + self.min1
        print(self.tothr,"Hour and ",self.totmin,"min")
    def displaymin(self):
        return (60*self.tothr+self.totmin)
b1 = Time()
b1.addTime()
print("The Total Time is")
b1.displaytime()
print("The Total Minute is",b1.displaymin())


# In[ ]:




