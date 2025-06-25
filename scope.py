x=5
def set_x(num):
    x=num
    print(x)  #second 43 [life cycle only this block]
    

def set_global_x(num): 
    global x
    print(x) #fourth fetch global value 5
    x=num
    print(x)  #fifth 6
 
print(x)   # first x=5
set_x(43)
print(x)    #third 5
set_global_x(6)
print(x)    #seventh 6 [out of global fuction output same value 6 ,can't modified because of mentioned (global)]
set_x(30)    #eighth 30
print(x)      #ninth 6
