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