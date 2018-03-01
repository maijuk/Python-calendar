#coding=utf-8
'''
Created on 15.2.2016

@author: Maiju
'''
import tkinter as tk
import os
from Käyttöliittymä import GUI



class Poista:
    
    def __init__(self):
        self.paa_ikkuna = tk.Tk()
        
        self.ylakehys = tk.Frame(self.paa_ikkuna)
        self.keskikehys = tk.Frame(self.paa_ikkuna)
        self.alakehys = tk.Frame(self.paa_ikkuna)
        self.alinkehys = tk.Frame(self.paa_ikkuna)
        
        
        self.kysypaiva = tk.Label(self.ylakehys,\
                            text = 'Anna päivämäärä (muodossa dd/mm/yyyy): ')
        self.paivasyote = tk.Entry(self.ylakehys,\
                            width = 10)
        
        self.kysyaika = tk.Label(self.keskikehys, \
                            text = 'Anna aihe: ')
        self.aikasyote = tk.Entry(self.keskikehys, \
                            width = 10)
        
        self.ok = tk.Button(self.keskikehys,\
                        text = 'Ok',\
                        command = self.ok)
        
        
        self.ok.pack()
        self.kysypaiva.pack()
        self.paivasyote.pack()
        self.kysyaika.pack()
        self.aikasyote.pack()
        self.ylakehys.pack()
        self.keskikehys.pack()
        self.alakehys.pack()
        
        tk.mainloop
        
    def ok(self):
        tiedosto = open("tiedot.txt", 'r')
        tmp_tiedosto = open("tmp.txt", 'w')
        paiva = self.paivasyote
        aihe = self.aikasyote
        for rivi in tiedosto:
            rivi_uusi = rivi.rstrip('\n')
            rivi_uusi = rivi_uusi.split('£')
            hae_paiva = rivi_uusi[1]
            hae_aihe = rivi_uusi[0]
            if paiva != hae_paiva and aihe != hae_aihe:
                tmp_tiedosto.write(rivi)
        tiedosto.close()
        tmp_tiedosto.close()
        os.remove('tiedot.txt')
        os.rename('tmp.txt', 'tiedot.txt')
        GUI.paivita()
        self.paa_ikkuna.destroy()
        
        
        
        
        
        
        