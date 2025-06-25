# def add(x,y):
#     z=x+y
#     print("result is {}".format(z))
#     return z

# a=int(input("Enter number 1:"))
# b=int(input("Enter  number 2:"))
# print("Addition of {} and {} is {} ".format(a,b,add(a,b)))

#return multiple value

# def basic_math(x,y):
#     a=x+y
#     s=x-y
#     m=x*y
#     d=x/y
#                      # or r=(a,s,m,d) 
#     return (a,s,m,d)  #return(r)

# a=int(input("Enter number 1:"))
# b=int(input("Enter  number 2:"))
# print("basic math of {} and {} is {} ".format(a,b,basic_math(a,b)))

# separately printed

# def basic_math(x,y):
    # a=x+y
    # s=x-y
    # m=x*y
    # d=x/y
    # return (a,s,m,d)  

# a=int(input("Enter number 1:"))
# b=int(input("Enter  number 2:"))

# i,j,k,l=basic_math(a,b)

# print("basic math of {} and {} is {} ".format(a,b,basic_math(a,b)))

# print("Addition:",i)
# print("subtraction:",j)
# print("multipication:",k)
# print("division:",l)


# or print using loop

# def basic_math(x,y):
#     a=x+y
#     s=x-y
#     m=x*y
#     d=x/y
#     return {           #return in dictionary
#        "Addition":a,
#        "subtraction":s,
#        "multiplication":m , 
#        "division":d
#        }  

# a=int(input("Enter number 1:"))
# b=int(input("Enter  number 2:"))

# dic=basic_math(y=a,x=b) # by default a=x,b=y

# print("basic math of {} and {} ".format(a,b,))

# for i in dic.keys():
#     print("{} : {}" .format(i,dic[i]))


# def add (x,*y):  #  or (*y)
#                  #     x=0
#     print(x)
#     print(y)

#     r=0
#     r=r+x
#     for i in y:
#         r=r+i
#     return r

# print("Addition result:{}".format(add(1,2,3,4,5,6,7,8,9)))  #passing many values 

# output in dictionary

# def keywordargs(**kwargs):
#     print(kwargs)
#     return kwargs

# keywordargs(a=1,b=2,c="hello",d=2.5)
 
# another example

# def keywordargs(i,j,k,l=20,*x,**kwargs):
#     print(x)
#     print(kwargs)
#     print(l)
#     print(i)
#     return kwargs

# keywordargs(1,2,3,4,5,6,7,8,9,a=1,b=2,c="hello",d=2.5,)
 
#swapping program using function
def swap(x,y):
    return (y,x)

x=10
y=20

print("swapping {}".format (swap (x,y)))