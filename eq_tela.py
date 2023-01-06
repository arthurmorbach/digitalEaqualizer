# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'eq_tela.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QInputDialog, QLineEdit, QFileDialog
from equalizador import equalizador, closew
import matplotlib as plt

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(999, 687)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        
        self.f1 = QtWidgets.QSlider(self.centralwidget)
        self.f1.setGeometry(QtCore.QRect(20, 180, 41, 171))
        self.f1.setMinimum(-120)
        self.f1.setMaximum(120)
        self.f1.setSingleStep(1)
        self.f1.setOrientation(QtCore.Qt.Vertical)
        self.f1.setObjectName("f1")
        self.f1.valueChanged.connect(self.freq_values_handler)
        self.f1.valueChanged.connect(self.show_gain_values)
        
        self.f2 = QtWidgets.QSlider(self.centralwidget)
        self.f2.setGeometry(QtCore.QRect(90, 180, 41, 171))
        self.f2.setMinimum(-120)
        self.f2.setMaximum(120)
        self.f2.setOrientation(QtCore.Qt.Vertical)
        self.f2.setObjectName("f2")
        self.f2.valueChanged.connect(self.freq_values_handler)
        self.f2.valueChanged.connect(self.show_gain_values)
        
        self.f3 = QtWidgets.QSlider(self.centralwidget)
        self.f3.setGeometry(QtCore.QRect(160, 180, 41, 171))
        self.f3.setMinimum(-120)
        self.f3.setMaximum(120)
        self.f3.setOrientation(QtCore.Qt.Vertical)
        self.f3.setObjectName("f3")
        self.f3.valueChanged.connect(self.freq_values_handler)
        self.f3.valueChanged.connect(self.show_gain_values)
        
        self.f4 = QtWidgets.QSlider(self.centralwidget)
        self.f4.setGeometry(QtCore.QRect(230, 180, 41, 171))
        self.f4.setMinimum(-120)
        self.f4.setMaximum(120)
        self.f4.setProperty("value", 0)
        self.f4.setOrientation(QtCore.Qt.Vertical)
        self.f4.setObjectName("f4")
        self.f4.valueChanged.connect(self.freq_values_handler)
        self.f4.valueChanged.connect(self.show_gain_values)
        
        self.f5 = QtWidgets.QSlider(self.centralwidget)
        self.f5.setGeometry(QtCore.QRect(300, 180, 41, 171))
        self.f5.setMinimum(-120)
        self.f5.setMaximum(120)
        self.f5.setOrientation(QtCore.Qt.Vertical)
        self.f5.setObjectName("f5")
        self.f5.valueChanged.connect(self.freq_values_handler)
        self.f5.valueChanged.connect(self.show_gain_values)
        
        self.f6 = QtWidgets.QSlider(self.centralwidget)
        self.f6.setGeometry(QtCore.QRect(370, 180, 41, 171))
        self.f6.setMinimum(-120)
        self.f6.setMaximum(120)
        self.f6.setOrientation(QtCore.Qt.Vertical)
        self.f6.setObjectName("f6")
        self.f6.valueChanged.connect(self.freq_values_handler)
        self.f6.valueChanged.connect(self.show_gain_values)
        
        self.f7 = QtWidgets.QSlider(self.centralwidget)
        self.f7.setGeometry(QtCore.QRect(440, 180, 41, 171))
        self.f7.setMinimum(-120)
        self.f7.setMaximum(120)
        self.f7.setOrientation(QtCore.Qt.Vertical)
        self.f7.setObjectName("f7")
        self.f7.valueChanged.connect(self.freq_values_handler)
        self.f7.valueChanged.connect(self.show_gain_values)
        
        self.f8 = QtWidgets.QSlider(self.centralwidget)
        self.f8.setGeometry(QtCore.QRect(510, 180, 41, 171))
        self.f8.setMinimum(-120)
        self.f8.setMaximum(120)
        self.f8.setSingleStep(1)
        self.f8.setOrientation(QtCore.Qt.Vertical)
        self.f8.setObjectName("f8")
        self.f8.valueChanged.connect(self.freq_values_handler)
        self.f8.valueChanged.connect(self.show_gain_values)
        
        self.f9 = QtWidgets.QSlider(self.centralwidget)
        self.f9.setGeometry(QtCore.QRect(580, 180, 41, 171))
        self.f9.setMinimum(-120)
        self.f9.setMaximum(120)
        self.f9.setOrientation(QtCore.Qt.Vertical)
        self.f9.setObjectName("f9")
        self.f9.valueChanged.connect(self.freq_values_handler)
        self.f9.valueChanged.connect(self.show_gain_values)
        
        self.f10 = QtWidgets.QSlider(self.centralwidget)
        self.f10.setGeometry(QtCore.QRect(650, 180, 41, 171))
        self.f10.setMinimum(-120)
        self.f10.setMaximum(120)
        self.f10.setOrientation(QtCore.Qt.Vertical)
        self.f10.setObjectName("f10")
        self.f10.valueChanged.connect(self.freq_values_handler)
        self.f10.valueChanged.connect(self.show_gain_values)
        
        self.f11 = QtWidgets.QSlider(self.centralwidget)
        self.f11.setGeometry(QtCore.QRect(720, 180, 41, 171))
        self.f11.setMinimum(-120)
        self.f11.setMaximum(120)
        self.f11.setProperty("value", 0)
        self.f11.setOrientation(QtCore.Qt.Vertical)
        self.f11.setObjectName("f11")
        self.f11.valueChanged.connect(self.freq_values_handler)
        self.f11.valueChanged.connect(self.show_gain_values)
        
        self.f12 = QtWidgets.QSlider(self.centralwidget)
        self.f12.setGeometry(QtCore.QRect(790, 180, 41, 171))
        self.f12.setMinimum(-120)
        self.f12.setMaximum(120)
        self.f12.setOrientation(QtCore.Qt.Vertical)
        self.f12.setObjectName("f12")
        self.f12.valueChanged.connect(self.freq_values_handler)
        self.f12.valueChanged.connect(self.show_gain_values)
        
        self.f13 = QtWidgets.QSlider(self.centralwidget)
        self.f13.setGeometry(QtCore.QRect(860, 180, 41, 171))
        self.f13.setMinimum(-120)
        self.f13.setMaximum(120)
        self.f13.setOrientation(QtCore.Qt.Vertical)
        self.f13.setObjectName("f13")
        self.f13.valueChanged.connect(self.freq_values_handler)
        self.f13.valueChanged.connect(self.show_gain_values)
        
        self.f14 = QtWidgets.QSlider(self.centralwidget)
        self.f14.setGeometry(QtCore.QRect(930, 180, 41, 171))
        self.f14.setMinimum(-120)
        self.f14.setMaximum(120)
        self.f14.setOrientation(QtCore.Qt.Vertical)
        self.f14.setObjectName("f14")
        self.f14.valueChanged.connect(self.freq_values_handler)
        self.f14.valueChanged.connect(self.show_gain_values)
        



        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(330, 20, 361, 81))
        font = QtGui.QFont()
        font.setPointSize(26)
        self.label.setFont(font)
        self.label.setObjectName("label")
        
        
        
        self.lcd1 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd1.setGeometry(QtCore.QRect(20, 360, 41, 21))
        self.lcd1.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd1.setObjectName("lcd1")
        self.lcd1.colorCount()
        
        self.lcd2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd2.setGeometry(QtCore.QRect(90, 360, 41, 21))
        self.lcd2.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd2.setObjectName("lcd2")
        
        self.lcd3 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd3.setGeometry(QtCore.QRect(160, 360, 41, 21))
        self.lcd3.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd3.setObjectName("lcd3")
        
        self.lcd4 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd4.setGeometry(QtCore.QRect(230, 360, 41, 21))
        self.lcd4.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd4.setObjectName("lcd4")
        
        self.lcd5 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd5.setGeometry(QtCore.QRect(300, 360, 41, 21))
        self.lcd5.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd5.setObjectName("lcd5")
        
        self.lcd6 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd6.setGeometry(QtCore.QRect(370, 360, 41, 21))
        self.lcd6.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd6.setObjectName("lcd6")
        
        self.lcd7 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd7.setGeometry(QtCore.QRect(440, 360, 41, 21))
        self.lcd7.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd7.setObjectName("lcd7")
        
        self.lcd8 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd8.setGeometry(QtCore.QRect(510, 360, 41, 21))
        self.lcd8.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd8.setObjectName("lcd8")
        
        self.lcd9 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd9.setGeometry(QtCore.QRect(580, 360, 41, 21))
        self.lcd9.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd9.setObjectName("lcd9")
        
        self.lcd10 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd10.setGeometry(QtCore.QRect(650, 360, 41, 21))
        self.lcd10.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd10.setObjectName("lcd10")
        
        self.lcd11 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd11.setGeometry(QtCore.QRect(720, 360, 41, 21))
        self.lcd11.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd11.setObjectName("lcd11")
        
        self.lcd12 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd12.setGeometry(QtCore.QRect(790, 360, 41, 21))
        self.lcd12.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd12.setObjectName("lcd12")
        
        self.lcd13 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd13.setGeometry(QtCore.QRect(860, 360, 41, 21))
        self.lcd13.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd13.setObjectName("lcd13")
        
        self.lcd14 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcd14.setGeometry(QtCore.QRect(930, 360, 41, 21))
        self.lcd14.setStyleSheet("QLCDNumber{\n"
"    color: rgb(0, 0, 0);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.lcd14.setObjectName("lcd14")
        
        
        self.file_name = QtWidgets.QLineEdit(self.centralwidget)
        self.file_name.setGeometry(QtCore.QRect(730, 470, 211, 22))
        self.file_name.setObjectName("file_name")
        self.file_name.setPlaceholderText("Enter your output file name. (.wav)")
        

        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(780, 500, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
               
        
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(90, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(160, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_7.setFont(font)
        self.label_7.setObjectName("label_7")
        
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(300, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(230, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(370, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_8.setFont(font)
        self.label_8.setObjectName("label_8")
        
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(720, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_9.setFont(font)
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(650, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_10.setFont(font)
        self.label_10.setObjectName("label_10")
        
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(790, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_11.setFont(font)
        self.label_11.setObjectName("label_11")
        
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(510, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_12.setFont(font)
        self.label_12.setObjectName("label_12")
        
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(440, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_13.setFont(font)
        self.label_13.setObjectName("label_13")
        
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(580, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(930, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_15.setFont(font)
        self.label_15.setObjectName("label_15")
        
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(860, 140, 51, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_16.setFont(font)
        self.label_16.setObjectName("label_16")
        
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(60, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_17.setFont(font)
        self.label_17.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_17.setAutoFillBackground(False)
        self.label_17.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_17.setObjectName("label_17")
        
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(130, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_18.setFont(font)
        self.label_18.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_18.setAutoFillBackground(False)
        self.label_18.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_18.setObjectName("label_18")
        
        
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(200, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_19.setFont(font)
        self.label_19.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_19.setAutoFillBackground(False)
        self.label_19.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_19.setObjectName("label_19")
        
        
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(270, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_20.setFont(font)
        self.label_20.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_20.setAutoFillBackground(False)
        self.label_20.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_20.setObjectName("label_20")
        
        
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(340, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_21.setFont(font)
        self.label_21.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_21.setAutoFillBackground(False)
        self.label_21.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_21.setObjectName("label_21")
        
        
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(410, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_22.setFont(font)
        self.label_22.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_22.setAutoFillBackground(False)
        self.label_22.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_22.setObjectName("label_22")
        
        
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(550, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_23.setFont(font)
        self.label_23.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_23.setAutoFillBackground(False)
        self.label_23.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_23.setObjectName("label_23")
        
        
        self.label_24 = QtWidgets.QLabel(self.centralwidget)
        self.label_24.setGeometry(QtCore.QRect(620, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_24.setFont(font)
        self.label_24.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_24.setAutoFillBackground(False)
        self.label_24.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_24.setObjectName("label_24")
        
        
        self.label_25 = QtWidgets.QLabel(self.centralwidget)
        self.label_25.setGeometry(QtCore.QRect(760, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_25.setFont(font)
        self.label_25.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_25.setAutoFillBackground(False)
        self.label_25.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_25.setObjectName("label_25")
        
        
        self.label_26 = QtWidgets.QLabel(self.centralwidget)
        self.label_26.setGeometry(QtCore.QRect(480, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_26.setFont(font)
        self.label_26.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_26.setAutoFillBackground(False)
        self.label_26.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_26.setObjectName("label_26")
        
        
        self.label_27 = QtWidgets.QLabel(self.centralwidget)
        self.label_27.setGeometry(QtCore.QRect(830, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_27.setFont(font)
        self.label_27.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_27.setAutoFillBackground(False)
        self.label_27.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_27.setObjectName("label_27")
        
        
        self.label_28 = QtWidgets.QLabel(self.centralwidget)
        self.label_28.setGeometry(QtCore.QRect(690, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_28.setFont(font)
        self.label_28.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_28.setAutoFillBackground(False)
        self.label_28.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_28.setObjectName("label_28")
        
        
        self.label_29 = QtWidgets.QLabel(self.centralwidget)
        self.label_29.setGeometry(QtCore.QRect(900, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_29.setFont(font)
        self.label_29.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_29.setAutoFillBackground(False)
        self.label_29.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_29.setObjectName("label_29")
        
        
        self.label_30 = QtWidgets.QLabel(self.centralwidget)
        self.label_30.setGeometry(QtCore.QRect(970, 360, 21, 21))
        font = QtGui.QFont()
        font.setFamily("MS Gothic")
        font.setPointSize(9)
        self.label_30.setFont(font)
        self.label_30.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_30.setAutoFillBackground(False)
        self.label_30.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 0, 0);\n"
"}")
        self.label_30.setObjectName("label_30")
        
        
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(780, 400, 161, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.ready = QtWidgets.QLabel(self.centralwidget)
        self.ready.setGeometry(QtCore.QRect(780, 560, 161, 41))
        self.ready.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.ready.setText("")
        self.ready.setObjectName("ready")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionOpen_File = QtWidgets.QAction(MainWindow)
        self.actionOpen_File.setObjectName("actionOpen_File")
        
        self.processDone = 0

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Digital Equalizer"))
        self.pushButton.setText(_translate("MainWindow", "Equalize"))
        self.label_3.setText(_translate("MainWindow", "100Hz"))
        self.label_4.setText(_translate("MainWindow", "400Hz"))
        self.label_7.setText(_translate("MainWindow", "600Hz"))
        self.label_5.setText(_translate("MainWindow", "2kHz"))
        self.label_6.setText(_translate("MainWindow", "1kHz"))
        self.label_8.setText(_translate("MainWindow", "3kHz"))
        self.label_9.setText(_translate("MainWindow", "12kHz"))
        self.label_10.setText(_translate("MainWindow", "10kHz"))
        self.label_11.setText(_translate("MainWindow", "15kHz"))
        self.label_12.setText(_translate("MainWindow", "5kHz"))
        self.label_13.setText(_translate("MainWindow", "4kHz"))
        self.label_14.setText(_translate("MainWindow", "8kHz"))
        self.label_15.setText(_translate("MainWindow", "19kHz"))
        self.label_16.setText(_translate("MainWindow", "17kHz"))
        self.label_17.setText(_translate("MainWindow", "dB"))
        self.label_18.setText(_translate("MainWindow", "dB"))
        self.label_19.setText(_translate("MainWindow", "dB"))
        self.label_20.setText(_translate("MainWindow", "dB"))
        self.label_21.setText(_translate("MainWindow", "dB"))
        self.label_22.setText(_translate("MainWindow", "dB"))
        self.label_23.setText(_translate("MainWindow", "dB"))
        self.label_24.setText(_translate("MainWindow", "dB"))
        self.label_25.setText(_translate("MainWindow", "dB"))
        self.label_26.setText(_translate("MainWindow", "dB"))
        self.label_27.setText(_translate("MainWindow", "dB"))
        self.label_28.setText(_translate("MainWindow", "dB"))
        self.label_29.setText(_translate("MainWindow", "dB"))
        self.label_30.setText(_translate("MainWindow", "dB"))
        self.pushButton_2.setText(_translate("MainWindow", "Load File"))
        self.actionOpen_File.setText(_translate("MainWindow", "Open"))
        
        self.pushButton.clicked.connect(self.pushButton_handler)
        self.pushButton_2.clicked.connect(self.pushButton_2_handler)
        self.pushButton_2.clicked.connect(self.resetSys)
        
    
    def pushButton_handler(self,processDone):
        out_fileName = self.file_name.text()
        print(out_fileName)
        print("Equalize button was pressed")
        self.processDone = equalizador(self.path, out_fileName,self.G1, self.G2, self.G3, self.G4, self.G5, self.G6, self.G7, self.G8, self.G9, self.G10, self.G11, self.G12, self.G13, self.G14) == 1
        if self.processDone == 1:
            self.ready.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(0, 255, 0);\n"
"}")
        self.ready.setText("")
        
    def pushButton_2_handler(self):
        print("Load File button was pressed")
        self.open_dialog_box()
        
    def open_dialog_box(self):   
        filename = QFileDialog.getOpenFileName(None,None,None,'WAV files (*.wav)')
        self.path = filename[0]
        print(self.path)
        
    def freq_values_handler(self):
        self.G1 = float(self.f1.value())/10
        self.G2 = float(self.f2.value())/10
        self.G3 = float(self.f3.value())/10
        self.G4 = float(self.f4.value())/10
        self.G5 = float(self.f5.value())/10
        self.G6 = float(self.f6.value())/10
        self.G7 = float(self.f7.value())/10
        self.G8 = float(self.f8.value())/10
        self.G9 = float(self.f9.value())/10
        self.G10 = float(self.f10.value())/10
        self.G11 = float(self.f11.value())/10
        self.G12 = float(self.f12.value())/10
        self.G13 = float(self.f13.value())/10
        self.G14 = float(self.f14.value())/10

    
    def show_gain_values(self):
        self.lcd1.display(self.G1)
        self.lcd2.display(self.G2)
        self.lcd3.display(self.G3)
        self.lcd4.display(self.G4)
        self.lcd5.display(self.G5)
        self.lcd6.display(self.G6)
        self.lcd7.display(self.G7)
        self.lcd8.display(self.G8)
        self.lcd9.display(self.G9)
        self.lcd10.display(self.G10)
        self.lcd11.display(self.G11)
        self.lcd12.display(self.G12)
        self.lcd13.display(self.G13)
        self.lcd14.display(self.G14)
        
    def resetSys(self):
        self.processDone = 0
        self.ready.setStyleSheet("QLabel{\n"
"    color: rgb(255, 255, 255);    \n"
"    background-color: rgb(255, 255, 255);\n"
"}")
        self.ready.setText("")
        closew()
        
        
        
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
