a=4
b=5
a=str(a)
l=[]
l=a*b
print(list(l))

m=input()
n=int(input())
p=m*n
print(list(p))

a1="ApPle"
b1="Application"
print(a1[:3]==b1[:3])

p1=input()
p2=input()
print(p1[0]<p2[2])

#and operator
m=int(input())
p=int(input())
c=int(input())
print((m>=70) and(p>=60) and (c>=60) and (m+p+c>=180))

#or operator
m=int(input())
p=int(input())
c=int(input())
print((m>=70) or (p>=60) or (c>=60) or (m+p+c>=180))

a="waterfall"
p=a[0:7:3]
print(p)
#lower
n=input()
print(n.lower())

#replace
a="dd-mm-yy"
a=a.replace("-","/")
print(a)

#swap
p="PyThon"
p=p.swapcase()
print(p)

#palindrome
a="pyttyp"
print(a[::-1]==a)


#To print the digit in the one's place
n=input()
print(n[-1])

#No of days(N) as input.To convert N to years,weeks,days.
N=int(input())
Y=N//365
M=(N-Y*365)//30
D=N-Y*365-M*30
print(Y)
print(M)
print(D)

#absolute difference
a=int(input())
b=int(input())
s=abs(a-b)
print(s)



