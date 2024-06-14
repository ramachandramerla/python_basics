#list comprehension
def main():
    yell('this','is', 'cs50')

def yell(*words):
    uppercased=[word.upper() for word in words]  #advance feature
    print(*uppercased)


if __name__=="__main__":
    main() 


#list comprehension bit more conditions

students=[{'name':'chandu','house':'cngalore'},
          {'name':'gowda','house':'ahandapura'},
          {'name':'chandu','house':'cngore'},]

result=[data['name'] for data in students if data['name']=='chandu']

print(result)
#for one below the other
for _ in result:
    print(_)


#list comprehension filter

students=[{'name':'chandu','house':'cngalore'},
          {'name':'gowda','house':'ahandapura'},
          {'name':'chandu','house':'cagore'},]


def is_chandu(c):
    return c['name']=='chandu'


place=filter(is_chandu,students)

for a in sorted(place,key=lambda x:x['house']):
    print(a['house'])


#dictionary comprehensions

students = ['chandu', 'gowda','spoo']

data = []

for i in students:
    data.append({'name':i , 'house':'bang'})


for i in data:
    print(i)


#different way for the above same code
#grop of dict
students = ['chandu', 'gowda','spoo']


data=[{'name':student, 'house':'bng'} for student in students]

for i in data:
    print(i)


#making a single dict
#dict compreshension

students=['chandu', 'gowda','spoo']

data={i:'bang' for i in students}

print(data)

students=['chandu', 'gowda','spoo']

for i in range(len(students)):
    print(i,students[i])

#if we need number should start from 1 then use i+1    
students=['chandu', 'gowda','spoo']

for i in range(len(students)):
    print(i+1,students[i])
