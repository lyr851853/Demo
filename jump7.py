for i in range(0,100):
    i=i+1
    if i%7==0:
        continue
    elif i%10==7:
        continue
    elif i//10==7:
        continue
    print('{}'.format(i))
