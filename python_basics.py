'''
# Day-1
# Input a variable and remove spaces  
name=input("What is your name ?").strip().capitalize().title()
#remove the spaces from the string inserted by the user
name=name.strip()
#first string Capital
name=name.capitalize()
#starting letter of every string is capital
name= name.title()
print("Hello",name)

#Day-2
# creating a define function to use anywhere within the code repetative times
def main():
    x=int(input("please provide the X value "))
    print("X Square is", square(x))

def square(n):
    print("the value is working only before the return value")
    return   n*n
    
main()

#Day-3 if , elif,else functions 
marks=int(input("Value of X : "))
if marks >=90:
    print("Distinction")
elif marks>=70:
    print("FC")
elif marks>=50:
    print("SC")
else:
    print ("Fail")

# Day -3 
# getting familir with the def function
def main():
    value=int(input("Give the Input value for the testing the def functions : "))
    if is_even(value) == True:
        print("Number is EVEN")
    else:
        print("Number is ODD")
# I created a function with in the program to use multiple times of the function "is_even"
def is_even(n):
    if n % 2==0:
        return True
    else:
        return False

main()

# match statement similar to the if elif else conditions.
name = input("give me the name : ")

match name:
    case "Cha" | "chw" | "che":  # case with or statement "|"
        print("Good")
    case "chh":
        print("Goodd")
    case _:
        print("Who???")

#Loops
# while loop
i=int(input("Give the number of times you want to loop : "))
j=int(input("Give the end number : "))
if i<j:
    while i<j:
        print("Done")
        i=i+1
else:
    print("I is greater than J")    

#while True if the while loop condition is true then it will break the loop and come out of the loop 
while True:
    n= int(input("Give me he number : "))
    if n>0:
        break
for _ in range(n):
    print("Tryeee")

# def function inside the for loop
def main():
    number = get_number()
    play(number)

def get_number():
    n=int(input("Give the number : "))
    return n

def play(n):
    for _ in range(n):
        print("Gooooooo")
main()    

# list which are in students list of the values to add in the rows by adding the 1st column

students=["Chan","Abhi","Chaaaaa","qpr","jar"]

for i in range(len(students)):
    print(i+1, students[i])

#Dict which are in the values defined below.

students = {
        "asda":"manvi",
        "dhdt": "hggg",
        "eetete":"sdr"}

print(students["asda"])
for student in students:
       print(student,students[student],sep=', ')

#Printing the number of rows and columns 
a = int(input("Number of Rows : "))
b = int(input("Number of Columns : "))
for i in range(a):
    for j in range(b):
        print("yes", end=' ')
       
    print()   

#importing all the modules inside the random  
import random
df = random.choice(["Gowda","Chandu","Test"])
print (df)

#importing a specific choice from the random module 
from random import choice
df = choice(["A","B","C","D"])
print (df)

#getting additional pic between 2 integers from the module random
import random
num = random.randint(1,100)
print (num)

#from the random library using the shuffle
import random

cards=["K","Q","J"]
random.shuffle(cards)
print (cards) #print in a single line
for i in cards: #using a for loop to get the shuffle data in rows
    print(i)

#module statistics getting familiar with the stats modules.
import statistics
df=statistics.mean([10,20])
print(df)


#command line arguments
#check for index error
#while running the code give the name after the file name to get the correct output 
#if you want to include the first name space and last name then use "" while executing the code.
import sys
if len(sys.argv)<2:
    print("less Arguments")
elif len(sys.argv)>2:
    print("Many arguments")
else:
    print("Hello, My Name is",sys.argv[1])        

#when we execute the same code with pnly if, elif and then indented print then we get the std output and along with that we get the index error 
#in order to avoid the index error we use sys.exit fucntion to get out of the execution and print the standard keywords

import sys

if len(sys.argv)<2:
    sys.exit("Less arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments") 

print("Hello,",sys.argv[1])
X
import sys

if len(sys.argv)<2:
    print("less arguments")
    sys.exit()
elif len(sys.argv) >2:
    print("Too many arguements")
    sys.exit()    

print("Hello :", sys.argv[1])
'''
'''
# working with APi and Requests
import sys
import requests
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=1&term=" + sys.argv[1])
print(response.json())    
'''
'''
#make a proper format for the api data we received
import sys
import requests
import json

if len(sys.argv)!=2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=2&term=" + sys.argv[1])
print(response.json())
#just printing as we have them in the API key and understand it is difficult to understand the data 
print("-----------------------------------------------------------------------------------------------")
print(json.dumps(response.json(), indent=2))
#using dumps creating a 2 spaces in the file representing 
print("----------------------------------------------------------------------------------------------------")
#if we need any specific things from the API like songs or something use below for loop and proper allignment in the file
o = response.json()
for result in o["results"]:
    print(result["trackName"], result["trackPrice"])
'''
'''
#def function additional content
# this is used to create a libraries 
# need to learn more on this one

def main():
    hello("a")
    goodbye("a")

def hello(name):
    print(f"Hello.............,{name}")

def goodbye(name):
    print(f"Bye.................................., {name}")

if __name__ == "__main__":
    main()

#create a new python file adding below content and write the below code to test the values for getting output
#creating a library
import sys
from python_basics import goodbye
from python_basics import hello

if len(sys.argv)==2:
    hello(sys.argv[1])
else:
    goodbye(sys.argv[1])
'''
'''
def chandu(x,y):
    result = x + y
    return result

a=int(input("give a 1st number "))
b=int(input("give a 2nd number "))

result = chandu(a,b)
print("printing outside the loop",result)
print("using direct call value",chandu(a,b))
'''
'''
def avg_marks(marks):
    sum_marks=sum(marks)
    print(sum_marks)
    total_marks=len(marks)
    print(total_marks)
    avg= sum_marks / total_marks
    return avg

marks=[10,20,30,40,50]

result=avg_marks(marks)

print(result)
'''
'''
def main():
    a=input()
    return a

def chandu(x):
    result= x + x 
    print(result)


chandu()
main()

#reverse a given number 
n=int(input())
sum=0
while (n > 0):
    digit=n%10
    sum = sum*10 + digit 
    n=n//10

print(sum)


#Assert 
#pytest -- Need to learn and used to test the test cases with out writing the print or return statements in the programme. 
#package

#file I/O

name=input("Give a Name: ")
print (f"Hello, {name}")

#Sort the given list
names=[]
for _ in range(3): names.append(input("Gave a Name: "))
print(names)
temp=[]
for i in sorted(names): 
    temp.append(i)
print(temp)   

#testing the Dev_A branch
'''
'''
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

import random

class Hat:
    def __init__(self):
        self.houses=['bangalore', 'Karnataka','Channasandra','Chandapura']

    def sort(self, name):
        print(name, "is in ",random.choice(self.houses))

hat = Hat()
hat.sort('Harry')        