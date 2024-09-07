z=eval(input("ENTE '1'FOR IN TERMS OF 10 & AND '2' FOR IN TERMS OF 100 "))
a=eval(input('ENTER THE ROUND OFFABLE NUMBER = '))
if z==1:
    b=a%10
    c=10-b
    if b>=5 :
        d=a+c
        print('THE NUMBER IS = ',d)
    else :
        e=a-b
        print('THE NUMBER IS = ',e)
else :
        b=a%100
        c=100-b
        if b>=50 :
            d=a+c
            print('THE NUMBER IS = ',d)
        else :
            e=a-b
            print('THE NUMBER IS = ',e)
