'''
Created on 22.1.2016

@author: Maiju
'''
import tkinter as tk
import time
import datetime
from datetime import date, timedelta, datetime
import Uusi_ikkuna
import Poista
from tkinter.scrolledtext import ScrolledText


class GUI():
    def __init__(self):

        self.paa_ikkuna = tk.Tk()

        self.ylakehys = tk.Frame(self.paa_ikkuna)
        self.keskikehys = tk.Frame(self.paa_ikkuna)
        self.alakehys = tk.Frame(self.paa_ikkuna)

        # päivämäärän näyttö ja valinta 
        self.paiva = time.strftime("%d/%m/%Y")

        self.paivamaara = tk.Entry(self.ylakehys, \
                                   text=self.paiva, \
                                   width=10)
        self.paivamaara.delete(0, len(self.paivamaara.get()))
        self.paivamaara.insert(0, self.paiva)

        self.vasemmalle = tk.Button(self.ylakehys, \
                                    text="<", \
                                    command=self.vasen)

        self.oikealle = tk.Button(self.ylakehys, \
                                  text=">", \
                                  command=self.oikea)

        self.vasemmalle.pack(side='left')
        self.paivamaara.pack(side='left')
        self.oikealle.pack(side='left')

        # muistutusten tekstikenttä

        self.tekstit = tk.StringVar()
        self.teksti_kentta = ScrolledText(self.keskikehys, width=15, height=8)
        self.teksti_kentta.pack()
        self.paivita()

        # alarivin "uusi muistutus" ja "poista" napit
        self.uusi_nappi = tk.Button(self.alakehys, \
                                    text='Uusi muistutus', \
                                    command=self.uusi)
        self.poista_nappi = tk.Button(self.alakehys, \
                                      text="Poista", \
                                      command=self.poista)
        self.uusi_nappi.pack(side="left")
        self.poista_nappi.pack(side='right')

        self.ylakehys.pack()
        self.keskikehys.pack()
        self.alakehys.pack()

        tk.mainloop()

    # hakee päivän muistutukset ohjelman käynnistyessä ja päivää vaihdettaessa

    def paivita(self):
        self.teksti_kentta.delete(1.0, tk.END)
        tiedosto = open('tiedot.txt', 'r')
        for rivi in tiedosto:
            rivi = rivi.rstrip('\n')
            rivi = rivi.split('£')
            hae_paiva = rivi[1]
            if hae_paiva == self.paiva:
                self.teksti_kentta.insert(tk.INSERT, rivi[2] + ' ')
                self.teksti_kentta.insert(tk.END, rivi[0] + ' ')
                self.teksti_kentta.insert(tk.END, '\n')

    # päivämäärän selaamiseen käytettävät napit

    def vasen(self):
        self.paiva = datetime.strptime(self.paiva, "%d/%m/%Y")
        self.paiva = self.paiva - timedelta(1)
        self.paiva = (self.paiva.strftime("%d/%m/%Y"))
        self.paivamaara.delete(0, len(self.paivamaara.get()))
        self.paivamaara.insert(0, self.paiva)
        self.paivita()

        return self.paiva

    def oikea(self):
        self.paiva = datetime.strptime(self.paiva, "%d/%m/%Y")
        self.paiva = self.paiva + timedelta(1)
        self.paiva = (self.paiva.strftime("%d/%m/%Y"))
        self.paivamaara.delete(0, len(self.paivamaara.get()))
        self.paivamaara.insert(0, self.paiva)
        self.paivita()
        return self.paiva

    # napit muistutusten luomiseen ja poistamiseen

    def uusi(self):
        Uusi_ikkuna.Uusi_ikkuna()

    def poista(self):
        Poista.Poista()


ohjelma = GUI()
