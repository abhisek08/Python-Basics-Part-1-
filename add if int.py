def summation(a,b):
    if not isinstance(a,int) or not isinstance(b,int):
        raise TypeError("must be integers")
    return a+b
print(summation(12,'12'))