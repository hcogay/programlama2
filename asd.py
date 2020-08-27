# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 21:54:15 2020

@author: Hasan
"""
import sys
import requests
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5 import *
import mysql.connector

headers_param={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36"}
link=input("Url giriniz")
link=requests.get(link,headers=headers_param)
b=link.content
soup=BeautifulSoup(b,"lxml")
urunler=soup.find("h1",{"id":"sp-title"})
for urun in urunler:
    pass
    
fiyatlar=soup.find("span",{"id":"sp-price-highPrice"})
for fiyat in fiyatlar: 
    pass  
class odev(QDialog):
    def __init__(self, ebeveyn=None):
        super(odev,self).__init__(ebeveyn)
        grid=QGridLayout()
        grid.addWidget(QLabel("URL: "),0,0)
        grid.addWidget(QLabel("Fiyat:"),1,0)
        grid.addWidget(QLabel("Ürün: "),2,0)
        grid.addWidget(QLabel(fiyat),1,1)
        grid.addWidget(QLabel(urun),2,1)
        self.link=QLineEdit()
        grid.addWidget(self.link,0,1)
        hesapla=QPushButton("Kaydet")
        grid.addWidget(hesapla,3,1)
        hesapla.clicked.connect(self.kaydet)
        grid.addWidget(hesapla,3,1)
        self.setLayout(grid)
        self.setWindowTitle("2019469079")

    def kaydet(self):
        url=(self.link.text())
        baglanti=mysql.connector.connect(user="root",password="",host="127.0.0.1",database="prog2odev")
        isaretci=baglanti.cursor()
        isaretci.execute('''INSERT INTO odev (url) VALUES("%s")'''%(url))
        baglanti.commit()
        baglanti.close
        

    
   
   
uyg=QApplication([])
pencere=odev()
pencere.show()
uyg.exec_()
