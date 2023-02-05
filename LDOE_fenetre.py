# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 18:30:11 2021

@author: Theo
"""
import sys
import datetime
import math

from PyQt5.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import * 

def today():
    global JJ_MM
    if(len(str(datetime.date.today().day))==1):
        JJ="0"+str(datetime.date.today().day)
    else:
        JJ=str(datetime.date.today().day)
    if (len(str(datetime.date.today().month))==1):
        MM="0"+str(datetime.date.today().month)
    else:
        MM=str(datetime.date.today().month)
    JJ_MM=JJ+"/"+MM
    return JJ_MM
    
def Bunker(date):
    global code
    codes_02=["01922","17539","71617","19295","95363","56227","62328","23121",
           "32991","23679","31256","19237","96271","62983","22711"]
    codes_03=["22711","22517","29397","97761","75879","53111","37131","78917",
           "81675","11773","19111","96398","67119","71717","13774","31151"]
    """
    if(str(datetime.date.today().month)=='2'):
        code=codes_02[int(int(date[0:2])/2)]
    
    elif(str(datetime.date.today().month)=='3'):
        code=codes_03[int(int(date[0:2])/2)]
    
    else:
        code = '0000'
        return code
    """
    code = '0000'
    return code

today()
Bunker(today())


class creer_Q():
    """
    La classe creer_Q regroupe les méthodes de création de QObjects.
    
    Paramètres
    ----------
    None.
    
    """
    
    def __init__(self):
        """
        Constructeur de la classe creer_Q

        Returns
        -------
        None.

        """
        
        self.font = QFont()
        self.font.setFamily(u"DejaVu Sans")
        self.font.setPointSize(12)
        self.font.setBold(True)
        self.font.setItalic(False)
        self.font.setWeight(75)
        
    def creer_Qlabel(self, name, geometry, txt):
        """
        Crée un Qlabel de manière générique adapté à nos besoins.

        Paramètres
        ----------
        name : unicode string : Nom du Qlabel
        geometry : QRect : Forme et taille du Qlabel
        txt : unicode string : Texte à afficher

        Returns
        -------
        self : Qlabel Object

        """
        self = QLabel(self.centralwidget)
        self.setObjectName(name)
        self.setGeometry(geometry)
        self.setText(QCoreApplication.translate("MainWindow", txt, None))
        return self

    def creer_QComboBox(self, items, name, geometry):
        """
        Crée une QComboBox de manière générique adapté à nos besoins.

        Paramètres
        ----------
        items : liste d'unicode string : Liste contenant l'ensemble des items à ajouter dans la QComboBox
        name : unicode string : Nom du QComboBox
        geometry :  QRect : Forme et taille du QComboBox

        Returns
        -------
        self : QComboBox Object

        """
        self = QComboBox(self.centralwidget)
        self.setObjectName(name)
        self.setGeometry(geometry)
        self.addItems(items)
        return self

    def creer_QPushButton(self, name, geometry, txt):
        """
        Crée une QPushButton de manière générique adapté à nos besoins.

        Parameters
        ----------
        name : unicode string : Nom du QPushButton
        geometry :  QRect : Forme et taille du QPushButton
        txt : unicode string : Texte à afficher

        Returns
        -------
        self : QPushButton Object

        """
        self = QPushButton(self.centralwidget)
        self.setObjectName(name)
        self.setGeometry(geometry)
        self.setText(txt)
        return self

    def creer_QSpinBox(self, name, geometry, max_size, mini, maxi, value):
        """
        Crée une QSpinBox de manière générique adapté à nos besoins.

        Parameters
        ----------
        name : unicode string : Nom du QSpinBox
        geometry :  QRect : Forme et taille du QSpinBox
        max_size : QSize : ??
        mini : int : Valeur minimale
        maxi : int : Valeur maximale
        value : int : Valeur par défaut

        Returns
        -------
        self : QSpinBox Object

        """
        self = QSpinBox(self.centralwidget)
        self.setObjectName(name)
        self.setGeometry(geometry)
        self.setMaximumSize(max_size)
        self.setMinimum(mini)
        self.setMaximum(maxi)
        self.setValue(value)
        return self
    

class Ui_MainWindow(QWidget, creer_Q):
    """
    La classe Ui_MainWindow permet de créer la fenêtre principale de notre UI.
    
    Paramètres
    ----------
    Objet de type QtWidgets
    
    Exemple
    -------
    MainWindow = QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    """
    
    def __init__(self):
        """
        Constructeur de la classe Ui_MainWindow

        Returns
        -------
        None.

        """
        super().__init__()
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
               
    
    def setupUi(self, MainWindow):
        """
        Mise en place des informations de la fenêtre principale.

        Paramètres
        ----------
        MainWindow : QtWidgets.QMainWindow() Object : Fenêtre

        Returns
        -------
        None.

        """
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(530, 519)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Fenêtre principale", None))
        
        self.Date_txt = self.creer_Qlabel(u"Date_txt", QRect(10, 10, 110, 16), u"Date (JJ/MM) :")
        self.Date_val = self.creer_Qlabel(u"Date_val", QRect(120, 10, 71, 16), JJ_MM)
        self.Code_txt = self.creer_Qlabel(u"Code_txt", QRect(360, 10, 100, 16), u"Code Bunker : ")
        self.Code_val = self.creer_Qlabel(u"Code_val", QRect(470, 10, 51, 16), code)
        
        self.label_zone = self.creer_Qlabel(u"label_zone", QRect(165, 70, 200, 61), u"Choisir la zone")
        self.label_zone.setStatusTip(QCoreApplication.translate("MainWindow", u"Choisir une zone à découvrir.", None))
        self.label_zone.setFont(self.font)
        
        items = [u"Pin\u00e8des", u"Cr\u00eate de calcaire", u"Station essence", u"Port"]
        self.CB_zone = self.creer_QComboBox(items, u"CB_zone", QRect(150, 150, 201, 31))
        
        items = [u"Vert", u"Jaune", u"Rouge", u"Bleu"]
        self.CB_couleur = self.creer_QComboBox(items, u"CB_couleur", QRect(40, 150, 101, 31))
        self.CB_couleur.currentTextChanged.connect(lambda: self.clicked_couleur(str(self.CB_couleur.currentText())))
        
        self.Boutton_zone = self.creer_QPushButton(u"Boutton_zone", QRect(400, 150, 91, 31),  u"OK")
        self.Boutton_zone.clicked.connect(lambda: self.clicked_bt_zone(str(self.CB_zone.currentText())))
        
        self.label_ressource = self.creer_Qlabel(u"label_ressource", QRect(130, 200, 270, 61), u"Chercher Ressource")
        self.label_ressource.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Taper la ressource que vous souhaitez trouver. Il en sortira les lieux o\u00f9 la trouver.", None))
        self.label_ressource.setFont(self.font)
        
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 270, 311, 31))
        
        self.Button_ressource = self.creer_QPushButton(u"Button_ressource", QRect(400, 270, 91, 31),  u"OK")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 22))
        
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(self.centralwidget)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)
        
    def clicked_couleur(self, couleur):
        if couleur=="Vert":
            items = [u"Pin\u00e8des", u"Cr\u00eate de calcaire", u"Station essence", u"Port"]
            self.CB_zone.clear()
            self.CB_zone.addItems(items)
        elif couleur=="Jaune":
            items = [u"Bosquet de pins", u"Falaises calcaires", u"H\u00f4tel", u"Brousses de ch\u00eane", u"Pied de montagne Bois\u00e9", u"F\u00f4ret des marais"]
            self.CB_zone.clear()
            self.CB_zone.addItems(items)
        elif couleur=="Rouge":
            items = [u"Usine abandonn\u00e9e", u"Fl\u00e8ches de calcaires", u"For\u00eat infect\u00e9e", u"Vieille Ferme", u"Bunker Alpha", u"Bunker Bravo", u"Commissariat de police", u"Ch\u00eaneraie", 
                     u"For\u00eat gel\u00e9e", u"Carri\u00e8re de sable", u"\u00cele des morts", u"Tourbi\u00e8re sauvages"]
            self.CB_zone.clear()
            self.CB_zone.addItems(items)
        else:
            items = [u"Tour de guet de l'est", u"Tour de guet du nord", u"Tour de guet", u"Plate-forme p\u00e9troli\u00e8re"]
            self.CB_zone.clear()
            self.CB_zone.addItems(items)
        
    def clicked_bt_zone(self, zone):
            
        if zone=="Port":
            self.w_port=Ui_WindowPort()
            self.w_port.setupUi(self.w_port)
            #self.w_port.setupPort(self.w_port)
            self.w_port.show()
            
        else:
            print(zone)
            
        
class Ui_WindowPort(QWidget, creer_Q):
    """
    La classe Ui_WindowPort permet de créer la fenêtre correspondant à la zone du port de notre UI.
    
    Paramètres
    ----------
    Aucuns
    
    Example
    -------
    
    """
    
    def __init__(self):
        """
        Constructeur de la classe Ui_WindowPort

        Returns
        -------
        None.

        """
        
        super().__init__()
        self.centralwidget = QWidget(self)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.txt_before="<!DOCTYPE HTML PUBLIC>\n <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n p, li { white-space: pre-wrap; }\n </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
        self.txt_style="<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
    
    def setupUi(self, WindowPort):
        if WindowPort.objectName():
            WindowPort.setObjectName(u"WindowPort")
        WindowPort.setEnabled(True)
        WindowPort.resize(530, 519)
        WindowPort.setWindowTitle(QCoreApplication.translate("WindowPort", u"Zone du port", None))
        
        self.Code_txt = self.creer_Qlabel(u"Code_txt", QRect(380, 10, 71, 16), u"Code Bunker : ")
        self.Code_val = self.creer_Qlabel(u"Code_val", QRect(470, 10, 51, 16), code)
        self.Date_txt = self.creer_Qlabel(u"Date_txt", QRect(10, 10, 81, 16), u"Date (JJ/MM) :")
        self.Date_val = self.creer_Qlabel(u"Date_val", QRect(90, 10, 71, 16), JJ_MM)
        
        txt = u"<html><head/><body><p><span style=\" font-size:14pt;\">D\u00e9couvrir la zone du Port</span></p></body></html>"
        self.Port_txt = self.creer_Qlabel(u"Port_txt", QRect(150, 30, 221, 61), txt)
        
        items = [u"Boite de mat\u00e9riaux basiques vide", u"Boite d'outils vide", u"Sac R\u00e9frig\u00e9rant vide", u"Boite de mat\u00e9riaux rares vide",
                 u"Boite de mat\u00e9riaux basiques plein", u"Boite d'outils plein", u"Sac R\u00e9frig\u00e9rant plein", u"Boite de mat\u00e9riaux rares plein"]
        self.CB_Boite = self.creer_QComboBox(items, u"CB_Boite", QRect(180, 130, 191, 31))
        
        txt = u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Jake</span></p></body></html>"
        self.Jake_txt = self.creer_Qlabel(u"Jake_txt", QRect(150, 70, 221, 61), txt)
        
        items = [u"Livraison", u"Laboratoire", u"Verrouill\u00e9(e)"]
        self.CB_Livraison = self.creer_QComboBox(items, u"CB_Livraison", QRect(40, 130, 131, 31))
        self.CB_Livraison.currentTextChanged.connect(lambda: self.clicked_Jake(str(self.CB_Livraison.currentText())))
        
        self.Bt_Actualiser_Boite = self.creer_QPushButton(u"Bt_Actualiser_Boite", QRect(430, 130, 91, 31),  u"Actualiser")
        self.Bt_Actualiser_Boite.clicked.connect(lambda: self.total())
        
        self.Nb_boite_txt = self.creer_Qlabel(u"Nb_boite_txt", QRect(380, 125, 47, 14), u"NB Boite")
        
        self.spinBox_Nb_boite = self.creer_QSpinBox(u"spinBox_Nb_boite", QRect(380, 140, 42, 22), QSize(42, 16777215), 1, 50, 8)
        
        temp=self.txt_before+self.txt_style+"1. XX object1</p\n"+self.txt_style+"    XX object2</p></body></html>"
        self.Boite_1_txt = self.creer_Qlabel(u"Boite_1_txt", QRect(40, 180, 161, 51), temp)
        
        temp=self.txt_before+self.txt_style+"2. XX object1</p\n"+self.txt_style+"    XX object2</p></body></html>"
        self.Boite_2_txt = self.creer_Qlabel(u"Boite_2_txt", QRect(40, 225, 161, 51), temp)
        
        self.Place_sac_1 = self.creer_Qlabel(u"Place_sac_1", QRect(200, 190, 161, 21), u"XX places dans le sac sur XX")
        self.Place_sac_2 = self.creer_Qlabel(u"Place_sac_2", QRect(200, 230, 161, 21), u"XX places dans le sac sur XX")
        
        self.radioButton_sac_1 = QRadioButton(WindowPort)
        self.radioButton_sac_1.setObjectName(u"radioButton_sac_1")
        self.radioButton_sac_1.setGeometry(QRect(390, 200, 41, 18))
        self.radioButton_sac_1.setText(QCoreApplication.translate("WindowPort", u"1", None))
                
        self.radioButton_sac_2 = QRadioButton(WindowPort)
        self.radioButton_sac_2.setObjectName(u"radioButton_sac_2")
        self.radioButton_sac_2.setGeometry(QRect(430, 200, 41, 18))
        self.radioButton_sac_2.setText(QCoreApplication.translate("WindowPort", u"2", None))
        
        self.radioButton_sac_3 = QRadioButton(WindowPort)
        self.radioButton_sac_3.setObjectName(u"radioButton_sac_3")
        self.radioButton_sac_3.setGeometry(QRect(470, 200, 41, 18))
        self.radioButton_sac_3.setText(QCoreApplication.translate("WindowPort", u"3", None))
        self.radioButton_sac_3.setChecked(True)
        
        self.Sac_txt = self.creer_Qlabel(u"Sac_txt", QRect(430, 180, 47, 14), u"Sac n\u00b0")
        self.Chopper_txt = self.creer_Qlabel(u"Chopper_txt", QRect(400, 232, 47, 14), u"Chopper")
        
        self.spinBox_chopper = self.creer_QSpinBox(u"spinBox_chopper", QRect(450, 230, 42, 22), QSize(42, 16777215), 2, 8, 8)
        
        self.Widget_Nv_2 = QWidget(WindowPort)
        self.Widget_Nv_2.setObjectName(u"Widget_Nv_2")
        self.Widget_Nv_2.setGeometry(QRect(40, 280, 71, 61))
        
        self.label_7 = QLabel(self.Widget_Nv_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(0, 43, 71, 21))
        self.label_7.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Niv. 2</p></body></html>", None))
        
        self.label_8 = QLabel(self.Widget_Nv_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 71, 41))
        self.label_8.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Clef</p></body></html>", None))
        
        self.Widget_Nv_6 = QWidget(WindowPort)
        self.Widget_Nv_6.setObjectName(u"Widget_Nv_6")
        self.Widget_Nv_6.setGeometry(QRect(110, 280, 71, 61))
        
        self.label_9 = QLabel(self.Widget_Nv_6)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(0, 43, 71, 21))
        self.label_9.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Niv. 6</p></body></html>", None))
        
        self.label_10 = QLabel(self.Widget_Nv_6)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(0, 0, 71, 41))
        self.label_10.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Milkor</p></body></html>", None))
        
        self.Widget_Nv_10 = QWidget(WindowPort)
        self.Widget_Nv_10.setObjectName(u"Widget_Nv_10")
        self.Widget_Nv_10.setGeometry(QRect(180, 280, 71, 61))
        
        self.label_11 = QLabel(self.Widget_Nv_10)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(0, 43, 71, 21))
        self.label_11.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Niv. 10</p></body></html>", None))
        
        self.label_12 = QLabel(self.Widget_Nv_10)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(0, 0, 71, 41))
        self.label_12.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">H\u00e9lice</p></body></html>", None))
        
        self.Widget_Nv_13 = QWidget(WindowPort)
        self.Widget_Nv_13.setObjectName(u"Widget_Nv_13")
        self.Widget_Nv_13.setGeometry(QRect(250, 280, 71, 61))
        
        self.label_13 = QLabel(self.Widget_Nv_13)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(0, 43, 71, 21))
        self.label_13.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Niv. 13</p></body></html>", None))
        
        self.label_14 = QLabel(self.Widget_Nv_13)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(0, 0, 71, 41))
        self.label_14.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Foreuse</p></body></html>", None))
        
        self.Widget_Nv_16 = QWidget(WindowPort)
        self.Widget_Nv_16.setObjectName(u"Widget_Nv_16")
        self.Widget_Nv_16.setGeometry(QRect(320, 280, 71, 61))
        
        self.label_15 = QLabel(self.Widget_Nv_16)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(0, 43, 71, 21))
        self.label_15.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Niv. 16</p></body></html>", None))
        
        self.label_16 = QLabel(self.Widget_Nv_16)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(0, 0, 71, 41))
        self.label_16.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Harpon</p></body></html>", None))
        
        self.Widget_Nv_20 = QWidget(WindowPort)
        self.Widget_Nv_20.setObjectName(u"Widget_Nv_20")
        self.Widget_Nv_20.setGeometry(QRect(390, 280, 71, 61))
        
        self.label_17 = QLabel(self.Widget_Nv_20)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(0, 43, 71, 21))
        self.label_17.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Niv. 20</p></body></html>", None))
        
        self.label_18 = QLabel(self.Widget_Nv_20)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(0, 0, 71, 41))
        self.label_18.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\">Motif</p></body></html>", None))
        
        txt = (u"<!DOCTYPE HTML PUBLIC>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 Sable</p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 Pierre</p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 Bauxite</p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 Eau</p></body></html>")
        self.Ciment_ressource = self.creer_Qlabel(u"Ciment_ressource", QRect(200, 400, 71, 71), txt)
        
        self.Ciment_line = QFrame(WindowPort)
        self.Ciment_line.setObjectName(u"Ciment_line")
        self.Ciment_line.setGeometry(QRect(260, 400, 3, 61))
        self.Ciment_line.setFrameShadow(QFrame.Plain)
        self.Ciment_line.setLineWidth(2)
        self.Ciment_line.setFrameShape(QFrame.VLine)
        
        self.Ciment_nb = self.creer_Qlabel(u"Ciment_nb", QRect(280, 420, 61, 16), u"3 Ciments")
        
        txt=u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">B\u00e9tonni\u00e8re</span></p></body></html>"
        self.Jake_txt_2 = self.creer_Qlabel(u"Betonniere", QRect(150, 340, 221, 61), txt)
        
    
    def clicked_Jake(self, Jake):
        if Jake=="Livraison":
            items = [u"Boite de mat\u00e9riaux basiques vide", u"Boite d'outils vide", u"Sac R\u00e9frig\u00e9rant vide", u"Boite de mat\u00e9riaux rares vide",
                     u"Boite de mat\u00e9riaux basiques plein", u"Boite d'outils plein", u"Sac R\u00e9frig\u00e9rant plein", u"Boite de mat\u00e9riaux rares plein"]
            self.CB_Boite.clear()
            self.CB_zone.addItems(items)
        elif Jake=="Laboratoire":
            self.CB_Boite.clear()
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"", None))
        else:
            self.CB_Boite.clear()
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"", None))
            
        
    def total_sac(self):
        import math
        import LDOE_port
        import LDOE_variables
        
        if(self.radioButton_sac_1.isChecked()):
            tt=15+self.spinBox_chopper.value()
        elif(self.radioButton_sac_2.isChecked()):
            tt=20+self.spinBox_chopper.value()
        else:
            tt=25+self.spinBox_chopper.value()
        self.Place_sac_1.setText(QCoreApplication.translate("WindowPort", u"XX places dans le sac sur "+str(tt), None))
        self.Place_sac_2.setText(QCoreApplication.translate("WindowPort", u"XX places dans le sac sur "+str(tt), None))
        
        if (self.CB_Boite.currentIndex()<4):
            Place_sac=0
            for obj in LDOE_port.Boite_vide[self.CB_Boite.currentIndex()]:
                for i in range(len(LDOE_variables.max_01)):
                    if(obj in LDOE_variables.max_01[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_vide[self.CB_Boite.currentIndex()][obj]*self.spinBox_Nb_boite.value()/1)
                for i in range(len(LDOE_variables.max_20)):
                    if(obj in LDOE_variables.max_20[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_vide[self.CB_Boite.currentIndex()][obj]*self.spinBox_Nb_boite.value()/20)
                for i in range(len(LDOE_variables.max_50)):
                    if(obj in LDOE_variables.max_50[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_vide[self.CB_Boite.currentIndex()][obj]*self.spinBox_Nb_boite.value()/50)
            self.Place_sac_1.setText(QCoreApplication.translate("WindowPort", str(Place_sac)+u" places dans le sac sur "+str(tt), None))
        
        else:
            y=8
            
            Place_sac=0
            for obj in LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y]:
                for i in range(len(LDOE_variables.max_01)):
                    if(obj in LDOE_variables.max_01[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y][obj]*self.spinBox_Nb_boite.value()/1)
                for i in range(len(LDOE_variables.max_20)):
                    if(obj in LDOE_variables.max_20[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y][obj]*self.spinBox_Nb_boite.value()/20)
                for i in range(len(LDOE_variables.max_50)):
                    if(obj in LDOE_variables.max_50[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y][obj]*self.spinBox_Nb_boite.value()/50)
            self.Place_sac_1.setText(QCoreApplication.translate("WindowPort", str(Place_sac)+u" places dans le sac sur "+str(tt), None))
            
            Place_sac=0
            for obj in LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y+1]:
                for i in range(len(LDOE_variables.max_01)):
                    if(obj in LDOE_variables.max_01[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y+1][obj]*self.spinBox_Nb_boite.value()/1)
                for i in range(len(LDOE_variables.max_20)):
                    if(obj in LDOE_variables.max_20[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y+1][obj]*self.spinBox_Nb_boite.value()/20)
                for i in range(len(LDOE_variables.max_50)):
                    if(obj in LDOE_variables.max_50[i]):
                        Place_sac+=math.ceil(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y+1][obj]*self.spinBox_Nb_boite.value()/50)
            self.Place_sac_2.setText(QCoreApplication.translate("WindowPort", str(Place_sac)+u" places dans le sac sur "+str(tt), None))
        
        
    def total_object(self):
        import LDOE_port
        import LDOE_variables
        
        tempo=self.txt_before+self.txt_style
        
        if (self.CB_Boite.currentIndex()<4):
            i=0
            temp=tempo+"1."
            for obj in LDOE_port.Boite_vide[self.CB_Boite.currentIndex()]:
                temp+=" "+str(LDOE_port.Boite_vide[self.CB_Boite.currentIndex()][obj]*self.spinBox_Nb_boite.value())+" "+obj
                if(i==0):
                    temp+="</p>\n"+self.txt_style+"    "
                else:
                    temp+="</p></body></html>"
                i+=1
            self.Boite_1_txt.setText(QCoreApplication.translate("WindowPort", temp, None))
            temp=self.txt_before+self.txt_style+"2. XX object1</p\n"+self.txt_style+"    XX object2</p></body></html>"
            self.Boite_2_txt.setText(QCoreApplication.translate("WindowPort", temp, None))
        else:
            i=0
            y=8
            temp=tempo+"1."
            for obj in LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y]:
                temp+=" "+str(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y][obj]*self.spinBox_Nb_boite.value())+" "+obj
                if(i==0) or (i==1):
                    temp+="</p>\n"+self.txt_style+"    "
                else:
                    temp+="</p></body></html>"
                i+=1
            self.Boite_1_txt.setText(QCoreApplication.translate("WindowPort", temp, None))
            i=0
            temp=tempo+"2."
            for obj in LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y+1]:
                temp+=" "+str(LDOE_port.Boite_pleine[2*self.CB_Boite.currentIndex()-y+1][obj]*self.spinBox_Nb_boite.value())+" "+obj
                if(i==0) or (i==1):
                    temp+="</p>\n"+self.txt_style+"    "
                else:
                    temp+="</p></body></html>"
                i+=1
            self.Boite_2_txt.setText(QCoreApplication.translate("WindowPort", temp, None))

        
    def total(self):
        self.total_object()
        self.total_sac()    



if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui= Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

