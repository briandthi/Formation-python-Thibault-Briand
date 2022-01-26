from turtle import title
from personnages import Dame, Brigand, Barman, Sherif, Cowboy
import random
from random import randrange
from utils import preprocessing, random_in_df

class Histoire():

    def __init__(self, initialiseur):
        self.__initialiseur = initialiseur
        self.__brigands, self.__cowboys, self.__dames, self.__barmans, self.__sherifs = self.generator(self.__initialiseur)
        

    def generator(self, valeurs):
        try:
            brigands = [
                Brigand(
                    random_in_df(prenoms_m, '01_prenom'),
                    random.choice(valeurs['looks']),
                    randrange(1500)) 
                    for i in range( valeurs['personnages']['brigands'])]


            cowboys = [
                Cowboy(
                    random_in_df(prenoms_m, '01_prenom'),
                    random.choice(valeurs['adjectifs'])) 
                    for i in range( valeurs['personnages']['cowboys'])]

            dames = [
                Dame(
                    random.choice(valeurs['couleurs']),
                    random_in_df(prenoms_f, '01_prenom')) 
                    for i in range( valeurs['personnages']['dames'])]

            barmans = [
                Barman(
                    random_in_df(prenoms_m, '01_prenom')) 
                    for i in range( valeurs['personnages']['barmans'])]

            sherifs = [
                Sherif(
                    random_in_df(prenoms_m, '01_prenom'),
                    random.choice(valeurs['adjectifs'])) 
                    for i in range( valeurs['personnages']['sherifs'])]

            return brigands, cowboys, dames, barmans, sherifs

        except Exception as e:
            raise e

    @property
    def brigands(self):
        return self.__brigands

    @property
    def cowboys(self):
        return self.__cowboys

    @property
    def dames(self):
        return self.__dames
        
    @property
    def barmans(self):
        return self.__barmans
        
    @property
    def sherifs(self):
        return self.__sherifs

    def liberer(self):
        random.choice(self.__cowboys).liberer(random.choice(self.__dames))
    def tirer(self):
        random.choice(self.__cowboys).tirer(random.choice(self.__brigands))
    def changer_robe(self):
        random.choice(self.__dames).couleur_robe = random.choice(self.__initialiseur['couleurs'])
    def servir(self):
        rand_h = random.choice([self.__brigands, self.__cowboys, self.__dames, self.__sherifs])
        random.choice(self.__barmans).servir(random.choice(rand_h))
    def kidnapper(self):
        random.choice(self.__brigands).kidnapper(random.choice(self.__dames))
    def coffrer(self):
        random.choice(self.__sherifs).coffrer(random.choice(self.__brigands))
    def rechercher(self):
        random.choice(self.__sherifs).coffrer(random.choice(self.__brigands))

    def rand_action(self):
        i = randrange(1,7)
        if i == 1:
            self.liberer()
        elif i == 2:
            self.tirer()
        elif i == 3:
            self.changer_robe()
        elif i == 4:
            self.servir()
        elif i == 5:
            self.kidnapper()
        elif i == 6:
            self.coffrer()
        elif i == 7:
            self.rechercher()

import tkinter as tk
import tkinter.ttk as ttk

class Main():

    def __init__(self):
        Histoire(initialisateur)

    def main(self):
        main = Histoire(initialisateur)

        root = tk.Tk()


        Label1 = tk.Label(text = "Distribution").pack(side = tk.TOP)

        # Personnages
        list_dame = tk.Listbox()
        for i in range(len(main.dames)):
            list_dame.insert(i, main.dames[i].nom)
        list_dame.pack(side = tk.LEFT)

        list_cb = tk.Listbox()
        for i in range(len(main.cowboys)):
            list_cb.insert(i, main.cowboys[i].nom)
        list_cb.pack(side = tk.LEFT)

        list_b = tk.Listbox()
        for i in range(len(main.brigands)):
            list_b.insert(i, main.brigands[i].nom)
        list_b.pack(side = tk.LEFT)

        list_bar = tk.Listbox()
        for i in range(len(main.barmans)):
            list_bar.insert(i, main.barmans[i].nom)
        list_bar.pack(side = tk.LEFT)

        list_s = tk.Listbox()
        for i in range(len(main.sherifs)):
            list_s.insert(i, main.sherifs[i].nom)
        list_s.pack()


        action_alea = tk.Button(text="action aléatoire", command=main.rand_action).pack()
        # brigand = ttk.Combobox(values=[brigand.nom for brigand in main.brigands]).pack(side = tk.LEFT)
        # Label2 = tk.Label(text = "enlève").pack(side = tk.LEFT)
        # dame = ttk.Combobox(values=[dame.nom for dame in main.dames]).pack(side = tk.LEFT)
        # enlever = tk.Button(text="Enlever").pack(side = tk.LEFT)

        root.mainloop()

import pandas as pd

prenoms = pd.read_csv("TP2/Prenoms.csv", delimiter=';', encoding="iso-8859-1")
prenoms_f, prenoms_m = preprocessing(prenoms) 

looks = ['accueillant', 'adorable', 'ambitieux', 'alourdi', 'attifé', 'attrayant', 'beau', 'carré', 'costaud', 'crasseux', 'désillusionné', 'droit', 'dynamique', 'élégant']
adjectifs = ['agressif', 'Amusé', 'Avare', 'Brave', 'Brillant', 'Calme', 'chaleureux', 'combatif', 'coopératif', 'cruel', 'dangereux', 'Débile', 'Désagréable', 'Déterminé']	
couleurs = ['Abricot', 'acajou', 'ammande', 'ambre', 'azur', 'blanc cassé', 'bronze', 'cacao', 'écru']

initialisateur = {
    'personnages':{
        'cowboys': 3,
        'dames': 6,
        'barmans': 2,
        'sherifs': 1,
        'brigands': 4
    },
    'prenoms': {
        'femme': prenoms_f,
        'homme': prenoms_m
    },
    'adjectifs': adjectifs,
    'looks': looks,
    'couleurs':couleurs
}

Main().main()