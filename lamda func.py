# y=(lambda x: x>3 )(5)    #def check (x)  return x>3
# print(y)

#purpose of lambda

def create_adder(x):
    def adder(y):
        return x+y
    def subtract(y):
        return x-y
    return adder,subtract

add_40,sub_40=(create_adder(40))

l=[100,200,1000,2000]
for i in l:
    print(add_40(i))
    print(sub_40(i))

print (list(map((lambda y : y+40),l)))  #using lambda funct
print(list(map(sub_40,l)))
 
 
#filter

print (list(filter((lambda x : x>=1000),l)))  #using lambda funct
    


