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
'''        
'''
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
