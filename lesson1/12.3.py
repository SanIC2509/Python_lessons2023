a=int(input())
b=int(input())
c=int(input())
if b>a>c:
    print(str(c) + str(a) + str(b))
elif b>c>a:
    print(str(a) + c + b)
elif c>a>b:
    print("b " + "a " + "c")
elif c>b>a:
    print("a " + "b " + "c")
elif a>b>c:
    print("c " + "b " + "a")
elif a>c>b:
    print("b " + "c " + "a")