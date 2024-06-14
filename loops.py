#if else if 
marks=int(input("Value of X : "))
if marks >=90:
    print("Distinction")
elif marks>=70:
    print("FC")
elif marks>=50:
    print("SC")
else:
    print ("Fail")


# match statement similar to the if elif else conditions.
name = input("give me the name : ")

match name:
    case "Cha" | "chw" | "che":  # case with or statement "|"
        print("Good")
    case "chh":
        print("Goodd")
    case _:
        print("Who???")


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


#printing a for loop
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

import sys

if len(sys.argv)<2:
    sys.exit("Less arguments")
elif len(sys.argv)>2:
    sys.exit("Too many arguments") 

print("Hello,",sys.argv[1])

import sys

if len(sys.argv)<2:
    print("less arguments")
    sys.exit()
elif len(sys.argv) >2:
    print("Too many arguements")
    sys.exit()    

print("Hello :", sys.argv[1])

#reverse a given number 
n=int(input())
sum=0
while (n > 0):
    digit=n%10
    sum = sum*10 + digit 
    n=n//10

print(sum)


#file I/O

name=input("Give a Name: ")
print (f"Hello, {name}")

#Sort the given list using functions
names=[]
for _ in range(3): names.append(input("Gave a Name: "))
print(names)
temp=[]
for i in sorted(names): 
    temp.append(i)
print(temp)   


#loops and printing based on the sorting techniquies
students=[{'name':'chandu','house':'cngalore'},
          {'name':'gowda','house':'ahandapura'}]

houses=[]
for i in students:
    if i['house'] not in houses:
        houses.append(i["house"])


for hous in sorted(houses):
    print(hous)


#generators
x=int(input("give the range value: "))

for i in range(x):
    print("*"*i)

