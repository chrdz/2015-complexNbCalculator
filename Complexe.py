# ==============================================================================
"""Complexe : classe pour manipuler des nombres complexes"""
# ==============================================================================
__author__ = "marie perez et charlotte rodriguez"
__date__ = "20.10.15"
__version__ = "2.0"
# ------------------------------------------------------------------------------
from math import * #changer pour n importer que le necessaire
from main_basique import *
# ------------------------------------------------------------------------------
class Complexe(object):
    # --------------------------------------------------------------------------
    def __init__(self,f,s,cart=True):
        """
        utilisteur doit obligatoirement entrer 2 valeurs (f et s)
        (f pour first ; s pour second)
        cart==True ==> f et s sont coordonnees cartesiennes du complexe
        cart==False ==> f et s sont coordonnees polaires du complexe
        (reel : float ou int)
        (True==1 ; False==0)
        """
        
        self.__d={'reel':0,'imag':0,'module':0,'argument':0,'cart':True}

        assert cart in (0,1),"1 pour repr cartesienne, 0 pour repr polaire"
        assert isinstance(f,(float,int)),"pas un reel"
        assert isinstance(s,(float,int)),"pas un reel"
        self.__d['cart']=cart
        if self.isCartesien:
            self.__d['reel']=f
            self.__d['imag']=s
            self.maj_polaire()
        else:
            assert f>=0,"module negatif"
            self.__d['module']=f
            self.__d['argument']=s%(2*pi)
            self.maj_cartesien()
    # --------------------------------------------------------------------------
    def maj_polaire(self):
        """
        (maj=mise a jour)
        met a jour les coor polaires de self en fct de ses coor cartesiennes
        """

        #maj du module
        self.__d['module']=sqrt(self.reel**2+self.imag**2)

        #maj argument
        if self.module==0:
            self.__d['argument']=0
        else:
            if self.reel<0 and self.imag==0:
                self.__d['argument']=pi
            else:
                assert (self.module+self.reel)!=0, "division par 0 !!!!"
                self.__d['argument']=(2*atan(self.imag/(self.module+self.reel)))%(2*pi) #division par 0
    # --------------------------------------------------------------------------
    def maj_cartesien(self):
        """
        met a jour les coor cartesiennes de self en fct de ses coor polaires
        """
        self.__d['reel']=cos(self.argument)*self.module
        self.__d['imag']=sin(self.argument)*self.module
    # --------------------------------------------------------------------------
    def __repr__(self):
        """
        """
        if self.isCartesien:
            return "%f+(%f)i"%(round(self.reel,9),round(self.imag,9))
        else:
            return "%fexp(%fi)"%(round(self.module,9),round(self.argument,9))
    # --------------------------------------------------------------------------   
    @property
    def reel(self):
        """
        """
        return self.__d['reel']
    # -------------------------------------
    @reel.setter
    def reel(self,val):
        """
        """
        
        assert isinstance(val,(float,int)),"n'est pas un reel"
        self.__d['reel']=val
        self.maj_polaire()
    # --------------------------------------------------------------------------
    @property
    def imag(self):
        """  """
        
        return self.__d['imag']
    # -------------------------------------
    @imag.setter
    def imag(self,val):
        """  """
        
        assert isinstance(val,(float,int)),"n'est pas un reel"
        self.__d['imag']=val
        self.maj_polaire()
    # --------------------------------------------------------------------------
    @property
    def module(self):
        """ """
        
        return self.__d['module']
    # -------------------------------------
    @module.setter
    def module(self,val):
        """ """
        
        assert isinstance(val,(float,int)),"n'est pas un reel"
        assert val>=0,"module negatif"
        self.__d['module']=val
        if self.module==0:self.__d['argument']=0
        self.maj_cartesien()
    # --------------------------------------------------------------------------
    @property
    def argument(self):
        """  """
        
        return self.__d['argument']
    # -------------------------------------
    @argument.setter
    def argument(self,val):
        """  """
        
        if self.module!=0:
            assert isinstance(val,(float,int)),"n'est pas un reel"
            self.__d['argument']=val%(2*pi)
            self.maj_cartesien()
        else:
            print("Module nul donc argument nul")
    # --------------------------------------------------------------------------
    @property
    def isCartesien(self):
        """
        """
        
        return self.__d['cart']
    # --------------------------------------------------------------------------
    @property
    def isPolaire(self):
        """
        """
        
        return not self.__d['cart']
    # --------------------------------------------------------------------------
    @property
    def cartesien(self):
        """      
        renvoie les coordonnees cartesiennes du Complexe
        """
        return (self.reel,self.imag)
    # --------------------------------------------------------------------------
    @property
    def polaire(self):
        """      
        renvoie les coordonnees polaires du Complexe
        """
        return (self.module,self.argument)
    # --------------------------------------------------------------------------
    @property
    def oppose(self):
        """
        """
        
        if self.isCartesien:
            return Complexe(-self.reel,-self.imag,1)
        else:
            return Complexe(self.module,self.argument+pi,0)
    # --------------------------------------------------------------------------
    @property
    def inverse(self):
        """
        """
        
        #renvoie None si la valeur n est pas definie
        if self.isCartesien:
            assert (self.reel!=0 or self.imag!=0), "division par zero"
            return Complexe(self.reel/(self.reel**2+self.imag**2),
                            -self.imag/(self.reel**2+self.imag**2),1)
        else:
            assert self.__d['module']!=0, "division par 0"
            return Complexe(1/self.module,-self.argument,0)
    # --------------------------------------------------------------------------
    @property
    def conjugue(self):
        """
        """
        
        if self.isCartesien:
            return Complexe(self.reel,-self.imag,1)
        else:
            return Complexe(self.module,-self.argument,0)
    # --------------------------------------------------------------------------
    def __abs__(self):
        """
        """
        
        return self.__d['module']
    # --------------------------------------------------------------------------
    def __add__(self,other):
        """
        """
        
        assert isinstance(other,Complexe),"pas un Complexe"

        if self.isCartesien:
            return Complexe(self.reel+other.reel,self.imag+other.imag,1)
        else:
            return Complexe(sqrt(self.module**2+other.module**2+2*self.module
                                 *other.module*cos(self.module-other.module)),
                            atan((self.module*sin(self.argument)+other.module*
                                  sin(other.argument))/(self.module*cos(self.argument)
                                                        +other.module*cos(other.argument))),
                            0)
    # --------------------------------------------------------------------------
    def __mul__(self,other):
        """
        """
        
        if self.isCartesien:
            return Complexe(self.reel*other.reel-self.imag*other.imag,
                            self.reel*other.imag+self.imag*other.reel,1)
        else:
            return Complexe(self.module*other.module,
                            self.argument+other.argument,0)
    # --------------------------------------------------------------------------
    def __sub__(self,other):
        """
        """
        
        return self+other.oppose
    # --------------------------------------------------------------------------
    def __truediv__(self,other):
        """
        """
        
        return self*other.inverse
    # --------------------------------------------------------------------------
    def __pow__(self,other):
        """
        """
        
        assert isinstance(other,int), "puissance entière"
        assert other>=0,"puissance negative"
        if other==0:
            if self.isCartesien:
                return Complexe(1,0,1)
            else:
                return Complexe(1,0,1)
        else:
            if self.isCartesien:
                s=Complexe(1,0,1)
                for i in range(other):
                    t=s*self
                    s.reel=t.reel
                    s.imag=t.imag
                return s
            else:
                return Complexe(self.module**other,self.argument*other,0)                 
    # --------------------------------------------------------------------------
    def __lt__(self,other):
        """        
        renvoie True si self<other, False sinon
        """
        #on compare en ecriture cartesienne
        assert isinstance(other,Complexe),"pas un Complexe"
        if round(self.reel-other.reel,9)<0:return True
        elif round(self.reel-other.reel,9)>0:return False
        else: #dans ce cas self.reel==other.reel
            if round(self.imag-other.imag)<0 :return True
            else:return False            
    # --------------------------------------------------------------------------
    def __eq__(self,other):
        """       
        renvoie True si self==other, False sinon
        """
        assert isinstance(other,Complexe),"pas un Complexe"

        if self.isCartesien:
            return round(self.reel,10)==round(other.reel,10)and round(self.imag,10)==round(other.imag,10)
        else:
            return round(self.module,10)==round(other.module,10)and round(self.argument,10)==round(other.argument,10)
    # --------------------------------------------------------------------------
    def find(self,l):
        """       
        Cherche self dans la liste l (de complexes)
        Renvoyer None si n est pas dedans, l'indice si dedans
        """
        assert isinstance(l,list),"l n est pas une liste"
        n=len(l)
        i=0
        while i<n:
            assert isinstance(l[i],Complexe),"liste ne contient pas que des Complexes"
            i+=1
        trouve=0
        i=0
        while i<n and not trouve:
            if l[i]==self:trouve=True
            else:i+=1
        if trouve : return i
        else: return None
    # --------------------------------------------------------------------------
#----------------------------------------------------------
def tri(l):
    """
    renvoie la version triee de la liste de complexes l
    si l vide -> renvoie liste vide
    """

    #verification que est liste de complexes
    assert isinstance(l,list),"pas une liste"
    n=len(l)
    if n<=0:#l est vide
        return []
    i=0
    while i<n:
        assert isinstance(l[i],Complexe),"liste ne contient pas que Complexes"
        i+=1

    p=[]
    while n!=0:
        c=l[0]
        ind=0
        i=0
        while i<n:
            if l[i]<c:
                c=l[i]
                ind=i
            i+=1
        del l[ind]
        p.append(c)
        n=len(l)
    return(p)
#----------------------------------------------------------
if __name__=="__main__":
    main_basique()
          
    
