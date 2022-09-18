#q1
'''
myset={1,"Shubham",2,"shiva"}
it=iter(myset)
for i in it:
    print(i)
'''
#q2
'''
n=int(input("Enter the value of n "))  
def odd(start=1,end=n):
    start=1
    while True:
        if start<=end:
            yield start
        
        start+=2
        
    

for x in odd(1,n):
        print(x)
 '''
 #q3
'''
n=int(input("Enter the value of n "))  
def even(start=2,end=n):
    start=2
    while True:
        if start<=end:
            yield start
        
        start+=2
        
    

for x in even(2,n):
        print(x)
 
'''
#q4
'''
n=int(input("Enter the value of n "))  
def square(start=1,end=n):
    start=1
    while True:
        if start<=end:
            yield start*start
        
        start+=1
        
    

for x in square(1,n):
        print(x)
 
'''
#q5
'''
n=int(input("Enter the value of n"))
def fib(n):
    a=0
    b=1 
    
    for e in range(n):
        yield a
        a,b=b,a+b
print(list(fib(n)))
'''
#q6
'''
def isprime(num):
    for e in range(2,num):
        if num%e==0:
            return False
        return True

    
def primeg(n):
    num=2
    while n:
        if isprime(num):
            yield num
            n-=1
        num+=1
    return
n=int(input("Enter the value of n "))
it=primeg(n)
for e in it:
    print(e)
'''


        
        
 

    
    

