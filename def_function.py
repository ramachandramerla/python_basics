#square a number
def main():
    x=int(input("please provide the X value "))
    print("X Square is", square(x))

def square(n):
    print("the value is working only before the return value")
    return   n*n
    
main()


#finding the even or odd number
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

#def function additional content
# this is used to create a libraries
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
from index_content import goodbye
from index_content import hello

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


#finding the avg result
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

#add 2 number suing def function
def main():
    a=input()
    return a

def chandu(x):
    result= x + x 
    print(result)


chandu()
main()

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



#using MAP function changed the yell from list to String
def main():
    yell('this','is', 'cs50')

def yell(*words):
    uppercased=map(str.upper,words)
    print(*uppercased)


if __name__=="__main__":
    main() 

#enumurate    
students=['chandu', 'gowda','spoo']

for i, name in enumerate(students):
    print(i,name)


#this range will work on a limited range value
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