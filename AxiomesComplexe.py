# ==============================================================================
"""Axiomes pour Complexe"""
# ==============================================================================
__author__ = "marie perez et charlotte rodriguez"
__date__ = "20.10.15"
__version__ = "4.0"
# ------------------------------------------------------------------------------
from math import *
import random
from Complexe import *
from ezCLI import * 
# ------------------------------------------------------------------------------
class myVars(object):
    """ defini un certain nombre de variables utiles pour plusieurs axiomes """
    def __init__(self):
        self.f1=round(random.uniform(-10,10),10) #cartesiens
        self.s1=round(random.uniform(-10,10),10)
        self.f2=round(random.uniform(-10,10),10)
        self.s2=round(random.uniform(-10,10),10)
        self.f3=round(random.uniform(-10,10),10)
        self.s3=round(random.uniform(-10,10),10)
        
        self.f4=round(random.uniform(0,10),10) #polaires
        self.s4=round(random.uniform(-10,10),10)
        self.f5=round(random.uniform(0,10),10)
        self.s5=round(random.uniform(-10,10),10)
        self.f6=round(random.uniform(0,10),10)
        self.s6=round(random.uniform(-10,10),10)

        self.f7=round(random.uniform(1,10),10)
        self.s7=round(random.uniform(1,10),10)
        self.f8=round(random.uniform(1,10),10)
        self.s8=round(random.uniform(0,pi/2),10)
        
        self.n=random.randint(0,10)
        
        self.zCart=Complexe(self.f1,self.s1,1) #un complexe cartesien
        self.zCart2=Complexe(self.f2,self.s2,1) #un autre complexe cartesien
        self.zCart3=Complexe(self.f3,self.s3,1) #un autre complexe cartesien
        
        self.zPol=Complexe(self.f4,self.s4,0) #un complexe polaire
        self.zPol2=Complexe(self.f5,self.s5,0) #un autre complexe polaire
        self.zPol3=Complexe(self.f6,self.s6,0) #un autre complexe polaire
        
        self.zR=Complexe(self.f1,0,1) #un complexe reel
        self.zIm=Complexe(0,self.s1,1) #un complexe imaginaire pur

        self.zPos=Complexe(self.f7,self.s7,1) #un complexe cartesien strictement positif
        self.zPosPol=Complexe(self.f8,self.s8,0) #un complexe polaire strictement positif

        self.zUn=Complexe(1,0,0) # 1
        self.zI=Complexe(0,1,1) # i
        self.zZero=Complexe(0,0,1) # 0
# --------------------------------------------------------------------------
def axiome_init():
    """
    """
    v=myVars()

    print('\n\nAXIOME_INIT')

    print('Pour un complexe cartesien :')
    z=Complexe(v.f1,v.s1,1)
    _=""
    _+="%r "%(z.reel==v.f1)
    _+="%r "%(z.imag==v.s1)
    _+="%r "%(z.isCartesien==1)
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    z=Complexe(v.f4,v.s4,0)
    _+="%r "%(z.module==v.f4)
    _+="%r "%(round(abs(z.argument-v.s4%(2*pi)),9)==0)   
    _+="%r "%(z.isCartesien==0)
    print(_+"\n");_=""
    print('Pour un complexe cartesien : par defaut')
    z=Complexe(v.f1,v.s1)
    _+="%r "%(z.isCartesien==1)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_maj_polaire():
    """
    """
    print('\n\nAXIOME_MAJ_POLAIRE')
    v=myVars()
    f=v.f1
    s=v.s1

    print('LE MODULE')

    print('Pour un complexe cartesien :')
    z1=v.zCart;z2=v.zCart2
    _=""
    _+="%r "%(z1.module == z1.oppose.module == z1.conjugue.module == z1.oppose.conjugue.module)
    _+="%r "%(round(v.zCart.module,9)==round(sqrt(v.zCart.reel**2+v.zCart.imag**2),9))
    _+="%r "%(round((z1*z2).module,9)==round(z1.module*z2.module,9))
    _+="%r "%(round((z1**v.n).module,9)==round((z1.module)**v.n,9))
    _+="%r "%(round(v.zPos.inverse.module,9)==round(1/v.zPos.module,9))
    _+="%r "%(round((z1/v.zPos).module,9)==round(z1.module/v.zPos.module,9))
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    z1=v.zPol;z2=v.zPol2
    _+="%r "%(z1.module == z1.oppose.module == z1.conjugue.module == z1.oppose.conjugue.module)
    _+="%r "%(round(v.zCart.module,9)==round(sqrt(v.zCart.reel**2+v.zCart.imag**2),9))
    _+="%r "%(round((z1*z2).module,9)==round(z1.module*z2.module,9))
    _+="%r "%(round((z1**v.n).module,9)==round((z1.module)**v.n,9))
    _+="%r "%(round(v.zPosPol.inverse.module,9)==round(1/v.zPosPol.module,9))
    _+="%r "%(round((z1/v.zPosPol).module,9)==round(z1.module/v.zPosPol.module,9))
    print(_+"\n");_=""
    
    print("L'ARGUMENT")
    _+="%r "%(v.zR.argument%pi==0 or v.zR==v.zZero)
    _+="%r "%(v.zIm.argument%(pi/2)==0 or v.zR==v.zZero)
    print(_+"\n");_=""
    print('Pour un complexe cartesien :')
    z1=v.zCart;z2=v.zCart2
    _+="%r "%(round(z1.oppose.argument,9)==round((z1.argument+pi)%(2*pi),9))
    _+="%r "%(round(z1.conjugue.argument,9)==round(-z1.argument%(2*pi),9))
    _+="%r "%(round((z1*z2).argument,9)==round((z1.argument+z2.argument)%(2*pi),9))
    _+="%r "%(round((z1**v.n).argument,9)==round((v.n*z1.argument)%(2*pi),9))
    _+="%r "%(round(v.zPos.inverse.argument,9)==round((-v.zPos.argument)%(2*pi),9))
    _+="%r "%(round((z1/v.zPos).argument,9)==round((z1.argument-v.zPos.argument)%(2*pi),9))
    _+="%r "%(round(z1.oppose.argument,9)==round((pi+z1.argument)%(2*pi),9))
    _+="%r "%(round(z1.conjugue.argument,9)==round((-z1.argument)%(2*pi),9))
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    z1=v.zPol;z2=v.zPol2
    _+="%r "%(round(z1.oppose.argument,9)==round((z1.argument+pi)%(2*pi),9))
    _+="%r "%(round(z1.conjugue.argument,9)==round(-z1.argument%(2*pi),9))
    _+="%r "%(round((z1*z2).argument,9)==round((z1.argument+z2.argument)%(2*pi),9))
    _+="%r "%(round((z1**v.n).argument,9)==round((v.n*z1.argument)%(2*pi),9))
    _+="%r "%(round(v.zPosPol.inverse.argument,9)==round((-v.zPosPol.argument)%(2*pi),9))
    _+="%r "%(round((z1/v.zPosPol).argument,9)==round((z1.argument-v.zPosPol.argument)%(2*pi),9))
    _+="%r "%(round(z1.oppose.argument,9)==round((pi+z1.argument)%(2*pi),9))
    _+="%r "%(round(z1.conjugue.argument,9)==round((-z1.argument)%(2*pi),9))
    print(_+"\n")
    
# --------------------------------------------------------------------------
def axiome_maj_cartesien():
    """
    """
    print('\n\nAXIOME_MAJ_CARTESIEN')
    v=myVars()
    f=v.f4
    s=v.s4
    _=""
    _+="%r "%(round(v.zPol.reel,9)==round(cos(s)*f,9))
    _+="%r "%(round(v.zPol.imag,9)==round(sin(s)*f,9))
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_str():
    """
    """
    print('\n\nAXIOME_STR')
    v=myVars()
    print('Affichage sous forme cartesienne : ',v.zCart)
    print('Affichage sous forme polaire : ',v.zPol)
# -------------------------------------------------------------------------- 
def axiome_module_setter():
    """
    """
    print('\n\nAXIOME_MODULE_SETTER')
    v=myVars()
    z=v.zPol
    print('Test impossibilite modifier argument si module=0 : ')
    z.module=0
    _=""
    _+="%r "%(round(z.argument)==0)
    print(_+"\n")
# -------------------------------------------------------------------------- 
def axiome_argument_setter():
    """
    """
    print('\n\nAXIOME_ARGUMENT_SETTER')
    v=myVars()
    z=v.zCart
    z.module=0
    z.argument=pi
    _=""
    _+="%r "%(z.argument==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_isCartesien():
    """
    """
    print('\n\nAXIOME_ISCARTESIEN')
    v=myVars()
    _=""
    _+="%r "%(v.zCart.isCartesien==1)
    _+="%r "%(v.zPol.isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_isPolaire():
    """
    """
    print('\n\nAXIOME_ISPOLAIRE')
    v=myVars()
    _=""
    _+="%r "%(v.zCart.isPolaire==0)
    _+="%r "%(v.zPol.isPolaire==1)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_oppose():
    """
    """
    print('\n\nAXIOME_OPPOSE')
    v=myVars()
    _=""
    _+="%r "%(v.zCart.oppose.argument>0 and v.zCart.oppose.argument<=(2*pi))
    _+="%r "%(v.zCart+v.zCart.oppose==v.zZero)
    print(_+"\n");_=""
    print('Pour un complexe cartesien :')
    _+="%r "%(v.zCart.oppose.reel==(-v.zCart.reel))
    _+="%r "%(v.zCart.oppose.imag==(-v.zCart.imag))
    _+="%r "%(v.zCart.oppose.isCartesien==1)
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    _+="%r "%(v.zPol.oppose.module==v.zPol.module)
    _+="%r "%(round(abs(v.zPol.oppose.argument-(v.zPol.argument+pi)%(2*pi)),10)==0)   
    _+="%r "%(v.zPol.oppose.isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_inverse():
    """
    """
    print('\n\nAXIOME_INVERSE')
    v=myVars()
    print('Pour un complexe cartesien :')
    _=""
    _+="%r "%((v.zCart*v.zCart.inverse)==v.zUn)
    _+="%r "%(v.zCart.inverse.isCartesien==1)
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    _+="%r "%((v.zPol*v.zPol.inverse)==v.zUn)
    _+="%r "%(v.zPol.inverse.isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_conjugue():
    """
    """
    print('\n\nAXIOME_CONJUGUE')
    v=myVars()
    z=v.zCart
    y=v.zPol
    _=""
    _+="%r "%(z*z.conjugue==Complexe(z.module**2,0,1))
    _+="%r "%(z.conjugue.conjugue==z)
    _+="%r "%(v.zR.conjugue==v.zR)
    _+="%r "%(v.zIm.conjugue==v.zIm.oppose)
    _+="%r "%((z+z.conjugue)==Complexe(2*z.reel,0,1))
    _+="%r "%((z-z.conjugue)==Complexe(0,2*z.imag,1))
    _+="%r "%((z+y).conjugue==z.conjugue+y.conjugue)
    _+="%r "%((z*y).conjugue==z.conjugue*y.conjugue)
    _+="%r "%(v.zPos.inverse.conjugue==v.zPos.conjugue.inverse)
    _+="%r "%((z**v.n).conjugue==z.conjugue**v.n)
    _+="%r "%((z/v.zPos).conjugue==z.conjugue/v.zPos.conjugue)
    print(_+"\n");_=""
    print('Pour un complexe cartesien :')
    _+="%r "%(v.zCart.conjugue.reel==v.zCart.reel)
    _+="%r "%(v.zCart.conjugue.imag==(-v.zCart.imag))
    _+="%r "%(v.zCart.conjugue.isCartesien==1)
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    _+="%r "%(v.zPol.conjugue.module==v.zPol.module)
    _+="%r "%(round(abs(v.zPol.conjugue.argument-(-v.zPol.argument)%(2*pi)),10)==0)   
    _+="%r "%(v.zPol.conjugue.isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_add():
    """
    """ 
    print('\n\nAXIOME_ADD')
    v=myVars()
    z1=v.zCart
    z2=v.zCart2
    z3=v.zPol
    _=""
    _+="%r "%((z1+z2).argument>0 and (z1+z2).argument<=(2*pi))
    _+="%r "%(z1+v.zZero==z1)
    _+="%r "%(z1+z2==z2+z1)
    _+="%r "%(z1+(z2+z3)==(z1+z2)+z3)
    print(_+"\n");_=""
    
    print('Avec un complexe cartesien en premier : ')
    _+="%r "%((z1+z2).reel==z1.reel+z2.reel)
    _+="%r "%((z1+z2).imag==z1.imag+z2.imag)
    _+="%r "%((z1+z2).isCartesien==z1.isCartesien)
    print(_+"\n");_=""
    
    print('Avec un complexe polaire en premier : ')
    m=sqrt(z3.module**2+z2.module**2+2*z3.module*z2.module*cos(z3.module-z2.module))
    _+="%r "%(round(abs((z3+z2).module-m),9)==0)
    arg=atan((z3.module*sin(z3.argument)+z2.module*sin(z2.argument))/(z3.module*cos(z3.argument)+z2.module*cos(z2.argument)))
    _+="%r "%(round(abs((z3+z2).argument-arg),9)==0)   
    _+="%r "%((z3+z2).isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_mul():
    """
    """
    print('\n\nAXIOME_MUL')

    v=myVars()
    print('Avec un complexe cartesien en premier : ')
    print('Transmission isCartesien : ',(v.zCart*v.zCart2).isCartesien==1)
    print('Element neutre : ',v.zCart*Complexe(1,0,1)==v.zCart*Complexe(1,0,0)==v.zCart)
    print('Commutativite : ',v.zCart*v.zCart2==v.zCart2*v.zCart)
    print('Associativite : ',v.zCart*(v.zCart2*v.zCart3)==(v.zCart*v.zCart2)*v.zCart3)
    print("Distributive par rapport à l'addition : ",v.zCart*(v.zCart2+v.zCart3)==(v.zCart*v.zCart2)+(v.zCart*v.zCart3))
    
    print('Avec un complexe polaire en premier : ')
    print('Transmission isPolaire : ',(v.zPol*v.zCart2).isCartesien==0)
    print('Element neutre : ',v.zPol*Complexe(1,0,1)==v.zPol*Complexe(1,0,0)==v.zPol)
    print('Commutativite : ',v.zPol*v.zPol2==v.zPol2*v.zPol)
    print('Associativite : ',v.zPol*(v.zPol2*v.zPol3)==(v.zPol*v.zPol2)*v.zPol3)
    print("Distributive par rapport à l'addition : ",v.zPol*(v.zPol2+v.zPol3)==(v.zPol*v.zPol2)+(v.zPol*v.zPol3))#PROBLEME
# --------------------------------------------------------------------------
def axiome_sub():
    """
    """
    print('\n\nAXIOME_SUB')
    v=myVars()
    z1=v.zCart
    z2=v.zCart2
    z3=v.zPol
    _=""
    _+="%r "%((z1+z2).argument>0 and (z1+z2).argument<=(2*pi))
    _+="%r "%(z1+v.zZero==z1)
    print(_+"\n");_=""
    
    print('Avec un complexe cartesien en premier : ')
    _+="%r "%(z1-z2==z1+z2.oppose)
    _+="%r "%((z1+z2).isCartesien==z1.isCartesien)
    print(_+"\n");_=""
    
    print('Avec un complexe polaire en premier : ')
    _+="%r "%(z3-z2==z3+z2.oppose)  
    _+="%r "%((z3+z2).isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_truediv():
    """
    """
    print("\n\nAXIOME_TRUEDIV")
  
    v=myVars()
    _=""
    _+="%r "%(v.zCart/Complexe(1,0,1)==v.zCart/Complexe(1,0,0)==v.zCart)
    _+="%r "%(Complexe(0,0,1)/v.zCart==Complexe(0,0,0))
    _+="%r "%(v.zCart.conjugue.isCartesien==1)
    _+="%r "%(v.zCart/v.zCart2==v.zCart*v.zCart2.inverse)
    print(_+"\n");_=""

    _+="%r "%(v.zPol/Complexe(1,0,1)==v.zPol/Complexe(1,0,0)==v.zPol)
    _+="%r "%(Complexe(0,0,1)/v.zPol==Complexe(0,0,0))
    _+="%r "%(v.zPol/v.zPol2==v.zPol*v.zPol2.inverse)
    _+="%r "%(v.zCart.conjugue.isCartesien==1)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_pow():
    """
    """
    print('\n\nAXIOME_POW')
    v=myVars()
    
    print('Pour un complexe cartesien :')
    _=""
    z=v.zCart
    _ev=""
    for i in range(v.n):
        _ev+="z*"
    _ev=_ev[:-1]
    _+="%r "%(eval(_ev)==z**v.n)
    
    _+="%r "%(z**0==v.zUn)
    _+="%r "%((z**v.n).isCartesien==1)
    print(_+"\n");_=""

    print('Pour un complexe polaire : ')
    z=v.zPol
    _ev=""
    for i in range(v.n):
        _ev+="z*"
    _ev=_ev[:-1]
    _+="%r "%(eval(_ev)==z**v.n)
    
    _+="%r "%(z**0==v.zUn) #PROBLEME
    _+="%r "%((z**v.n).isCartesien==0)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_lt():
    """
    """
    print('\n\nAXIOME_LT')
    v=myVars()
    print('Pour un complexe cartesien :')
    z=v.zPos
    _=""
    _+="%r "%((z<z)==0)
    u=Complexe(z.reel/5,z.imag/5,1)
    _+="%r "%((u<z)==1)
    t=Complexe(z.reel,z.imag/5,1)
    _+="%r "%((t<z)==1)
    print(_+"\n");_=""

    print('Pour un complexe polaire : ')
    z=v.zPosPol
    _+="%r "%((z<z)==0)
    u=Complexe(z.module/5,z.argument,0)
    _+="%r "%((u<z)==1)
    t=Complexe(z.module,-z.argument,0)
    _+="%r "%((t<z)==1)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_eq():
    """
    """
    print('\n\nAXIOME_EQ')
    v=myVars()
    print('Pour un complexe cartesien :')
    z=v.zCart
    _=""
    _+="%r "%(z==z)
    print(_+"\n");_=""
    print('Pour un complexe polaire : ')
    z=v.zPol
    _+="%r "%(z==z)
    print(_+"\n")
    
# --------------------------------------------------------------------------
def axiome_find():
    """
    """
    print('\n\nAXIOME_FIND')
    _=""
    v=myVars()
    l=[v.zCart,v.zPol,v.zCart2,v.zPol2,v.zCart3,v.zPol3,v.zPos,v.zPosPol,
       v.zUn,v.zIm,v.zR,v.zI,v.zZero]
    random.shuffle(l)
    i=random.randint(0,len(l)-1)
    a=l[i]
    _+="%r "%(a.find(l)==i)
    g=[v.zUn,v.zIm,v.zR,v.zI,v.zZero]
    a=Complexe(4,1,1)
    _+="%r "%(a.find(g)==None)
    print(_+"\n")
# --------------------------------------------------------------------------
def axiome_tri():
    """
    """
    print('\n\nAXIOME_TRI')
    v=myVars()
    _=""
    l=[v.zCart,v.zPol,v.zCart2,v.zPol2,v.zCart3,v.zPol3,v.zPos,v.zPosPol,
       v.zUn,v.zIm,v.zR,v.zI,v.zZero]
    _+="%r "%(len(l)==len(tri(l)))

    g=[]
    _+="%r "%(g==tri(g))
    print(_+"\n")

    m=[v.zCart,v.zPol,v.zCart2,v.zPol2,v.zCart3,v.zPol3,v.zPos,v.zPosPol,
       v.zUn,v.zIm,v.zR,v.zI,v.zZero]
    n=tri(m)
    _c="Verification que la liste est triee en ordre croissant : "
    for k in range(20):
        i=random.randint(1,len(n)-1)
        j=i-1
        _c += "%r "%((n[j]<n[i])==True)
    print(_c)
# --------------------------------------------------------------------------
# ----------------------------------------------------------------------
if __name__=="__main__":
    code=r'''
    print('Verification des axiomes : affiche True si axiome verifie, False sinon')

    axiome_init()

    axiome_maj_polaire()

    axiome_maj_cartesien()

    axiome_str()

    axiome_module_setter()

    axiome_argument_setter()

    axiome_isCartesien()

    axiome_isPolaire()

    axiome_oppose()

    axiome_inverse()

    axiome_conjugue()

    axiome_mul()

    axiome_pow()

    axiome_truediv()

    axiome_add()

    axiome_sub()

    axiome_lt()

    axiome_eq()

    axiome_find()

    axiome_tri()         
    ''';testcode(code)
