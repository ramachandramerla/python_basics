#CLASSES
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


#class method below is the one way
import random

class Hat:
    def __init__(self):
        self.houses=['bangalore', 'Karnataka','Channasandra','Chandapura']

    def sort(self, name):
        print(name, "is in ",random.choice(self.houses))

hat = Hat()
hat.sort('Harry')        

#class method using the creation of the variables

import random

class Hat:
    houses =['bangalore', 'Karnataka','Channasandra','Chandapura'] #directly create a variable houses and use within the class 

    @classmethod
    def sort(cls,name):
        print(name, "is in ", random.choice(cls.houses))

#instead a creating one more variable use directly Hat
Hat.sort("Chandu")

class vault:
    def __init__(self,party=0,party2=0,party3=0):
        self.party=party
        self.party2=party2
        self.party3=party3

    def __str__(self):
        return f'{self.party} "gowda", {self.party2} "chandu", {self.party3} "cha'


print(vault()) #if we dont give the values it taked default as o as defined above in the classs
print(vault(10,20,30)) #if we give the values then it will take the values that we defined


#constants

class Cat:
    MEOW=3

    def meow(self):
        for _ in range(Cat.MEOW):
            print("Yup")


#cat=Cat
#cat.meow() or
Cat().meow()


