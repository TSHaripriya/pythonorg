##return an argyment
def argument(arg1):
    return arg1
arg1=argument("Hello")
##return argument
def argument():
    print("Hari")
argument()

##concatenate
def arg1(a1):
    return a1
def arg2(a2):
    return a2
a1=arg1("welcome")
a2=arg2("HCL")
print(a1+a2)

##3
def arg1():
    n=(1,2,3,4)
    for i in n:
        i=i*i
        print(i,end=" ")
arg1()

##4
def division(n):
    if(n%7==0):
        print("True")
    else:
        print("False")
n=int(input())
division(n)

##
def fun(a):
    if(a%3==0 and a%5!=0):
        print("Macro")
    elif(a%5==0 and a%3!=0):
        print("Polo")
    elif(a%3==0 and a%5==0):
        print("MacroPolo")
    else:
        print("no")
a=int(input())
fun(a)

##
def fun(a):
    lower=0
    upper=0
    for i in a:
        if not(ord(i)>=65 and ord(i)<=90 or ord(i)>=97 and ord(i)<=122):
            print("Invalid string")
        elif i.isupper():
            upper+=1
        else:
            lower+=1
    return upper,lower
a=input()
upper,lower=fun(a)
print(upper)
print(lower)
