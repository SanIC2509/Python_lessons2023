a=int(input())
b=int(input())
if a/b-a//b >=0.1:
    print(a//b+1)
else:
    print(a/b)