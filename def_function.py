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



