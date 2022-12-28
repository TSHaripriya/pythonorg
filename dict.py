##update value of particular key
dict_a={
    'name':'Hari',
    'age': 20
}
dict_a['name']='Priya'
print(dict_a)

##remove a key
dict_b={
    'name':'Hari',
    'age':20,
    'address':'s.konda'
}
del dict_b['age']
print(dict_b)

##4
dict_b=dict()
n=int(input())
for i in range(n):
    dict_b[i]=i**2
print(dict_b)

###7
dict_b=dict()
n=int(input())
p=int(input())
for i in range(n,p):
    dict_b[i]=i**2
print(dict_b)

##
m=int(input())
n=int(input())
matrix=[]
for i in range(m):
    row=input().split()
    for j in row:
        matrix.append(j)
list_a=matrix.sort()
print(matrix)








