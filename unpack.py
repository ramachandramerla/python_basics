#argpharse

#unpacking
first, _=input("What's your Name: ").split(" ")
print(f"your first name is {first}")

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

# *args , **kwargs

#most important as we can insert any number of values no specific restriction

#*args returns a list of values defined
def name(*args,**kwargs):
    print("names are : ",args)

name(10,20,30,'chandu','gowda')    

#**kwargs returns a dict of objects as defined

def name(*args,**kwargs):
    print("names are",kwargs)

name(chandu=20,gowda=30)    


def main():
    yell(['this','is', 'cs50'])

def yell(words):
    uppercased=[]
    for word in words:
        uppercased.append(word.upper())
    print(*uppercased)    # start (*) used for considering all the values in the list


if __name__=="__main__":
    main()   