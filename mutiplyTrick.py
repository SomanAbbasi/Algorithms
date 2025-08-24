
def add(a,b):
    if b==0:
        return a
    return add(a+1,b-1)

def multiply(a,b):
    if b==0:
        return 0
    return add(a,multiply(a,b-1))



a=10
b=12
res=multiply(a,b)
print(res)