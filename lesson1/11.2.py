s=int(input())
g=int(input())
if g>s:
    s=s+(g-s)
elif s>g:
    s=s-(s-g)
print(s)
