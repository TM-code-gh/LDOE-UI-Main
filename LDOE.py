# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 00:34:52 2021

@author: theom
"""
import math

chopper=8

sac_0=10
sac_1=15
sac_2=20
sac_3=25

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


Boite_materiaux_basiques_vide={'Bois':3,'Corde':1}
Boite_outils_vide={'Barre fer':3,'Ferraille':1}
Sac_Refrigerants_vide={'Plastique':3,'Gomme':1}
Boite_materiaux_rares_vide={'Plaque fer':3,'Plaque acier':1}

Boite_vide_nom=['Boite_materiaux_basiques_vide','Boite_outils_vide','Sac_Refrigerants_vide','Boite_materiaux_rares_vide']
Boite_vide=[Boite_materiaux_basiques_vide,Boite_outils_vide,Sac_Refrigerants_vide,Boite_materiaux_rares_vide]

Boite_materiaux_basiques_plein_1={'Planche':3,'Brique':3,'Tissus epais':2}
Boite_materiaux_basiques_plein_2={'Planche':3,'Barre fer':3,'Cuire':2}
Boite_outils_plein_1={'Cle plate':1,'Scotch':3,'Vis':5}
Boite_outils_plein_2={'Marteau':1,'Adhesif':3,'Clous':5}
Sac_Refrigerants_plein_1={'Pansement':5,'Alcool':3,'Kit soins':2}
Sac_Refrigerants_plein_2={'Viande cuite':5,'Plat carottes':3,'Dinde cuîte':2}
Boite_materiaux_rares_plein_1={'Planche chene':3,'Barre cuivre':2,'Fibre verre':2}
Boite_materiaux_rares_plein_2={'Planche chene':3,'Plaque aluminium':2,'Ciment':2}

Boite_pleine_nom=['Boite_materiaux_basiques_plein_1','Boite_materiaux_basiques_plein_2',
              'Boite_outils_plein_1','Boite_outils_plein_2',
              'Sac_Refrigerants_plein_1','Sac_Refrigerants_plein_2',
              'Boite_materiaux_rares_plein_1','Boite_materiaux_rares_plein_2']
Boite_pleine=[Boite_materiaux_basiques_plein_1,Boite_materiaux_basiques_plein_2,
              Boite_outils_plein_1,Boite_outils_plein_2,
              Sac_Refrigerants_plein_1,Sac_Refrigerants_plein_2,
              Boite_materiaux_rares_plein_1,Boite_materiaux_rares_plein_2]


Nombre_de_boite=20
sac=sac_3+chopper

j=0
for boite in Boite_vide:
    Nombre_manque=0
    Place_sac=0
    print('----------', Boite_vide_nom[j], '----------')
    for obj in boite:
        for i in range(len(max_01)):
            if(obj in max_01[i]):
                print(obj,':',Nombre_de_boite*boite[obj])
                Nombre_manque+=1
                Place_sac+=math.ceil(Nombre_de_boite*boite[obj]/1)
        for i in range(len(max_20)):
            if(obj in max_20[i]):
                print(obj,':',Nombre_de_boite*boite[obj])
                Nombre_manque+=1
                Place_sac+=math.ceil(Nombre_de_boite*boite[obj]/20)
        for i in range(len(max_50)):
            if(obj in max_50[i]):
                print(obj,':',Nombre_de_boite*boite[obj])
                Nombre_manque+=1
                Place_sac+=math.ceil(Nombre_de_boite*boite[obj]/50)
    if(Nombre_manque!=len(boite)):
        print('Il manque ',len(boite)-Nombre_manque,' obj')
    print('J\'ai besoin de', Place_sac, 'places dans le sac sur', sac_3)
    print('\n')
    j+=1


j=0
for boite in Boite_pleine:
    Nombre_manque=0
    Place_sac=0
    print('----------', Boite_pleine_nom[j], '----------')
    for obj in boite:
        for i in range(len(max_01)):
            if(obj in max_01[i]):
                print(obj,':',Nombre_de_boite*boite[obj])
                Nombre_manque+=1
                Place_sac+=math.ceil(Nombre_de_boite*boite[obj]/1)
        for i in range(len(max_20)):
            if(obj in max_20[i]):
                print(obj,':',Nombre_de_boite*boite[obj])
                Nombre_manque+=1
                Place_sac+=math.ceil(Nombre_de_boite*boite[obj]/20)
        for i in range(len(max_50)):
            if(obj in max_50[i]):
                print(obj,':',Nombre_de_boite*boite[obj])
                Nombre_manque+=1
                Place_sac+=math.ceil(Nombre_de_boite*boite[obj]/50)
    if(Nombre_manque!=len(boite)):
        print('Il manque ',len(boite)-Nombre_manque,' obj')
    print('J\'ai besoin de', Place_sac, 'places dans le sac sur', sac_3)
    print('\n')
    j+=1


