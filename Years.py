# -------------------------------------------------------------------------------
# Name:             Years.py
# Purpose:          Calculate the years between two given dates
#
# Author:           Jeffreaux
#
# Created:          11July24
#
# Required Packages:    PyQt5, PyQt5-Tools
# -------------------------------------------------------------------------------

from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QAction, QDateEdit, QLabel
from PyQt5 import uic
from datetime import date

# from dateutil.relativedelta import relativedelta
import sys
import datetime


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()

        # Load the UI file
        uic.loadUi("Years_GUI.ui", self)

        # define Widgets
        self.btnExit = self.findChild(QPushButton, "btnExit")
        self.btnCalc = self.findChild(QPushButton, "btnCalc")

        self.dtStart = self.findChild(QDateEdit, "dtStart")
        self.dtEnd = self.findChild(QDateEdit, "dtEnd")

        self.label = self.findChild(QLabel, "label")       

        self.actExit = self.findChild(QAction, "actExit")

        # Define the actions
        self.btnExit.clicked.connect(self.closeEvent)
        #self.btnCalc.clicked.connect(self.calc_years)
        self.btnCalc.clicked.connect(self.get_age)

        self.actExit.triggered.connect(self.closeEvent)

        # Set date boxes to current date
        self.dtStart.setDate(date.today())
        self.dtEnd.setDate(date.today())

        # Show the app
        self.show()

    def calc_years(self):
        print("Calculating years")
        sDate = self.dtStart.date().toString()  # Get date from box as a string
        tsDate = sDate.split(" ")  # Parse the date from the list
        sYear = int(tsDate[3])  # Get year from list and assign as a variable
        print(sYear)  # Print the Variable (year)

        eDate = self.dtEnd.date().toString()
        teDate = eDate.split(" ")
        eYear = int(teDate[3])
        print(eYear)
        age = eYear - sYear
        print(age)

        print(f"Starting Date {sDate}")
        print(f"Ending Date {eDate}")

        # print(diff)
        # print(diff/365)

    def get_age(self):
        sDate = self.dtStart.date()
        sYear = sDate.year()
        sMonth = sDate.month()
        print(sYear)
        print(sMonth)

        eDate = self.dtEnd.date()
        eYear = eDate.year()
        eMonth = eDate.month()
        print(eYear)
        print(eMonth)
        finalAge = eYear - sYear
        if sMonth > eMonth:
            finalAge = finalAge - 1
        print(finalAge)
        self.label.setText(f"The final age is {finalAge}")

    
    def closeEvent(self, *args, **kwargs):
        # print("Program closed Successfully!")
        self.close()


# Initialize the App
app = QApplication(sys.argv)
UIWindow = UI()
app.exec_()
