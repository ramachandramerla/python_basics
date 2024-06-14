
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


student=[]
with open("student.csv") as file:
    for line in file:
        name,house=line.rstrip().split(",")
        student.append(f"{name} is in {house}")

for i in sorted(student):
    print(i)

students=[]

with open("student.csv") as file:
    for line in file: 
        name,city=line.rstrip().split(",") 
        stnd = {"name": name,"city": city}
        students.append(stnd)


for i in stnd:
    print(i)

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
