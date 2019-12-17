e1=e2=1
sum=1
i=1
n=int(input('n vlue:'))
x=float(input('x value:'))

while i<=n:
    e1=e1*x
    e2=e2*i
    print('{}'.format(e1/e2))
    sum=sum+(e1/e2)
    print('{}'.format(sum))
    i=i+1
print('')
print('{}'.format(sum))
