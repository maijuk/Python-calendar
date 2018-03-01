#coding=utf-8
'''
Created on 3.2.2016

@author: Maiju

'''
import tkinter as tk
from tkinter import messagebox
import Muistutukset
import time
import datetime

import pickle

class Uusi_ikkuna:
    def __init__(self):
        
        self.paa_ikkuna = tk.Toplevel()
        
        self.ylakehys = tk.Frame(self.paa_ikkuna)
        self.keskikehys = tk.Frame(self.paa_ikkuna)
        self.alakehys = tk.Frame(self.paa_ikkuna)
        self.alinkehys = tk.Frame(self.paa_ikkuna)
        
        self.aihe_teksti = tk.Label(self.ylakehys, \
                            text = 'Aihe: ')
        self.aihe_syote = tk.Entry(self.ylakehys, \
                                        width = 10)


        self.aika_teksti = tk.Label(self.keskikehys, \
                            text = 'Aika (hh:mm): ')

        self.aika_syote = tk.Entry(self.keskikehys, \
                                        width = 10)
        self.paiva_teksti = tk.Label(self.alakehys, \
                            text = 'Päivämäärä (dd/mm/yyyy): ')
        self.paiva_syote = tk.Entry(self.alakehys, \
                                        width = 10)
        
        self.cb_muut = tk.IntVar()
        self.cb_muut.set(0)
        self.cb = tk.Checkbutton(self.alinkehys, \
                    text='Haluatko hälytyksen?', variable = self.cb_muut)
        
        self.aihe_teksti.pack(side='left')
        self.aihe_syote.pack(side='left')
        self.paiva_teksti.pack(side='left')
        self.paiva_syote.pack(side='left')
        self.aika_teksti.pack(side='left')
        self.aika_syote.pack(side='left')
        self.cb.pack()
        
        self.ok_painike = tk.Button(self.alinkehys, \
                                        text='Ok', \
                                        command = self.tallenna)
        self.lopetus_painike = tk.Button(self.alinkehys, \
                                        text = 'Takaisin', \
                                        command = self.paa_ikkuna.destroy)
        self.ok_painike.pack(side='left')
        self.lopetus_painike.pack(side='left')
        
        self.ylakehys.pack()
        self.keskikehys.pack()
        self.alakehys.pack()
        self.alinkehys.pack()
        
        
        tk.mainloop()
        
    def tallenna(self):
        try:
            time.strptime(self.aika_syote.get(), '%H:%M')
        except ValueError:
            tk.messagebox.showwarning("Anna aika muodossa hh:mm")
            return
        try:
            datetime.datetime.strptime(self.paiva_syote.get(), "%d/%m/%Y")
        except ValueError:
            tk.messagebox.showwarning("Anna päivämäärä muodossa dd/mm/yyyy")
            return

        muistutus = Muistutukset.Muistutus(self.aihe_syote.get(), self.paiva_syote.get(), self.aika_syote.get(), self.cb_muut.get())
        tiedostoon = muistutus.get_teksti() + '£'+ str(muistutus.get_paiva()) + '£'+str(muistutus.get_aika())+'£'+str(muistutus.get_halytys()) +'\n'
        tiedosto = open("tiedot.txt", 'a')
        tiedosto.write(tiedostoon)
        tiedosto.close()
        self.paa_ikkuna.destroy()
        
        
#ikkuna=Uusi_ikkuna()
        
        