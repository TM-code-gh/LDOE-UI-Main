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

class Ui_MainWindow(object):
    # setupUi
    def setupUi(self, MainWindow):
        if MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(530, 519)
        #MainWindow.resize(QDesktopWidget().width()*0.5, QDesktopWidget().height()*0.5)
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        
        self.Date_txt = QLabel(self.centralwidget)
        self.Date_txt.setObjectName(u"Date_txt")
        self.Date_txt.setGeometry(QRect(10, 10, 110, 16))
        self.Date_txt.setText(QCoreApplication.translate("MainWindow", u"Date (JJ/MM) :", None))
        
        self.Date_val = QLabel(self.centralwidget)
        self.Date_val.setObjectName(u"Date_val")
        self.Date_val.setGeometry(QRect(120, 10, 71, 16))
        self.Date_val.setText(QCoreApplication.translate("MainWindow", JJ_MM, None))
        
        self.Code_txt = QLabel(self.centralwidget)
        self.Code_txt.setObjectName(u"Code_txt")
        self.Code_txt.setGeometry(QRect(360, 10, 100, 16))
        self.Code_txt.setText(QCoreApplication.translate("MainWindow", u"Code Bunker : ", None))
        
        self.Code_val = QLabel(self.centralwidget)
        self.Code_val.setObjectName(u"Code_val")
        self.Code_val.setGeometry(QRect(470, 10, 51, 16))
        self.Code_val.setText(QCoreApplication.translate("MainWindow", code, None))
        
        self.label_zone = QLabel(self.centralwidget)
        self.label_zone.setObjectName(u"label_zone")
        self.label_zone.setGeometry(QRect(165, 70, 200, 61))
        self.label_zone.setStatusTip(QCoreApplication.translate("MainWindow", u"Choisir une zone à découvrir.", None))
        self.label_zone.setText(QCoreApplication.translate("MainWindow", u"Choisir la zone", None))
        
        font = QFont()
        font.setFamily(u"DejaVu Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.label_zone.setFont(font)
        
        self.CB_zone = QComboBox(self.centralwidget)
        self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Pin\u00e8des", None))
        self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Cr\u00eate de calcaire", None))
        self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Station essence", None))
        self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Port", None))
        self.CB_zone.setObjectName(u"CB_zone")
        self.CB_zone.setGeometry(QRect(150, 150, 201, 31))
        
        self.CB_couleur = QComboBox(self.centralwidget)
        self.CB_couleur.addItem(QCoreApplication.translate("MainWindow", u"Vert", None))
        self.CB_couleur.addItem(QCoreApplication.translate("MainWindow", u"Jaune", None))
        self.CB_couleur.addItem(QCoreApplication.translate("MainWindow", u"Rouge", None))
        self.CB_couleur.addItem(QCoreApplication.translate("MainWindow", u"Bleu", None))
        self.CB_couleur.setObjectName(u"CB_couleur")
        self.CB_couleur.setGeometry(QRect(40, 150, 101, 31))
        self.CB_couleur.currentTextChanged.connect(lambda: self.clicked_couleur(str(self.CB_couleur.currentText())))
        
        self.Boutton_zone = QPushButton(self.centralwidget)
        self.Boutton_zone.setObjectName(u"Boutton_zone")
        self.Boutton_zone.setGeometry(QRect(400, 150, 91, 31))
        self.Boutton_zone.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        self.Boutton_zone.clicked.connect(lambda: self.clicked_bt_zone(str(self.CB_zone.currentText())))
        
        self.label_ressource = QLabel(self.centralwidget)
        self.label_ressource.setObjectName(u"label_ressource")
        self.label_ressource.setGeometry(QRect(130, 200, 270, 61))
        self.label_ressource.setFont(font)
        self.label_ressource.setStatusTip(QCoreApplication.translate(
            "MainWindow", u"Taper la ressource que vous souhaitez trouver. Il en sortira les lieux o\u00f9 la trouver.", None))
        self.label_ressource.setText(QCoreApplication.translate("MainWindow", u"Chercher Ressource", None))
        
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(40, 270, 311, 31))
        
        self.Button_ressource = QPushButton(self.centralwidget)
        self.Button_ressource.setObjectName(u"Button_ressource")
        self.Button_ressource.setGeometry(QRect(400, 270, 91, 31))
        self.Button_ressource.setText(QCoreApplication.translate("MainWindow", u"OK", None))
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 530, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        QMetaObject.connectSlotsByName(MainWindow)      
        
    def clicked_couleur(self, couleur):
        if couleur=="Vert":
            self.CB_zone.clear()
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Pin\u00e8des", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Cr\u00eate de calcaire", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Station essence", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Port", None))
        elif couleur=="Jaune":
            self.CB_zone.clear()
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Bosquet de pins", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Falaises calcaires", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"H\u00f4tel", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Brousses de ch\u00eane", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Pied de montagne Bois\u00e9", None))
        elif couleur=="Rouge":
            self.CB_zone.clear()
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Bois de Pin", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Fl\u00e8ches de calcaires", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"For\u00eat infect\u00e9e", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Vieille Ferme", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Bunker Alpha", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Bunker Bravo", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Commissariat de police", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Ch\u00eaneraie", None))
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"For\u00eat gel\u00e9e", None))
        else:
            self.CB_zone.clear()
            self.CB_zone.addItem(QCoreApplication.translate("MainWindow", u"Tour de guet", None))
        
    def clicked_bt_zone(self, zone):
        if zone=="Pin\u00e8des":
            self.w=Ui_WindowZone()
            self.w.setupUi(self.w)
            self.w.show()
            
        elif zone=="Port":
            self.w=Ui_WindowZone()
            self.w.setupUi(self.w)
            self.w.setupPort(self.w)
            self.w.show()
            
        else:
            print(zone)
            
        
class Ui_WindowZone(QWidget):
    
    def setupUi(self, WindowZone):
        if WindowZone.objectName():
            WindowZone.setObjectName(u"WindowZone")
        WindowZone.setEnabled(True)
        WindowZone.resize(530, 519)
        #MainWindow.resize(QDesktopWidget().width()*0.5, QDesktopWidget().height()*0.5)
        WindowZone.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        

    def setupPort(self, WindowPort):
        
        self.txt_before="<!DOCTYPE HTML PUBLIC>\n <html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n p, li { white-space: pre-wrap; }\n </style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
        self.txt_style="<p style=\" margin-top:1px; margin-bottom:1px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">"
        
        WindowPort.setWindowTitle(QCoreApplication.translate("WindowPort", u"WindowPort", None))
        
        self.Code_txt = QLabel(WindowPort)
        self.Code_txt.setObjectName(u"Code_txt")
        self.Code_txt.setGeometry(QRect(380, 10, 71, 16))
        self.Code_txt.setText(QCoreApplication.translate("WindowPort", u"Code Bunker : ", None))
        
        self.Code_val = QLabel(WindowPort)
        self.Code_val.setObjectName(u"Code_val")
        self.Code_val.setGeometry(QRect(470, 10, 51, 16))
        self.Code_val.setText(QCoreApplication.translate("WindowPort", code, None))
        
        self.Date_txt = QLabel(WindowPort)
        self.Date_txt.setObjectName(u"Date_txt")
        self.Date_txt.setGeometry(QRect(10, 10, 81, 16))
        self.Date_txt.setText(QCoreApplication.translate("MainWindow", u"Date (JJ/MM) :", None))
        
        self.Date_val = QLabel(WindowPort)
        self.Date_val.setObjectName(u"Date_val")
        self.Date_val.setGeometry(QRect(90, 10, 71, 16))
        self.Date_val.setText(QCoreApplication.translate("WindowPort", JJ_MM, None))
        
        self.Port_txt = QLabel(WindowPort)
        self.Port_txt.setObjectName(u"Port_txt")
        self.Port_txt.setGeometry(QRect(150, 30, 221, 61))
        self.Port_txt.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p><span style=\" font-size:14pt;\">D\u00e9couvrir la zone du Port</span></p></body></html>", None))
        
        self.CB_Boite = QComboBox(WindowPort)
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux basiques vide", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite d'outils vide", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Sac R\u00e9frig\u00e9rant vide", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux rares vide", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux basiques plein", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite d'outils plein", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Sac R\u00e9frig\u00e9rant plein", None))
        self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux rares plein", None))
        self.CB_Boite.setObjectName(u"CB_Boite")
        self.CB_Boite.setGeometry(QRect(180, 130, 191, 31))
        
        self.Jake_txt = QLabel(WindowPort)
        self.Jake_txt.setObjectName(u"Jake_txt")
        self.Jake_txt.setGeometry(QRect(150, 70, 221, 61))
        self.Jake_txt.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">Jake</span></p></body></html>", None))
        
        self.CB_Livraison = QComboBox(WindowPort)
        self.CB_Livraison.addItem(QCoreApplication.translate("WindowPort", u"Livraison", None))
        self.CB_Livraison.addItem(QCoreApplication.translate("WindowPort", u"Laboratoire", None))
        self.CB_Livraison.addItem(QCoreApplication.translate("WindowPort", u"Verrouill\u00e9(e)", None))
        self.CB_Livraison.setObjectName(u"CB_Livraison")
        self.CB_Livraison.setGeometry(QRect(40, 130, 131, 31))
        self.CB_Livraison.currentTextChanged.connect(lambda: self.clicked_Jake(str(self.CB_Livraison.currentText())))
        
        self.Bt_Actualiser_Boite = QPushButton(WindowPort)
        self.Bt_Actualiser_Boite.setObjectName(u"Bt_Actualiser_Boite")
        self.Bt_Actualiser_Boite.setGeometry(QRect(430, 130, 91, 31))
        self.Bt_Actualiser_Boite.setText(QCoreApplication.translate("WindowPort", u"Actualiser", None))
        self.Bt_Actualiser_Boite.clicked.connect(lambda: self.total())
        
        self.Nb_boite_txt = QLabel(WindowPort)
        self.Nb_boite_txt.setObjectName(u"Nb_boite_txt")
        self.Nb_boite_txt.setGeometry(QRect(380, 125, 47, 14))
        self.Nb_boite_txt.setText(QCoreApplication.translate("WindowPort", u"NB Boite", None))
        
        self.spinBox_Nb_boite = QSpinBox(WindowPort)
        self.spinBox_Nb_boite.setObjectName(u"spinBox_Nb_boite")
        self.spinBox_Nb_boite.setGeometry(QRect(380, 140, 42, 22))
        self.spinBox_Nb_boite.setMaximumSize(QSize(42, 16777215))
        self.spinBox_Nb_boite.setMinimum(1)
        self.spinBox_Nb_boite.setMaximum(50)
        self.spinBox_Nb_boite.setValue(8)
        
        temp=self.txt_before+self.txt_style+"1. XX object1</p\n"+self.txt_style+"    XX object2</p></body></html>"
        
        self.Boite_1_txt = QLabel(WindowPort)
        self.Boite_1_txt.setObjectName(u"Boite_1_txt")
        self.Boite_1_txt.setGeometry(QRect(40, 180, 161, 51))
        self.Boite_1_txt.setText(QCoreApplication.translate("WindowPort", temp, None))
        
        temp=self.txt_before+self.txt_style+"2. XX object1</p\n"+self.txt_style+"    XX object2</p></body></html>"
        
        self.Boite_2_txt = QLabel(WindowPort)
        self.Boite_2_txt.setObjectName(u"Boite_2_txt")
        self.Boite_2_txt.setGeometry(QRect(40, 225, 161, 51))
        self.Boite_2_txt.setText(QCoreApplication.translate("WindowPort", temp, None))
        
        self.Place_sac_1 = QLabel(WindowPort)
        self.Place_sac_1.setObjectName(u"Place_sac_1")
        self.Place_sac_1.setGeometry(QRect(200, 180, 161, 21))
        self.Place_sac_1.setText(QCoreApplication.translate("WindowPort", u"XX places dans le sac sur XX", None))
        
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
        
        self.Sac_txt = QLabel(WindowPort)
        self.Sac_txt.setObjectName(u"Sac_txt")
        self.Sac_txt.setGeometry(QRect(430, 180, 47, 14))
        self.Sac_txt.setText(QCoreApplication.translate("WindowPort", u"Sac n\u00b0", None))
        
        self.Place_sac_2 = QLabel(WindowPort)
        self.Place_sac_2.setObjectName(u"Place_sac_2")
        self.Place_sac_2.setGeometry(QRect(200, 220, 161, 21))
        self.Place_sac_2.setText(QCoreApplication.translate("WindowPort", u"XX places dans le sac sur XX", None))
        
        self.Chopper_txt = QLabel(WindowPort)
        self.Chopper_txt.setObjectName(u"Chopper_txt")
        self.Chopper_txt.setGeometry(QRect(400, 232, 47, 14))
        self.Chopper_txt.setText(QCoreApplication.translate("WindowPort", u"Chopper", None))
        
        self.spinBox_chopper = QSpinBox(WindowPort)
        self.spinBox_chopper.setObjectName(u"spinBox_chopper")
        self.spinBox_chopper.setGeometry(QRect(450, 230, 42, 22))
        self.spinBox_chopper.setMaximumSize(QSize(42, 16777215))
        self.spinBox_chopper.setMinimum(2)
        self.spinBox_chopper.setMaximum(8)
        self.spinBox_chopper.setValue(8)
        
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
        
        self.Ciment_ressource = QLabel(WindowPort)
        self.Ciment_ressource.setObjectName(u"Ciment_ressource")
        self.Ciment_ressource.setGeometry(QRect(200, 400, 71, 71))
        self.Ciment_ressource.setText(QCoreApplication.translate("WindowPort", u"<!DOCTYPE HTML PUBLIC>\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">15 Sable</p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">20 Pierre</p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">5 Bauxite</p>\n"
"<p style=\" margin-top:2px; margin-bottom:2px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">10 Eau</p></body></html>", None))
        
        self.Ciment_line = QFrame(WindowPort)
        self.Ciment_line.setObjectName(u"Ciment_line")
        self.Ciment_line.setGeometry(QRect(260, 400, 3, 61))
        self.Ciment_line.setFrameShadow(QFrame.Plain)
        self.Ciment_line.setLineWidth(2)
        self.Ciment_line.setFrameShape(QFrame.VLine)
        
        self.Ciment_nb = QLabel(WindowPort)
        self.Ciment_nb.setObjectName(u"Ciment_nb")
        self.Ciment_nb.setGeometry(QRect(280, 420, 61, 16))
        self.Ciment_nb.setText(QCoreApplication.translate("WindowPort", u"3 Ciments", None))
        
        self.Jake_txt_2 = QLabel(WindowPort)
        self.Jake_txt_2.setObjectName(u"Betonniere")
        self.Jake_txt_2.setGeometry(QRect(150, 340, 221, 61))
        self.Jake_txt_2.setText(QCoreApplication.translate("WindowPort", u"<html><head/><body><p align=\"center\"><span style=\" font-size:14pt;\">B\u00e9tonni\u00e8re</span></p></body></html>", None))
        
    
    def clicked_Jake(self, Jake):
        if Jake=="Livraison":
            self.CB_Boite.clear()
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux basiques vide", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite d'outils vide", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Sac R\u00e9frig\u00e9rant vide", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux rares vide", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux basiques plein", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite d'outils plein", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Sac R\u00e9frig\u00e9rant plein", None))
            self.CB_Boite.addItem(QCoreApplication.translate("WindowPort", u"Boite de mat\u00e9riaux rares plein", None))
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

