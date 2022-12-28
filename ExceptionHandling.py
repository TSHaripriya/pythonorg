##
def div(a1,b1):
    try:
        div=a1/b1
        print(div)
    except:
        print("Denomintor is zero")

a1=int(input())
b1=int(input())
div(a1,b1)

#
#def div(a1,b1):
try:
    a1 = int(input())
    b1 = int(input())
    div=a1/b1
    print(div)
except ZeroDivisionError:
    print("Denomintor is zero")
except ValueError:
    print("It is not a number")
