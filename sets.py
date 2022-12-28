#remove duplicate from list
list_a=[1,2,77,87,2]
set_a=set(list_a)
print(set_a)
#to print the numbers that are present in both lines
set_a={1,2,3,45,88}
set_b={22,45,7,98,9}
set_c=set_a  & set_b
print(set_c)

list_a=[9,8,6]
list_b=[5,8,3]
list_a=set(list_a)
list_b=set(list_b)
c=(list_a-list_b)
print(c)

#superset
list_a1=[1,5,8,9]
list_a2=[1,5,8,9]
set_a1=set(list_a1)
set_a2=set(list_a2)
is_superset=set_a1.issuperset(set_a2)
print(is_superset)

#subset
list_a1=[1,5,8,9,18,2]
list_a2=[1,5,8,9]
set_a1=set(list_a1)
set_a2=set(list_a2)
is_subset=set_a2.issubset(set_a1)
print(is_subset)

#disjoint
list_a1=[1,5,8,9]
list_a2=[1,5,81,92]
set_a1=set(list_a1)
set_a2=set(list_a2)
set_1=set_a1.isdisjoint(set_a2)
print(set_1)

#to print common elements in 3 sets
list_1=[1,2,3,4,5]
list_2=[88,9,3,97,66]
list_3=[2,3,7,1,88]
set1=set(list_1)
set2=set(list_2)
set3=set(list_3)
set4=set1&set2&set3
print(set4)

#4
list_1=["@","#",1,2,3,4,"*"]
list_2=[]
for i in range(len(list_1)):
    if str(i.isdigit()== True):
          list_2.append(i)
print(list_2)

##
list_a=[1,2,3,'@','#']
result=[val for val in list_a if isinstance(val,(int,float))]
print(result)

#max and min
tuple_a=(1,3,5,67)
print(max(tuple_a))
print(min(tuple_a))

#rotate the elements d times
l_a=list(map(int,input().split( )))
n=int(input())
for i in range(n):
    t=l_a[0]
    l_a.remove(t)
    l_a.append(t)
    print(l_a)
##nested list
lista=list(map(int,input().split(",")))
l1=int(input())
l2=[]
for i in range(len(l2)):
    for j in range(i+1,len(l2)):
        if(l2[i]+l2[j]==l1):
            l3=[l2[i],l2[j]]
            l2.append(l3)
print(l2)










