'''
Created on 31.1.2016

@author: Maiju
'''
class Muistutus:
    def __init__(self, teksti, paiva, aika, halytys):
        self.__teksti = teksti
        self.__paiva = paiva
        self.__aika = aika
        self.__halytys = halytys
        
    def set_teksti(self, teksti):
        self.__teksti = teksti
        
    def set_aika(self, aika):
        self.__aika = aika
        
    def set_paiva(self, paiva):
        self.__paiva = paiva
        
    def set_halytys(self, halytys):
        self.__halytys = halytys
    
    def get_teksti(self):
        return self.__teksti
    
    def get_paiva(self):
        return self.__paiva
    
    def get_aika(self):
        return self.__aika
    
    def get_halytys(self):
        return self.__halytys
    
    def tallenna(self):
        pass
        
    def __str__(self):
        return self.__teksti +' '+ str(self.__paiva)+' '+str(self.__aika)+' '+str(self.__halytys)