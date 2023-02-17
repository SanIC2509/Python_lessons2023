x1=1
x2=1
x3=x1+x2
for i in range(1,45):
    x1=x2
    x2=x3
    x3=x1+x2
    print(x1, x2, x3)