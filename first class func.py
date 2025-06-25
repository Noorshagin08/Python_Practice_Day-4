#function inside another function

def create_adder(x):
    def adder(y):
        return x+y
    def subtract(y):
        return x-y
    return adder,subtract

add_40,sub_40=(create_adder(40)) # a function instance with x=40 is created and saved
print(add_40(100))
print(add_40(1000))
print(sub_40(100))
print(sub_40(1000))
