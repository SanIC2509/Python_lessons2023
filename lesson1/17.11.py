a=int(input())
if 10<=a<=20:
    print(str(a) + " стульев")
elif a%10==1:
    print(str(a)+ " стул")
elif a==0:
    print(str(a) + " стульев")
elif 2<=a%10<=4:
    print(str(a) + " стула")
elif 5<=a%10<=9:
    print(str(a) + " стульев")
elif a%10==0:
    print(str(a) + " стульев")