#sum of numbers
list_number=[10,20,30,40]
sum_number=0
for i in list_number:
    sum_number=sum_number+i
    i=i+1
print(sum_number)

number=[1,2,3,4,5,6]
sum_number=0
for i in number:
    sum_number=sum_number+i
    i=i+1
print(sum_number)
#natural numbers
n=int(input())
sum_number=0
natural_num=list(map(int,range(1,n+1)))
for i in natural_num:
    sum_number=sum_number+i
    i=i+1
print(sum_number)

#product numbers
number=list(map(int,input().split()))
product_number=1
for i in number:
    product_number=product_number*i
    i=i+1
print(product_number)
#solid square
size=int(input())
for i in range(size):
    for j in range(size):
        print("*",end=' ')
    print()
#right angle triangle
size=int(input())
for i in range(size):
    for j in range(i+1):
        print("*",end=' ')
    print()
#rectangle
size=int(input())
s=int(input())
for i in range(size):
    for j in range(s):
        print("*",end=' ')
    print()

#triangle
size=int(input())
for i in range(1,size+1):
    for j in range(i-1,size):
        print("*",end=' ')
    print()