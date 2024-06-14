
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

import sys
if len(sys.argv)<2:
    print("less Arguments")
elif len(sys.argv)>2:
    print("Many arguments")
else:
    print("Hello, My Name is",sys.argv[1])    


