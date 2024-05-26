# class Vehicle:
#     def __init__(self, make, model, year):
#         self.make = make 
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return f"{self.year} {self.make} {self.model}"

# class Car(Vehicle):
#     def __init__(self, make, model, year, num_doors):
#         super().__init__(make, model, year)
#         self.num_doors = num_doors

#     def display_info(self):
#         return f"{super().display_info()}, {self.num_doors}-door car"

# class Motorcycle(Vehicle):
#     def __init__(self, make, model, year, num_wheels):
#         super().__init__(make, model, year)
#         self.num_wheels = num_wheels

#     def display_info(self):
#         return f"{super().display_info()}, {self.num_wheels}-wheeler motorcycle"


# car1 = Car("Toyota", "Camry", 2022, 4)
# motorcycle1 = Motorcycle("Harley-Davidson", "Street Glide", 2022, 2)

# print(car1.display_info())        
# print(motorcycle1.display_info())  
# -----------------------------------------------------------------------------------------
# class car:
#     def __init__(self,model,brand):
#         self.model = model
#         self.brand = brand 
#         self.is_running = True

#     def start_engine(self):
#         if self.is_running:
#             print("Model is running")
#             self.is_running = True
#         else:
#             print("Model is stopped") 

#     def get_info(self):
#         return f"Model is {self.model} and Brand of {self.brand}"
    
# car1 = car("Agera rs","Koenigsegg")
# car2 = car("Divo","Bugatti")

# print(f"Car1:{car1.get_info()}")
# car1.start_engine()

# print(f"Car2:{car2.get_info()}")
# car2.start_engine()
# -----------------------------------------------------------------------------------------
# class Player:
#     def __init__(self,power,skill,weapon):
#         self.power = power
#         self.skill = skill
#         self.weapon = weapon
#         self.is_fighting = True
#         self.weapon_avail = True

#     def fighting(self):
#         if self.is_fighting:
#             print("Player is busy rn")
#             self.is_fighting = True
#         else:
#             print("Player is free")

#     def weapons_Available(self):
#         if self.weapon_avail:
#             print("Weapon is available")
#             self.weapon_avail = True
#         else:
#             print("Weapon is not available")

#     def get_info(self):
#         return f"Power:{self.power}, Skill:{self.skill}, Weapons:{self.weapon}"

# P1 = Player(100000,"Martial Arts,Kung Fu,Judo","Ak47,Sniper")
# P2 = Player(100000000,"Invisible,High Jump","Rifle,Revolver")

# print(f"Player1:{P1.get_info()}")
# P1.fighting()
# P1.weapons_Available()

# print(f"Player2:{P2.get_info()}")
# P2.fighting()
# P2.weapons_Available()
# -----------------------------------------------------------------------------------------
# class Bank_Account:
#     def __init__(self,name,account_number,balance):
#         self.name=name
#         self.account_number=account_number
#         self.balance=balance
#         self.deposited=False

#     def deposit(self):
#         if not self.deposited:
#             print(f"{self.name} {self.account_number} {self.balance} has deposited the money")
#             self.deposited=True
#         else:
#             print("Money hasn't deposited")

#     def withdraw(self):
#         if self.deposited:
#             print(f"{self.name} {self.account_number} {self.balance} has deposited the money")
#             self.deposited=True
#         else:
#             print("Money hasn't deposited")

#     def get_info(self):
#         return f"{self.name} {self.account_number} {self.balance}"

# Bank_Account1 = Bank_Account("Aditya",1234,1000000)
# Bank_Account2 = Bank_Account("Anirudh",5678,100)


# print(f"Bank_account: {Bank_Account1.get_info()}")
# Bank_Account1.deposit()
# Bank_Account1.withdraw()

# print(f"\n Bank_Account2: {Bank_Account2.get_info()}")
# Bank_Account2.deposit()
# Bank_Account2.withdraw()
# -----------------------------------------------------------------------------------------
# class staff_info:
#     def __init__(self,staff_no,staff_name,staff_designation,staff_salary):
#         self.staff_no = staff_no
#         self.staff_name = staff_name
#         self.staff_designation = staff_designation
#         self.staff_salary = staff_salary

#     def get_info(self):
#         return f"{self.staff_no} {self.staff_name} {self.staff_designation} {self.staff_salary}"
    
# staff1 = staff_info(1,"Aditya","EM1",200000)
# staff2 = staff_info(2,"Anirudh","EM2",2000)

# print(f"Staff_info: {staff1.get_info()}")
# print(f"Staff_info: {staff2.get_info()}")
# -----------------------------------------------------------------------------------------
# class ElectronicDevice:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def display_info(self):
#         return {
#             'Brand' : self.brand,
#             'Model' : self.model,
#             'Year' : self.year
#             }
    
# class Television(ElectronicDevice):
#     def __init__(self,brand,model,year,screen_size):
#         super().__init__(brand,model,year)
#         self.screen_size = screen_size

#     def display_info(self):
#         return f"{super().display_info()},Screen Size is {self.screen_size}"
    
# class Smartphone(ElectronicDevice):
#     def __init__(self, brand, model, year,operating_system):
#         super().__init__(brand, model, year)
#         self.operating_system = operating_system

#     def display_info(self):
#         return f"{super().display_info()},Operating System is {self.operating_system}"
    

# Tv1 = Television('Samsung','QLED',2022,55.5)
# Tv2 = Television('Sony','LED',2002,45)
# SP1 = Smartphone('Apple','iphone15',2022,'ios')
# SP2 = Smartphone('Samsung','S24 Ultra',2024,'Android')


# print(Tv1.display_info())
# print(Tv2.display_info())
# print(SP1.display_info())
# print(SP2.display_info())
# -----------------------------------------------------------------------------------------
# class Appliance:
#     def __init__(self,Brand,Model,Year):
#         self.Brand = Brand 
#         self.Model = Model
#         self.Year = Year

#     def Appliance_info(self):
#         return {
#             'Brand' : self.Brand,
#             'Model' : self.Model,
#             'Year' : self.Year
#         }
    
# class Refrigerator(Appliance):
#     def __init__(self, Brand, Model, Year,Capacity):
#         Appliance.__init__(self,Brand, Model, Year)
#         self.Capacity = Capacity

#     def Refrgrator_info(self):
#         return f"{Appliance.Appliance_info(self)},Capacity is {self.Capacity}L"
    
# class washingmachine(Appliance):
#     def __init__(self, Brand, Model, Year,Load_Capacity):
#         Appliance.__init__(self,Brand, Model, Year)
#         self.Load_Capacity = Load_Capacity

#     def washingmachine_info(self):
#         return f"{Appliance.Appliance_info(self)},Load Capacity is {self.Load_Capacity}L"
    
# F1 = Refrigerator('LG','French Door',2022,20.0)
# W1 = washingmachine('Samsung','Top Load',2022,9.8)

# print(F1.Refrgrator_info())
# print(W1.washingmachine_info())
# -----------------------------------------------------------------------------------------
# class shape:
#     def __init__(self,length,width,height):
#         self.length = length
#         self.width = width
#         self.height = height

#     def display_info(self):
#         return f"Length:{self.length},Width:{self.width},Height:{self.height}"
    
# class rectangle(shape):
#     def __init__(self, length, width, height):
#         super().__init__(length, width, height)

#     def Area1(self):
#         return f"Area of rectangle:{self.length*self.width}"
#     def Perimeter1(self):
#         return f"Perimeter of rectangle:{2*(self.length+self.width)}"
    
# class square(shape):
#     def __init__(self, length, width, height):
#         super().__init__(length, width, height)

#     def Area2(self):
#         return f"Area of square:{self.length*self.length}"
#     def Perimeter2(self):
#         return f"Perimeter of square:{4*self.length}"
    
# a = int(input("Enter a length:"))
# b = int(input("Enter a width:"))
# c = int(input("Enter a heigth:"))

# obj1 = rectangle(a,b,c)
# obj2 = square(a,b,c)

# print(obj1.Area1())
# print(obj1.Perimeter1())
# print(obj2.Area2())
# print(obj2.Perimeter2())
# -----------------------------------------------------------------------------------------
# import tkinter as tk 

# class ToDoList:
#     def __init__(self,win):
#         self.win = win
#         win.title('To-Do-List')

#         self.entry = tk.Entry(win,width=20)
#         self.entry.grid(row=0,column=0)

#         self.bt1 = tk.Button(win,text='Add Item',command=self.addItem)
#         self.bt1.grid(row=0,column=1)

#         self.listbox = tk.Listbox(win,width=40)
#         self.listbox.grid(row=1,column=0,columnspan=2)

#         self.bt2 = tk.Button(win,text='Delete Item',command=self.delItem)
#         self.bt2.grid(row=2,column=0)

#         self.bt3 = tk.Button(win,text='Delete All Item',command=self.delallItem)
#         self.bt3.grid(row=2,column=1)

#     def addItem(self):
#         data = self.entry.get()
#         self.entry.delete(0,tk.END)
#         self.listbox.insert(tk.END,data)

#     def delItem(self):
#         index = self.listbox.curselection()
#         self.listbox.delete(index)

#     def delallItem(self):
#         self.listbox.delete(0,tk.END)

# root = tk.Tk()
# exc = ToDoList(root)
# root.mainloop()
# -----------------------------------------------------------------------------------------------------------------------------------
# class product:
#     def __init__(self,price):
#         self.price = price 

# class electronics(product):
#     def __init__(self, price):
#         super().__init__(price)

#     def calculate_discount(self):
#         return f'Discount:{self.price*0.15}'

# class clothing(product):
#     def __init__(self, price):
#         super().__init__(price)

#     def calculate_discount(self):
#         return f'Discount:{self.price*0.10}'
    
# class books(product):
#     def __init__(self, price):
#         super().__init__(price)

#     def calculate_discount(self):
#         return f'Discount:{self.price*0.05}'
    
# p1 = electronics(200)
# p2 = clothing(50)
# p3 = books(30)

# print(p1.calculate_discount())
# print(p2.calculate_discount())
# print(p3.calculate_discount())
# -----------------------------------------------------------------------------------------------------------------------------------
# class product:
#     def __init__(self,price):
#         self.price = price 

# class electronics(product):
#     def __init__(self, price):
#         super().__init__(price)

#     def calculate_discount(self):
#         return f'Discount on Electronic Item:{self.price*0.15}'

# class clothing(product):
#     def __init__(self, price):
#         super().__init__(price)

#     def calculate_discount(self):
#         return f'Discount on Clothing:{self.price*0.10}'
    
# class books(product):
#     def __init__(self, price):
#         super().__init__(price)

#     def calculate_discount(self):
#         return f'Discount on Book:{self.price*0.05}'


# a = float(input("Enter Price of Electronic Item:"))
# b = float(input("Enter Price of Clothing:"))
# c = float(input("Enter Price of Book:"))

# p1 = electronics(a)
# p2 = clothing(b)
# p3 = books(c)

# print(p1.calculate_discount())
# print(p2.calculate_discount())
# print(p3.calculate_discount())
# -----------------------------------------------------------------------------------------------------------------------------------
# class Weather_Analyzer:
#     def __init__(self,temp):
#         self.temp = temp

#     def Analyze_Condition(self):
#             if self.temp<50:
#                 return("Cold")
#             elif 50<=self.temp<=75:
#                 return("Moderate")
#             elif 76<=self.temp<=90:
#                 return("Warm")
#             else:
#                 return("Hot")

# temp1 = float(input("Enter temperature:"))
# temp2 = float(input("Enter temperature:"))
# temp3 = float(input("Enter temperature:"))
# W1 = Weather_Analyzer(temp1)
# W2 = Weather_Analyzer(temp2)
# W3 = Weather_Analyzer(temp3)
# print("Weather1 Condition:",W1.Analyze_Condition())
# print("Weather2 Condition:",W2.Analyze_Condition())
# print("Weather3 Condition:",W3.Analyze_Condition())
# -----------------------------------------------------------------------------------------------------------------------------------
# class Weather_Analyzer:
#     def __init__(self,temp):
#         self.temp = temp

#     def Analyze_Condition(self):
#             if self.temp<50:
#                 return("Cold")
#             elif 50<=self.temp<=75:
#                 return("Moderate")
#             elif 76<=self.temp<=90:
#                 return("Warm")
#             else:
#                 return("Hot")

# W1 = Weather_Analyzer(35)
# W2 = Weather_Analyzer(65)
# W3 = Weather_Analyzer(95)
# print("Weather1 Condition:",W1.Analyze_Condition())
# print("Weather2 Condition:",W2.Analyze_Condition())
# print("Weather3 Condition:",W3.Analyze_Condition())
# -----------------------------------------------------------------------------------------------------------------------------------
# import tkinter as tk 

# class ToDoList:
#     def __init__(self,win) -> None:
#         self.win = win
#         win.title('ToDoList')
#         self.lst = []
#         self.entry = tk.Entry(win)
#         self.entry.grid(row=0,column=0)

#         tk.Button(win,text='Add',command=self.AddItem).grid(row=0,column=1)

#         self.listBox = tk.Listbox(win)
#         self.listBox.grid(row=0,column=0,columnspan=2)

#         tk.Button(win,text='Delete',command=self.DelItem).grid(row=2,column=0)
#         tk.Button(win,text='Delete All',command=self.DelAll).grid(row=2,column=1)
#         tk.Button(win,text='Undo',command=self.Undo).grid(row=3,column=0,columnspan=2)

#     def AddItem(self):
#         self.listBoxBackup=self.listBox.get(0,tk.END)
#         self.listBox.insert(tk.END,self.entry.get())
#         self.entry.delete(0,tk.END)

#     def DelItem(self):
#         index = self.listBox.curselection()
#         ele = self.listBox.get(index)
#         self.listBox.delete(index)
#         self.lst.append((index,ele))

#     def DelAll(self):
#         self.listBoxBackup = self.listBox.get(0,tk.END)
#         self.listBox.delete(0,tk.END)

#     def Undo(self):
#         if self.lst:
#             index, ele = self.lst.pop()
#             self.listBox.insert(index, ele)

# if __name__ == '_main_':
#     root=tk.Tk()
#     exc=ToDoList(root)
#     root.mainloop()
# -----------------------------------------------------------------------------------------------------------------------------------
# class A:
#     def disp(self):
#         print("this is disp from A")

# class B(A):
#     def disp(self):
#         print("this is disp from B")
#         super().disp()

# class C(A):
#     def disp(self):
#         print("this is disp from C")
#         super().disp()

# class D(B,C):
#     pass

# obj = D()
# obj.disp()
# -----------------------------------------------------------------------------------------------------------------------------------
# for i in range(1,6):
#     if i == 1:
#         print(i, 'little bear')
#     else:
#         print(i, 'little bears')
#     print('Wondering what to do')
#     print('Along came another')
#     print('Then there were', i+1, '!')
# n = 2.777
# print(str(float(int(n))))
# print[print("hello")]
# print('I', 'am', 'the', 'test')
# print('I', 'am', 'the', sep='', end='test')
# print('I', ' ', 'am', ' ', 'the', 'test', sep='_', end='')
# -----------------------------------------------------------------------------------------------------------------------------------
# def is_prime(num):
#   if num <= 1:
#     return False  # 1 or less are not prime
#   for i in range(2, int(num**0.5) + 1):
#     if num % i == 0:
#       return False
#   return True
# number = int(input("Enter a number: "))
# if is_prime(number):
#   print("This number is prime")
# else:
#   print("This number is not prime")
# -----------------------------------------------------------------------------------------------------------------------------------
# l = []
# while True:
#     a = input("Enter:")
#     l.append(a)
#     print(l)
# -----------------------------------------------------------------------------------------------------------------------------------
# n = 12345
# for i in range(0,5):
#     print(n) 
# -----------------------------------------------------------------------------------------------------------------------------------
# n = 12345
# print([n]*5)
# -----------------------------------------------------------------------------------------------------------------------------------
# n = 12345
# for i in range(0,50):
#     print(n,end=",") 
# -----------------------------------------------------------------------------------------------------------------------------------
# l = [1,2,3,4,5]
# print(l)
# l = [1,2,3,4,5]
# print(*l)
# -----------------------------------------------------------------------------------------------------------------------------------
# class array:
#     def __init__(self,ls,) -> None:
#         self.ls = ls
#     def validity(self,m,n):
#         return len(self.ls)==m*n
    
#     def create_matrix(self,m,n):
#         self.M=[]
#         tmp = []
#         count = 0
#         for i in self.ls:
#             tmp.append(i)
#             count+=1
#             if count == n:
#                 self.M.append(tmp)
#                 tmp = []
#                 count=0

#     def display_matrix(self):
#         for i in self.M:
#             print(*i,sep='\t')
        
        
# lst = list(map(int,input().split()))
# row ,column = list(map(int,input().split()))
# arr = array(lst)
# if arr.validity(row,column):
#     arr.create_matrix(row,column)
#     arr.display_matrix()
# else:
#     print("Invalid Dimensions")
# -----------------------------------------------------------------------------------------------------------------------------------
# class Angel:
#     color = "white"
#     feature = "wings"
#     home = "Heaven"


# class Demon:
#     color = "red"
#     feature = "horns"
#     home = "Hell"

# angel = Angel()
# demon = Demon()

# print("Angel")
# print(f"Color: {angel.color}")
# print(f"Feature: {angel.feature}")
# print(f"Home: {angel.home}")

# print("\nDemon")
# print(f"Color: {demon.color}")
# print(f"Feature: {demon.feature}")
# print(f"Home: {demon.home}")
# -----------------------------------------------------------------------------------------------------------------------------------
# a = list(input())
# print(a)
# a = dict(input())
# print(a)
# a = set(input())
# print(a)
# -----------------------------------------------------------------------------------------------------------------------------------
# while True:
#     print("WHAT YOU WANNA DO:\nA.Add\nB.Sub\nC.Multiply\nD.Divide ")
#     x = input("CHOOSE ANY ONE OF THEM:").upper()
#     a = int(input("ENTER A NUMBER:"))
#     b = int(input("ENTER ANOTHER NUMBER:"))
#     if x=="A":
#         print(a+b)
#     elif x=="B":
#         print(a-b)
#     elif x=="C":
#         print(a*b)
#     elif x=="D":
#         print(a/b)
#     else:
#         print("OUT OF RANGE")
# -----------------------------------------------------------------------------------------------------------------------------------
# import numpy as np
# # For list
# arr1 = np.array([1,2,3,4,5,6,7,8,9])
# # For tuple
# arr2 = np.array((1,2,3,4,5,6,7,8,9))
# print(arr1)
# print(arr2)
# print(np.__version__)
# print(type(arr1))
# # 0-Dimensional Array
# print(np.array(42))
# # 1-Dimensional Array
# print(np.array([1,2,3,4,5]))
# # 2-Dimensional Array
# print(np.array([[1,2,3],[4,5,6]]))
# # 3-Dimensional Array 
# print(np.array([[[1,2,3],[4,5,6]],[[7,8,9],[1,5,6]]]))
# # How to check dimensions of array
# a = np.array(42)
# b = np.array([1, 2, 3, 4, 5])
# c = np.array([[1, 2, 3], [4, 5, 6]])
# d = np.array([[[1, 2, 3], [4, 5, 6]], [[10, 20, 30], [40, 50, 60]]])
# print(a.ndim)
# print(b.ndim)
# print(c.ndim)
# print(d.ndim)
# # How to create n dimensional array
# arr3 = np.array([1,2,3,4],ndmin=5)
# print(arr3)
# print(arr3.ndim)
# # How to excess elements of array in 1-D
# print(arr1[0])
# print(arr1[0]+arr1[1])
# # How to excess elements of array 2-D
# # Pass two arguments 1 is row and another one is column
# print(c[:,:]) 
# # How to excess elements in of array 3-D
# # arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
# # Example Explained
# # arr[0, 1, 2] prints the value 6.
# # And this is why:
# # The first number represents the first dimension, which contains two arrays:
# # [[1, 2, 3], [4, 5, 6]]
# # and:
# # [[7, 8, 9], [10, 11, 12]]
# # Since we selected 0, we are left with the first array:
# # [[1, 2, 3], [4, 5, 6]]
# # The second number represents the second dimension, which also contains two arrays:
# # [1, 2, 3]
# # and:
# # [4, 5, 6]
# # Since we selected 1, we are left with the second array:
# # [4, 5, 6]
# # The third number represents the third dimension, which contains three values:
# # 4
# # 5
# # 6
# # Since we selected 2, we end up with the third value:
# # 6
# print(d[0,1,2])
# # # How to take array from user
# # yum= list(map(int,input().split()))
# # you= np.array(yum)
# # print(you)
# # Slicing 
# print(arr1[1:5])
# # Slicing in 2-D
# print(c[1,1:4])
# # Slicing in 3-D
# print(d[0,1,1:4])
# print(arr1.dtype)
# print(arr2.dtype)
# arr4 = np.array(['apple','banana','cherry'])
# print(arr4.dtype) 
# arr5 = np.array([1,2,3,4,5,6],dtype='S')
# print(arr5)
# print(arr5.dtype)
# arr6 = np.array([1,2,3,4,5,6],dtype='i')
# print(arr6)
# print(arr6.dtype)
# # Converting data type on existing arrays 
# arr7 = np.array([1.1,2.2,3.3,4.4,5.5,6.6])
# print(arr7.dtype)
# newarr7 = arr7.astype('i')
# newarr8 = arr7.astype('bool')
# print(newarr7)
# print(newarr8)
# print(newarr7.dtype)
# print(newarr8.dtype)
# print(c.shape)
# -----------------------------------------------------------------------------------------------------------------------------------
# Create a csv file with the name student data and add the following details.
# The details are student id, student name, student subject, and marks. 
# Make sure atleat 10 entries now perform the following operations: 
# 1. Display student marks from student 1 to 5 
# 2. Display the student details from student 7 to 10 
# 3. Find out the average of all the marks 
# 4. Find out the percentage of each student
# 5. Display the grade of each students
# 6. Finally display the first 3 topper of your data
# 7. Add deatils to csv file 
# -----------------------------------------------------------------------------------------------------------------------------------
# while True:
#     age = int(input("ENTER YOUR AGE:"))
#     income = int(input("ENTER YOUR INCOME:"))
#     if age>=18 or income>=60000:
#         print("YOU ARE ELIGIBLE")
#     else:
#         print("YOU ARE NOT ELIGIBLE\nTRY AGAIN")
# while True:
#     age = int(input("ENTER YOUR AGE:"))
#     income = int(input("ENTER YOUR INCOME:"))
#     if age>=18 and income>=60000:
#         print("YOU ARE ELIGIBLE")
#     else:
#         print("YOU ARE NOT ELIGIBLE\nTRY AGAIN")
# -----------------------------------------------------------------------------------------------------------------------------------
# def print_full_name(first,last):
#     return f"Hello {first} {last}!You just delved into python."

# first_name=input()
# last_name=input()
# print(print_full_name(first_name,last_name))
# -----------------------------------------------------------------------------------------------------------------------------------
# def print_full_name(first,last):
#     print(f"Hello {first} {last}!You just delved into python.")

# first_name=input()
# last_name=input()
# print_full_name(first_name,last_name)
# -----------------------------------------------------------------------------------------------------------------------------------
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     l=[]
#     for i in range(x+1):
#         for j in range(y+1):
#             for k in range(z+1):
#                 if(i+j+k)!=n:
#                     l.append([i,j,k])
#                 else:
#                     continue
# print(l)
# -----------------------------------------------------------------------------------------------------------------------------------
# A1 = ["a","b","c"]
# print("".join(A1))
# A2 = ["a","b","c"]
# print("\n".join(A2))
# A3 = ["a","b","c"]
# print(",".join(A3))
# # Join is used for joining the elements of list and tuple 
# B = "AdiTyA Is grEaT"
# print(i.swapcase() for i in B)
# -----------------------------------------------------------------------------------------------------------------------------------
# from tkinter import *
# import random
# WIDTH = 500 
# HEIGHT = 500 
# SPEED = 200
# SPACE_SIZE = 20
# BODY_SIZE = 2
# SNAKE = "#00FF00"
# FOOD = "#FFFFFF"
# BACKGROUND = "#000000"
# class Snake: 
#     def __init__(self): 
#         self.body_size = BODY_SIZE 
#         self.coordinates = [] 
#         self.squares = [] 
  
#         for i in range(0, BODY_SIZE): 
#             self.coordinates.append([0, 0]) 
  
#         for x, y in self.coordinates: 
#             square = canvas.create_rectangle( 
#                 x, y, x + SPACE_SIZE, y + SPACE_SIZE,  
#               fill=SNAKE, tag="snake") 
#             self.squares.append(square) 

# class Food: 
  
#     def __init__(self): 
#         x = random.randint(0,  
#             (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
#         y = random.randint(0,  
#              (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE 
  
#         self.coordinates = [x, y] 
  
#         canvas.create_oval(x, y, x + SPACE_SIZE, y +
#                            SPACE_SIZE, fill=FOOD,  
#                            tag="food") 
# def next_turn(snake, food): 
#     x, y = snake.coordinates[0] 
  
#     if direction == "up": 
#         y -= SPACE_SIZE 
#     elif direction == "down": 
#         y += SPACE_SIZE 
#     elif direction == "left": 
#         x -= SPACE_SIZE 
#     elif direction == "right": 
#         x += SPACE_SIZE 
  
#     snake.coordinates.insert(0, (x, y)) 
  
#     square = canvas.create_rectangle( 
#         x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE) 
  
#     snake.squares.insert(0, square) 
  
#     if x == food.coordinates[0] and y == food.coordinates[1]: 
  
#         global score 
  
#         score += 1
  
#         label.config(text="Points:{}".format(score)) 
  
#         canvas.delete("food") 
  
#         food = Food() 
  
#     else: 
  
#         del snake.coordinates[-1] 
  
#         canvas.delete(snake.squares[-1]) 
  
#         del snake.squares[-1] 
  
#     if check_collisions(snake): 
#         game_over() 
  
#     else: 
#         window.after(SPEED, next_turn, snake, food)

# def change_direction(new_direction): 
  
#     global direction 
  
#     if new_direction == 'left': 
#         if direction != 'right': 
#             direction = new_direction 
#     elif new_direction == 'right': 
#         if direction != 'left': 
#             direction = new_direction 
#     elif new_direction == 'up': 
#         if direction != 'down': 
#             direction = new_direction 
#     elif new_direction == 'down': 
#         if direction != 'up': 
#             direction = new_direction 

# def check_collisions(snake): 
  
#     x, y = snake.coordinates[0] 
  
#     if x < 0 or x >= WIDTH: 
#         return True
#     elif y < 0 or y >= HEIGHT: 
#         return True
  
#     for body_part in snake.coordinates[1:]: 
#         if x == body_part[0] and y == body_part[1]: 
#             return True
  
#     return False

# def game_over(): 
  
#     canvas.delete(ALL) 
#     canvas.create_text(canvas.winfo_width()/2,  
#                        canvas.winfo_height()/2, 
#                        font=('consolas', 70),  
#                        text="GAME OVER",  
#                        fill="red", tag="gameover") 
  
  
# window = Tk() 
# window.title("GFG Snake game ") 
  
# score = 0
# direction = 'down'
  
# label = Label(window,  
#               text="Points:{}".format(score),  
#               font=('consolas', 20)) 
# label.pack() 
  
# canvas = Canvas(window, bg=BACKGROUND,  
#                 height=HEIGHT, width=WIDTH) 
# canvas.pack() 
  
# window.update() 
  
# window_width = window.winfo_width() 
# window_height = window.winfo_height() 
# screen_width = window.winfo_screenwidth() 
# screen_height = window.winfo_screenheight() 
  
# x = int((screen_width/2) - (window_width/2)) 
# y = int((screen_height/2) - (window_height/2)) 
  
# window.geometry(f"{window_width}x{window_height}+{x}+{y}") 
  
# window.bind('<Left>',  
#             lambda event: change_direction('left')) 
# window.bind('<Right>',  
#             lambda event: change_direction('right')) 
# window.bind('<Up>',  
#             lambda event: change_direction('up')) 
# window.bind('<Down>',  
#             lambda event: change_direction('down')) 
  
# snake = Snake() 
# food = Food() 
  
# next_turn(snake, food) 
  
# window.mainloop()

  
# from tkinter import *
# import random 
  
# WIDTH = 500
# HEIGHT = 500
# SPEED = 200
# SPACE_SIZE = 20
# BODY_SIZE = 2
# SNAKE = "#00FF00"
# FOOD = "#FFFFFF"
# BACKGROUND = "#000000"
  
# class Snake: 
  
#     def __init__(self): 
#         self.body_size = BODY_SIZE 
#         self.coordinates = [] 
#         self.squares = [] 
  
#         for i in range(0, BODY_SIZE): 
#             self.coordinates.append([0, 0]) 
  
#         for x, y in self.coordinates: 
#             square = canvas.create_rectangle( 
#                 x, y, x + SPACE_SIZE, y + SPACE_SIZE,  
#                       fill=SNAKE, tag="snake") 
#             self.squares.append(square) 
  
# class Food: 
  
#     def __init__(self): 
  
#         x = random.randint(0,  
#                    (WIDTH / SPACE_SIZE)-1) * SPACE_SIZE 
#         y = random.randint(0,  
#                    (HEIGHT / SPACE_SIZE) - 1) * SPACE_SIZE 
  
#         self.coordinates = [x, y] 
  
#         canvas.create_oval(x, y, x + SPACE_SIZE, y +
#                            SPACE_SIZE, fill=FOOD, tag="food") 
  
# def next_turn(snake, food): 
  
#     x, y = snake.coordinates[0] 
  
#     if direction == "up": 
#         y -= SPACE_SIZE 
#     elif direction == "down": 
#         y += SPACE_SIZE 
#     elif direction == "left": 
#         x -= SPACE_SIZE 
#     elif direction == "right": 
#         x += SPACE_SIZE 
  
#     snake.coordinates.insert(0, (x, y)) 
  
#     square = canvas.create_rectangle( 
#         x, y, x + SPACE_SIZE, 
#                   y + SPACE_SIZE, fill=SNAKE) 
  
#     snake.squares.insert(0, square) 
  
#     if x == food.coordinates[0] and y == food.coordinates[1]: 
  
#         global score 
  
#         score += 1
  
#         label.config(text="Points:{}".format(score)) 
  
#         canvas.delete("food") 
  
#         food = Food() 
  
#     else: 
  
#         del snake.coordinates[-1] 
  
#         canvas.delete(snake.squares[-1]) 
  
#         del snake.squares[-1] 
  
#     if check_collisions(snake): 
#         game_over() 
  
#     else: 
#         window.after(SPEED, next_turn, snake, food) 
  
# def change_direction(new_direction): 
  
#     global direction 
  
#     if new_direction == 'left': 
#         if direction != 'right': 
#             direction = new_direction 
#     elif new_direction == 'right': 
#         if direction != 'left': 
#             direction = new_direction 
#     elif new_direction == 'up': 
#         if direction != 'down': 
#             direction = new_direction 
#     elif new_direction == 'down': 
#         if direction != 'up': 
#             direction = new_direction 
  
# def check_collisions(snake): 
  
#     x, y = snake.coordinates[0] 
  
#     if x < 0 or x >= WIDTH: 
#         return True
#     elif y < 0 or y >= HEIGHT: 
#         return True
  
#     for body_part in snake.coordinates[1:]: 
#         if x == body_part[0] and y == body_part[1]: 
#             return True
  
#     return False
  
# def game_over(): 
  
#     canvas.delete(ALL) 
#     canvas.create_text(canvas.winfo_width()/2,  
#                        canvas.winfo_height()/2, 
#                        font=('consolas', 70),  
#                        text="GAME OVER", fill="red",  
#                        tag="gameover") 
  
  
  
# window = Tk() 
# window.title("GFG Snake game ") 
  
  
# score = 0
# direction = 'down'

  
# label = Label(window, text="Points:{}".format(score),  
#               font=('consolas', 20)) 
# label.pack() 
  
# canvas = Canvas(window, bg=BACKGROUND,  
#                 height=HEIGHT, width=WIDTH) 
# canvas.pack() 
  
# window.update() 
  
# window_width = window.winfo_width() 
# window_height = window.winfo_height() 
# screen_width = window.winfo_screenwidth() 
# screen_height = window.winfo_screenheight() 
  
# x = int((screen_width/2) - (window_width/2)) 
# y = int((screen_height/2) - (window_height/2)) 
  
# window.geometry(f"{window_width}x{window_height}+{x}+{y}") 
  
# window.bind('<Left>',  
#             lambda event: change_direction('left')) 
# window.bind('<Right>',  
#             lambda event: change_direction('right')) 
# window.bind('<Up>',  
#             lambda event: change_direction('up')) 
# window.bind('<Down>',  
#             lambda event: change_direction('down')) 
  
# snake = Snake() 
# food = Food() 
  
# next_turn(snake, food) 
  
# window.mainloop() 
# -----------------------------------------------------------------------------------------------------------------------------------
# l = ["Aditya","Anirudh","Vansh","Shresthi","A"]
# for i in l:
#     for j in i:
#         if j=="A":
#             print(i)
# -----------------------------------------------------------------------------------------------------------------------------------
# import numpy as np 
# arr = np.array((1,2,3,4,5,6))
# print(arr.dtype)
# -----------------------------------------------------------------------------------------------------------------------------------
# # Fibonacci Series
# n = int(input("Enter a number:"))
# l = [0,1]
# if n>1:
#     for i in range(1,n-1):
#         A=l[i]+l[i-1]
#         l.append(A)
#     print(l)
# -----------------------------------------------------------------------------------------------------------------------------------
# def prime(num):
#   for i in range(2,(num//2) + 1):
#     if num % i == 0:
#       return False
#   return True

# count = 0
# num = 2
# n=int(input())
# while count < n:
#   if prime(num):
#     print(num)
#     count += 1
#   num += 1
# -----------------------------------------------------------------------------------------------------------------------------------
# l = [[1,2,100],[4,5,6],[7,8,9]]
# sum = 0
# for i in l:
#     sum=sum+max(i)
# print(sum)
# -----------------------------------------------------------------------------------------------------------------------------------
# import numpy as np 
# arr = np.array([[[1,2,3,4,5,6,7,8,9,10],[11,12,13,14,15,16,17,18,19,20],[21,22,23,24,25,26,27,28,29,30]]])
# # print(arr.dtype)
# a=int(input(""))
# b=int(input(""))
# print(np.dot(arr,b))
# print(arr.ndim)
l = list(map(int,input().split()))
l = []
