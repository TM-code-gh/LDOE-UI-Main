# -*- coding: utf-8 -*-
"""
Created on Thu Feb  4 01:53:16 2021

@author: Theo
"""

import math

Ressource_Bois=['Bois','Planche','Charbon','Chene','Planche chene']
Ressource_Pierre=['Pierre','Brique']
Ressource_Fibre=['Fibre','Tissus','Corde','Tissus epais']
Ressource_Alcool=['Alcool']
Ressource_Adhesif=['Adhesif','Scotch']
Ressource_Marteau=['Marteau']
Ressource_Fer=['Minerai fer','Barre fer','Plaque fer', 'Clous']

Ressource_Ferraille=['Ferraille'] #50

Ressource_Plastique=['Plastique']
Ressource_Lingot=['Lingot or','Barre aluminium','Fil aluminium', 'Minerai cuivre',
                  'Barre cuivre', 'Barre acier', 'Plaque aluminium', 'Plaque acier',
                  'Souffre', 'Plaque plomb', 'Bauxite']
Ressource_Nourriture=['Carotte','Plat carottes','Champignon','Baie','Boite conserve','Pousse','Mais']
Ressource_Soin=['Pansement','Kit soins']

Ressource_Basique=['Roulement billes','Vis','Cable','Piece caoutchouc','Transistor']
Ressource_Arme_20=['Piece usine', 'Fibre carbonne']
Ressource_Arme_50=['Ressort']
Ressource_Precieux=['Vitamines','Circuit electronique','Detecteur chaleur',
                    'Gros os','Filtre air','Lentille','Piece moteur','Huile arme',
                    'Piece tourelle','Pompe','Helice','Composant hightech',
                    'Fibre verre', 'Verre', 'Rouage', 'Gomme','Cle plate',
                    'Acide']

Ressource_Animal=['Peau','Cuire','Renard','Viande','Viande cuite', 'Viande sechee', 'Dinde', 'Dinde rotie']


max_01=[Ressource_Marteau]
max_20=[Ressource_Bois,Ressource_Pierre,Ressource_Fibre,Ressource_Alcool,
        Ressource_Adhesif,Ressource_Fer,Ressource_Plastique,Ressource_Lingot,
        Ressource_Nourriture,Ressource_Soin,Ressource_Basique,Ressource_Arme_20,
        Ressource_Precieux,Ressource_Animal]
max_50=[Ressource_Ferraille,Ressource_Arme_50]


