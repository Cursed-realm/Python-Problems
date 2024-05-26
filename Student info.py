# class Student:
#     def __init__(self,name,age,grade):
#         self.name = name
#         self.age = age
#         self.grade = grade

#     def get_info(self):
#         return f"{self.name},{self.age},{self.grade}"
    
# name = (input("ENTER NAME:"))
# age = int(input("ENTER AGE:"))
# grade = (input("ENTER GRADE:"))
# student = Student(name,age,grade)
# print("STUDENT DETAILS ARE:",student.get_info())
# -----------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,percent):
#         self.percent = percent

#     def Grade(self):
#         if self.percent>=90:
#             return "O"
#         elif self.percent>=80:
#             return "A"
#         elif self.percent>=70:
#             return "B"
#         elif self.percent>=60:
#             return "C"
#         elif self.percent>=50:
#             return "D"
#         else:
#             return "fail"

# percent = int(input("ENTER YOUR PERCENTAGE:"))
# obj = Student(percent)
# print("YOUR GRADE IS",obj.Grade())
# -----------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,percent):
#         self.percent = percent

#     def Grade(self):
#         if 90<self.percent<=100:
#             return "A"
#         elif 80<self.percent<=90:
#             return "B"
#         elif 70<self.percent<=80:
#             return "C"
#         elif 60<self.percent<=70:
#             return "D"
#         elif 50<self.percent<=60:
#             return "E"
#         else:
#             return "F"

# percent1 = int(input("ENTER YOUR PERCENTAGE:"))
# percent2 = int(input("ENTER YOUR PERCENTAGE:"))
# percent3 = int(input("ENTER YOUR PERCENTAGE:"))
# obj1 = Student(percent1)
# obj2 = Student(percent2)
# obj3 = Student(percent3)
# print("YOUR GRADE:",obj1.Grade())
# print("YOUR GRADE:",obj2.Grade())
# print("YOUR GRADE:",obj3.Grade())
# -----------------------------------------------------------------------------------------------------------------------------------
# class Student:
#     def __init__(self,percent):
#         self.percent = percent

#     def Grade(self):
#         if 90<self.percent<=100:
#             return "A"
#         elif 80<self.percent<=90:
#             return "B"
#         elif 70<self.percent<=80:
#             return "C"
#         elif 60<self.percent<=70:
#             return "D"
#         elif 50<self.percent<=60:
#             return "E"
#         else:
#             return "F"

# obj1 = Student(95)
# obj2 = Student(78)
# obj3 = Student(42)
# print("YOUR GRADE:",obj1.Grade())
# print("YOUR GRADE:",obj2.Grade())
# print("YOUR GRADE:",obj3.Grade())