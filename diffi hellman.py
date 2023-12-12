from random import randint
if __name__=='__main__':
    P=23
    G=9
    print('the value of P is:%d'%(P))
    print('the value of G is:%d'%(G))
    a=4
    print('secret number for alice is :%d'%(a))
    x=int(pow(G,a,P))
    b=6
    print('secret number for bob is :%d'%(b))
    y=int(pow(G,b,P))
    ka=int(pow(y,a,P))
    kb=int(pow(x,b,P))
    print('secret key for the alice is:%d'%(ka))
    print('secret key for the bob is:%d'%(kb))
    
    
    
