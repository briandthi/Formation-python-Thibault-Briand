import pandas as pd


def preprocessing(prenoms):
    prenoms["04_fréquence"].astype(float)
    prenoms_frequent = prenoms[(prenoms["04_fréquence"] > 1) ]
    prenoms_f = prenoms_frequent[(prenoms_frequent["02_genre"] == "f")]
    prenoms_m = prenoms_frequent[(prenoms_frequent["02_genre"] == "m")]
    return prenoms_f, prenoms_m
    

from random import randrange
import random

## fonction utilitaires
def random_in_df(df, col:str):
    nb = randrange(0, len(df) - 1)
    rand_prenom = df[col].iloc[nb]
    return rand_prenom