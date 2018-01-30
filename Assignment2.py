# Assignment #2 (Functions)
## Python for Informatics
## Scott Warnock


def to_number(str):
    x = int(str)
    return x

def add_two(n1,n2):
    add = n1 + n2
    return add
   
def cube(n):
    cube = n**3
    return cube
    
x1 = '2'

x2 = '3'

n1 = to_number(x1)

n2 = to_number(x2)

n = add_two(n1,n2)

print cube(n)