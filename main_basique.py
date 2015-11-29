from Complexe import *

def main_basique():
    
    print('INIT et GETTER SETTER')
    print('A DEVIENT EST CARTESIEN')
    a=Complexe(0,0,1)
    print("a.cartesien : ",a.cartesien)
    print("a.polaire : ",a.polaire)
    print("a.isCartesien : ",a.isCartesien)
    print("a.isPolaire : ",a.isPolaire)

    print('A DEVIENT I+1')
    a.reel=1
    a.imag=1
    print("a.reel=1; a.reel : ",a.reel)
    print("a.imag=1; a.imag : ",a.imag)
    print('pi/4 : ', pi/4)
    print('sqrt(2) : ',sqrt(2))
    print("a.cartesien : ",a.cartesien)
    print("a.polaire : ",a.polaire)

    print('MODULE DEVIENT 1')
    a.module=1
    print("a.cartesien : ",a.cartesien)
    print("a.polaire : ",a.polaire)

    print('argument DEVIENT pi/2')
    a.argument=pi/2
    print("a.cartesien : ",a.cartesien)
    print("a.polaire : ",a.polaire)
    
    print()

    #TESTS
    print('TESTS')
    print('Cartesien : ')
    a=Complexe(1,2,True)
    b=Complexe(1,2,True)
    c=Complexe(1,1,True)
    print('a : ',a)
    print('b : ',b)
    print('c : ',c)
    print('a==b : ',a==b)
    print('a==c : ',a==c)
    print('a<b : ',a<b)
    print('c<a : ',c<a)

    print('Polaire : ')
    a=Complexe(1.0,pi/4,0)
    b=Complexe(2,pi/4,0)
    c=Complexe(2,pi/2,0)
    print('a==b : ',a==b)
    print('a==c : ',a==c)
    print('a<b : ',a<b)
    print('c<a : ',c<a)

    print()
    
    #ADDITION:
    print('ADDITION')
    print('Cartesien  ')
    a=Complexe(1,2,True)
    b=Complexe(1,2,True)
    print('a : ',a)
    print('b : ',b)
    print('a+b :',a+b)

    print('Polaire  ')
    a=Complexe(2,pi/2,False)
    b=Complexe(2,pi/4,0)
    print('a : ',a)
    print('b : ',b)
    print('a+b : ',a+b)

    print()

    #MULTIPLICATION
    print('MULTIPLICATION')
    print('Cartesien  ')
    a=Complexe(1,1,True)
    b=Complexe(1,1,True)
    print('a : ',a)
    print('b : ',b)
    print('a*b : ',a*b)
    a=Complexe(1,2,True)
    b=Complexe(1,2,True)
    print('a : ',a)
    print('b : ',b)
    print('a*b : ',a*b)
    
    print('Polaire  ')
    a=Complexe(1,pi/2,0)
    b=Complexe(2,pi/4,0)
    print('a : ',a)
    print('b : ',b)
    print('3pi/4 : ',3*pi/4)
    print('a*b : ',a*b)

    print()

    #OPPOSE
    print('OPPOSE')
    print('Cartesien : ')
    a=Complexe(-3,0,True)
    print('a : ',a)
    print('a.oppose : ',a.oppose)
    print('a.cartesien : ',a.cartesien)
    print('a.polaire : ',a.polaire)
    print('a.oppose.cartesien : ',a.oppose.cartesien)
    print('a.oppose.polaire : ',a.oppose.polaire)

    print('Polaire : ')
    a=Complexe(2,pi,0)
    print('a : ',a)
    print('a.oppose : ',a.oppose)
    print('a.cartesien : ',a.cartesien)
    print('a.polaire : ',a.polaire)
    print('a.oppose.cartesien : ',a.oppose.cartesien)
    print('a.oppose.polaire : ',a.oppose.polaire)

    print()

    #INVERSE
    print('INVERSE')
    print('Cartesien ')
    a=Complexe(1,1,1)
    print('a : ',a)
    print(a.inverse)
    
    print('Polaire ')
    a=Complexe(2,2*pi/3,0)
    print('a : ',a)
    print(a.inverse)

    print()
    
    #CONJUGUE
    print('CONJUGUE')
    print('Cartesien')
    a=Complexe(1,2,1)
    print('a : ',a)
    print(a.conjugue)

    print('Polaire')
    a=Complexe(1,5*pi/6,0)
    print('a : ',a)
    print(a.conjugue)

    print()

    #VALEUR ABSOLUE
    print('VALEUR ABSOLUE')
    print('Cartesien')
    a=Complexe(1,1,1)
    print('a : ',a)
    print(abs(a))
    print(sqrt(0.5))
    print(abs(a.inverse))

    print('Polaire')
    a=Complexe(87,pi/3,0)
    print('a : ',a)
    print(abs(a))

    print()
    
    #SOUSTRACTION
    print('SOUSTRACTION')
    print('Cartesien')
    a=Complexe(1,1,1)
    b=Complexe(1,-3,1)
    print('a : ',a)
    print('b : ',b)
    print('a-b : ',a-b)
    
    print('Polaire')
    a=Complexe(sqrt(2),pi/4,0)
    b=Complexe(1,pi/2,0)
    print('a : ',a)
    print('b : ',b)
    print('a-b : ',a-b)
    
    print()
    
    #DIVISION
    print('DIVISION')
    print('Cartesien: ')
    a=Complexe(1,1,1)
    print('a : ',a)
    print('a/a : ',a/a)
    
    print('Polaire : ')
    a=Complexe(42,pi/2,0)
    b=Complexe(2,pi/4,0)
    print('a : ',a)
    print('b : ',b)
    print('pi/4 ',(pi/4))
    print('a/b : ',a/b)

    print()

    #PUISSANCE ENTIERE
    print('PUISSANCE ENTIERE')
    print('Cartesien')
    a=Complexe(1,1,1)
    print('a : ',a)
    print('a**2 : ',a**2)
    print('a**3 : ',a**3)
    print('a**4 : ',a**4)

    print('Polaire')
    a=Complexe(1,pi,0)
    print('a : ',a)
    print('a**2 : ',a**2)
    print('a**3 : ',a**3)
    print('a**4 : ',a**4)

    print()

    #CHERCHE DANS LISTE DE COMPLEXES
    print('CHERCHE')
    l=[Complexe(i,j,1) for i in range(2) for j in range(5)]
    print(l)
    print()
    g=[Complexe(i,j,0) for i in range(2) for j in range(5)]
    print(g)
    a=Complexe(1,4,1)
    print('a : ',a)
    print('a.find(l) : ',a.find(l))
    print('a.find(g) : ',a.find(g))
    a=Complexe(1,4,0)
    print('a : ',a)
    print('a.find(g) : ',a.find(g))

    print()

    #TRI LISTE DE COMPLEXES
    print('TRI LISTE')
    print('Cartesien')
    print('Liste:')
    y=[Complexe(1,1,1),Complexe(2,1,1),Complexe(1,3,1)]
    print(y)
    r=tri(y)
    print('tri de la liste')
    print(r)
    print()
    print('Nouvelle liste:')
    u=[Complexe(1,1,1),Complexe(2,1,1),Complexe(1,3,1)]*3
    print(u)
    o=tri(u)
    print('tri de la liste')
    print(o)
    print()
    
    print('Polaire')
    print('Nouvelle liste:')
    g=[Complexe(1,pi/4,0),Complexe(2,pi/4,0),Complexe(1,pi,0)]
    print(g)
    h=tri(g)
    print('tri de la liste')
    print(h)
    print()
    print('Nouvelle liste:')
    q=[Complexe(1,pi/4,0),Complexe(2,pi/4,0),Complexe(1,pi,0)]*3
    print(q)
    j=tri(q)
    print('tri de la liste')
    print(j)

    print()


    a=Complexe(1,4*pi,0)
    b=Complexe(1,-10*pi,0)
    print('a : ',a)
    print('b : ',b)
    print('a==b :',a==b)

    a=Complexe(1,1,1)
    b=Complexe(sqrt(2),pi/4+1000*pi,0)
    print('a : ',a)
    print('b : ',b)
    print('a==b :',a==b)

       
