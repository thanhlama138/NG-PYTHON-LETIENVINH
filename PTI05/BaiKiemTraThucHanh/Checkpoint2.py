from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication , QInputDialog, QFileDialog
from PyQt6 import uic
from PyQt6.QtCore import Qt
import sys
import json

class Homework:
    def __init__(self, name, priority, completed=False):
        self.name = name
        self.priority = priority
        self.completed = completed


class HomeworkList:
    def __init__(self):
        super().__init__()
        uic.loadUi("Dialog.ui",self)
        self.btexport.clicked.connect(self.showdialog)
    
    
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def all_completed(self):
        completed = True
        for item in self.items:
            if item.completed == False:
                completed = False
                print(item.name)
            elif completed == True :
                print("All finished!")

    def showdialog(self):
        with open("Dialog.json","w") as hwlist:
            HwSave = []
            for item in self.items:
                HwSave.append({"Ten bai tap":item.name,"Muc do":item.priority,"hoan thanh":item.completed})
                json.dump(HwSave, hwlist, indent=3)
                print("luu du lieu thanh cong!")

    
   

        

    



hw_list = HomeworkList()
hw_list.add_item(Homework("Lap trình App Producer", 3,False))
hw_list.add_item(Homework("Lam văn", 2, True))
hw_list.add_item(Homework("Lap trình GameMaker", 3,False))


hw_list.all_completed()

hw_list.showdialog()

if __name__ == "__main__":


    sys.exit()
    