from enum import Enum

class Etat(Enum):
    libre = "libre"
    captive = "captive"

class Humain():

    # Attributs
    def __init__(self, nom: str, boisson: str = "eau"):
        self.__nom = nom
        self.__boisson = boisson

    # Methodes
    def parler(self, text):
        print(f"({self.nom}) - {text}")

    def se_presenter(self):
        return f"Bonjour, je suis {self.nom} et j'aime le {self.boisson}."

    def boire(self, boisson: str):
        # TO DO
        self.parler(f"Ah! un bon verre de {boisson} ! MIAMM !")
    @property
    def nom(self):
        return self.__nom

    @property
    def boisson(self):
        return self.__boisson

class Cowboy(Humain):

    def __init__(self, nom: str, adjectif: str ="vaillant", boisson: str = "eau"):
        super().__init__(nom, boisson)
        self.__popularite = 0
        self.__adjectif = adjectif

    def liberer(self, dame: Humain):
        self.parler(f"{dame.nom}, vous êtes libre maintenant.")
        dame.se_faire_liberer(self)
        self.__popularite += 1

    def tirer(self, brigand: Humain):
        print(f"Le {self.__adjectif} {self.nom} tire sur {brigand.nom}. PAN !")
        self.parler(f"Prend ça, rascal !")

    @property
    def adjectif(self):
        return self.__adjectif

    @property
    def popularite(self):
        return self.__popularite

    def se_presenter(self):
        self.parler(f"{super().se_presenter()} On dit de moi que je suis {self.adjectif} et ma popularité est actuellement de {self.popularite}/10.")


class Dame(Humain):

    def __init__(self, couleur_robe: str, nom: str, boisson: str = "champagne"):
        super().__init__(nom, boisson)
        self.__couleur_robe = couleur_robe
        self.__etat = Etat.libre
        self.__ravisseur = None
        self.__sauveur = None

    def se_faire_kidnapper(self, ravisseur: Humain):
        if self.__etat == Etat.libre:
            self.__ravisseur = ravisseur
            self.__etat = Etat.captive
            self.parler(f"Je me fait enlever par {self.__ravisseur.nom}")
        else:
            if ravisseur.nom == self.__ravisseur.nom:
                self.parler(f"Ma parole, tu es idiot {self.__ravisseur.nom}")
            else:
                self.parler(f"Je suis déjà retenue par {self.__ravisseur.nom}")

    def se_faire_liberer(self, sauveur: Humain):
        if self.__etat == Etat.captive:
            self.__sauveur = sauveur
            self.__etat = Etat.libre
        else:
            self.parler(f"Je suis déjà libre, que fais tu {sauveur.nom}?")
            
    @property
    def couleur_robe(self):
        return self.__couleur_robe

    @couleur_robe.setter
    def couleur_robe(self, new_couleur: str):
        self.__couleur_robe = new_couleur
        self.parler(f"Regardez ma nouvelle robe {self.__couleur_robe} !")
    
    # Surcharge
    @property
    def nom(self):
        return f"Miss {super().nom}"

    def se_presenter(self):
        self.parler(f"{super().se_presenter()} J'ai une belle robe {self.couleur_robe}.")


class Brigand(Humain):

    def __init__(self, nom: str, look: str = "méchant", prime: int = 100, boisson: str = "vignasse"):
        super().__init__(nom, boisson)
        self.__look = look
        self.__nb_enlevements = 0
        self.__prime = prime
        self.__prison = False

    def kidnapper(self, dame: Humain):
        self.__nb_enlevements += 1
        self.parler(f"Ah ah ! {dame.nom}, tu es mienne désormais !")
        dame.se_faire_kidnapper(self)

    def valeur_prime(self):
        return self.__prime

    def emprisonne(self, sherif: Humain): 
        self.__prison = True
        self.parler(f"Damned, je suis fait ! {sherif.nom}, tu m’as eu !")

    @property
    def prime(self):
        return self.__prime
        
    @property
    def prison(self):
        return self.__prison

    # Surcharge
    @property
    def nom(self):
        return f"{super().nom} le {self.__look}"

    
    def se_presenter(self):
        self.parler(f"{super().se_presenter()} J'ai une une prime de {self.prime} $ sur la tête.")

class Barman(Humain):

    def __init__(self, nom: str, bar: str = "", boisson: str = "vin"):
        super().__init__(nom, boisson)
        if bar =="":
            self.__bar = f'"Chez {self.nom}"'
        else:
            self.__bar = bar

    @property
    def bar(self):
        return self.__bar

    def servir(self, client: Humain):
        client.boire(client.boisson)

    def parler(self, text):
        super().parler(text + " Coco !")
    def se_presenter(self):
        self.parler(f"{super().se_presenter()} Je suis le patron de {self.bar}")

class Sherif(Cowboy):

    def __init__(self, nom: str, adjectif: str ="vaillant", boisson: str = "eau"):
        super().__init__(nom, adjectif, boisson)
        self.__nb_brigand = 0

    @property
    def nb_brigand(self):
        return self.__nb_brigand

    def coffrer(self, brigand: Humain):
        if brigand.prison:
            print(f'"{brigand.nom} est déjà en prison"')
        else:
            self.parler(f"Au nom de la loi {brigand.nom}, je vous arrête")
            brigand.emprisonne(self)

    def rechercher(self, brigand: Humain):
        print(f"OYEZ OYEZ BRAVE GENS !! {brigand.prime} $ à qui arrêtera {brigand.nom} mort ou vif !")

    @property
    def nom(self):
        return f"Shérif {super().nom}"

    
    def se_presenter(self):
        self.parler(f"Bonjour, je suis le {self.nom}. J'ai arrêté au moins {self.nb_brigand} malfrats dans ce conté.")