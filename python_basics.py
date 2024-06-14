#Index

#Function and Variable
#Conditionals
#Loops
#Exceptions
#Libraies
#Unit Tests
#File I/O
#Regular Expressions
#Object Oriented Programming
#Et cetera


#Open how to create a file and write something in the file created

names = input()

file=open("test.txt","a") #a is used to append the content
file.write(f"{names} \n")
file.close

#Open a file which you have saved above and then pass a arg 
#once the file is created then open it using the code.
#if we want to add the default arguments

names = []

with open("test.txt") as file:
    for i in file:
        names.append(i)


for name in (names):
    print(f"Hello {name}",end="")
'''
"""student=[]
with open("student.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student.append(f"{name} is in {house}")

for i in sorted(student):
    print(i)
"""
"""students=[]

with open("student.csv") as file:
    for line in file: 
        name,city=line.rstrip().split(",") 
        stnd = {"name": name,"city": city}
        students.append(stnd)


for i in stnd:
    print(i)"""

'''
# importing a csv file to read easily when we have a other delimiter in the text
#other ways to print the dta we have
import csv

students=[]

with open("student.csv") as file:
    reader=csv.reader(file)
    for name,home in reader:
        students.append({"name":name,"home":home})

for student in sorted(students,key=lambda student: student ["name"]):
    print(f'{student["name"]} is in {student["home"]}') 
           

#Using the DictReader
#this will work even columns are interchanged this is used to read the file

import csv

students=[]

with open("student.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        students.append({"name":row["name"],"home":row["home"]})

for student in sorted(students,key=lambda student: student ["name"]):
    print(f'{student["name"]} is in {student["home"]}')
         

#using the DictWriter to update the CSV file
import csv

name=input("input a name: ")
home=input("input a house: ")

with open("student.csv",'a') as file:
    writer= csv.DictWriter(file, fieldnames=["name","home"])
    writer.writerow({"name":name, "home":home})
    '''
'''
#creating a Gif's using "arg"
#import image and take 2 images and combine them with a 200 millisec to make a Gif 
import sys

from PIL import Image

images=[]

for arg in sys.argv[1:]:
    image=image.open(arg)
    images.append(image)

images[0].save(
    "costumes.gif", save_all=True, append_images=[image[1]],duration=200, loop=0)
'''
"""#Regular Expressions:
#re.split, re.refill, re.search, re.sub. prefix, re.replace
#regexes
"""
"""#without regex functions
email=input("Give Email Id to validate: ")

if '@' in email and "." in email:
    print("Valid")
else:
    print("invalid")    """

"""
#Syntax for Regex
#re.search(pattern, string,flags=0)
email=input("Give Email Id to validate: ").rstrip() #remove the spaces beginning and end

username,domain=email.split("@") # split the value with the keyword @
print(f'{username},{domain}')
if username and domain.endswith(".com"):
    print("Valid")
else:
    print("invalid")    
"""
"""
#object oriented programming

#basic example of the def functions
#writing the if __name__=="__main__" is nothing but of creating a module or library

def main():
    name=get_name()
    house=get_house()
    print(f"{name} is in {house}")


def get_name():
    return input("Name : ")

def get_house():
    return input("House : ")

if __name__=="__main__":
    main()
    """
"""
#list based def function
def main():
    student = get_student()
    if student[0]=="gowda":
        student[1]="hikeeee"
    print(f"{student[0]} is in {student[1]}")

def get_student():
    name=input("Name: ") 
    House=input("House: ")
    return [name,House]
#if we use retun (name,House) this is a tuple and immutable

if __name__=="__main__":
    main()
"""
"""#CLASSES
#OBJECTS
#instance variable
#methods
#raise for exceptions
#__str__


class Student:
    def __init__(self,name,house):
        if not name:  # or if name==""
            raise ValueError("Missing Name")
        if house not in ["bng","cha","aaa"]:
            raise ValueError("Incorrect Place/house")
        self.name = name 
        self.house = house
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
        

def main():
    student=get_student()
    print(f"{student.name} is from {student.house}")

def get_student():
    name=input("Name: ")
    house=input("House: ")
    student=Student(name,house)
    return student
 

if __name__=="__main__":
    main()
"""
"""
class Student:
    def __init__(self,name,house,patronus):
        if not name:  
            raise ValueError("Missing Name")
        if house not in ["bng","cha","aaa"]:
            raise ValueError("Incorrect Place/house")
        self.name = name 
        self.house = house
        self.patronus = patronus
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
    def charm(self):
        if self.patronus=="stag":
            return "cha"
        elif self.patronus=="ccc":
            return "ccc"
        else:
            return "everythins is working fine"


        

def main():
    student=get_student()
    print(f"{student.name} is from {student.house}")
    print("Horreyyy")
    print(student.charm())


def get_student():
    name=input("Name: ")
    house=input("House: ")
    patronus=input("patronus: ")
    student=Student(name,house,patronus)
    return student
 

if __name__=="__main__":
    main()
"""
"""
class Student:
    def __init__(self,name,house):
        if not name:  
            raise ValueError("Missing Name")
        if house not in ["bng","cha","aaa"]:
            raise ValueError("Incorrect Place/house")
        self.name = name 
        self.house = house
    
    def __str__(self):
        return f"{self.name} is from {self.house}"
    
def main():
    student=get_student()
    print(student)
    #print(f"{student.name} is from {student.house}") #both will work fine above and below
    


def get_student():
    name=input("Name: ")
    house=input("House: ")
    student=Student(name,house)
    return student
 

if __name__=="__main__":
    main()

    """

'''
#everything that we study is a aclass which is created by someone
print(type(50))
print(type("Hello world"))'''


"""#class method below is the one way
import random

class Hat:
    def __init__(self):
        self.houses=['bangalore', 'Karnataka','Channasandra','Chandapura']

    def sort(self, name):
        print(name, "is in ",random.choice(self.houses))

hat = Hat()
hat.sort('Harry')        
"""'''
#class method using the creation of the variables

import random

class Hat:
    houses =['bangalore', 'Karnataka','Channasandra','Chandapura'] #directly create a variable houses and use within the class 

    @classmethod
    def sort(cls,name):
        print(name, "is in ", random.choice(cls.houses))

#instead a creating one more variable use directly Hat
Hat.sort("Chandu")        
'''
'''
class vault:
    def __init__(self,party=0,party2=0,party3=0):
        self.party=party
        self.party2=party2
        self.party3=party3

    def __str__(self):
        return f'{self.party} "gowda", {self.party2} "chandu", {self.party3} "cha'


print(vault()) #if we dont give the values it taked default as o as defined above in the classs
print(vault(10,20,30)) #if we give the values then it will take the values that we defined
'''       
'''
students=[{'name':'chandu','house':'cngalore'},
          {'name':'gowda','house':'ahandapura'}]

houses=[]
for i in students:
    if i['house'] not in houses:
        houses.append(i["house"])


for hous in sorted(houses):
    print(hous)

'''
'''
#Global Variable Declaration use  the "global" keyword for defining outside the main function

balance=0

def main():
    print("Initial Balance is : ",balance)
    x=int(input("Deposit Amount : "))
    y=int(input("WithDraw amount : "))
    deposit(x)
    withdraw(y)
    print("Final Balance : ", balance)



def deposit(n):
    global balance
    balance = balance + n

def withdraw(n):
    global balance
    balance = balance - n

if __name__=="__main__":
    main()
'''
'''
#constants

class Cat:
    MEOW=3

    def meow(self):
        for _ in range(Cat.MEOW):
            print("Yup")


#cat=Cat
#cat.meow() or
Cat().meow()
'''
'''
#argpharse

#unpacking
first, _=input("What's your Name: ").split(" ")
print(f"your first name is {first}")'''
'''
#use a * in the code to assign in the specific place

def names(chandu,gowda,cha,gow):
    return (chandu*10+gowda*20)*20+cha*10+gow*12

coin = [10,40,20,30]

print(names(*coin),"total value-1")  

# using 2 ** for these as we have coin variable is a dict
def names(chandu,gowda,cha,gow):
    return (chandu*10+gowda*20)*20+cha*10+gow*12

coin ={'chandu':10,'gowda':40,'cha':20,'gow':30}

print(names(**coin),"total value-2")
'''
'''# *args , **kwargs

#most important as we can insert any number of values no specific restriction

#*args returns a list of values defined
def name(*args,**kwargs):
    print("names are : ",args)

name(10,20,30,'chandu','gowda')    

#**kwargs returns a dict of objects as defined

def name(*args,**kwargs):
    print("names are",kwargs)

name(chandu=20,gowda=30)    
'''
'''
def main():
    yell(['this','is', 'cs50'])

def yell(words):
    uppercased=[]
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)    # start (*) used for considering all the values in the list


if __name__=="__main__":
    main()   

'''
'''
#using MAP function changed the yell from list to String
def main():
    yell('this','is', 'cs50')

def yell(*words):
    uppercased=map(str.upper,words)
    print(*uppercased)


if __name__=="__main__":
    main() 
'''
'''
#list comprehension
def main():
    yell('this','is', 'cs50')

def yell(*words):
    uppercased=[word.upper() for word in words]  #advance feature
    print(*uppercased)


if __name__=="__main__":
    main() 
'''
'''

#list comprehension bit more conditions

students=[{'name':'chandu','house':'cngalore'},
          {'name':'gowda','house':'ahandapura'},
          {'name':'chandu','house':'cngore'},]

result=[data['name'] for data in students if data['name']=='chandu']

print(result)
#for one below the other
for _ in result:
    print(_)
'''

'''
#list comprehension filter

students=[{'name':'chandu','house':'cngalore'},
          {'name':'gowda','house':'ahandapura'},
          {'name':'chandu','house':'cagore'},]


def is_chandu(c):
    return c['name']=='chandu'


place=filter(is_chandu,students)

for a in sorted(place,key=lambda x:x['house']):
    print(a['house'])
'''

'''
#dictionary comprehensions

students = ['chandu', 'gowda','spoo']

data = []

for i in students:
    data.append({'name':i , 'house':'bang'})


for i in data:
    print(i)
'''
'''
#different way for the above same code
#grop of dict
students = ['chandu', 'gowda','spoo']


data=[{'name':student, 'house':'bng'} for student in students]

for i in data:
    print(i)
'''
'''
#making a single dict
#dict compreshension

students=['chandu', 'gowda','spoo']

data={i:'bang' for i in students}

print(data)'''
'''
students=['chandu', 'gowda','spoo']

for i in range(len(students)):
    print(i,students[i])
'''
'''#if we need number should start from 1 then use i+1    
students=['chandu', 'gowda','spoo']

for i in range(len(students)):
    print(i+1,students[i])'''
    
'''#enumurate    
students=['chandu', 'gowda','spoo']

for i, name in enumerate(students):
    print(i,name)
'''
'''
#generators

x=int(input("give the range value: "))

for i in range(x):
    print("*"*i)
    '''

'''#this range will work on a limited range value
def main():
    n=int(input("give a range: "))
    for s in sheep(n):
        print(s)

def sheep(n):
    flock=[]
    for i in range(n):
        flock.append("*"*i)
    return flock
               

if __name__=="__main__":
    main()    
'''

'''
#if we use the yield function any number of values can be generated
#yield
def main():
    n=int(input("give a range: "))
    for s in sheep(n):
        print(s)

def sheep(n):
    for i in range(n):
        yield ("*"*i)
               

if __name__=="__main__":
    main()    '''
