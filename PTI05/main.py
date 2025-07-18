from PyQt6.QtWidgets import QMainWindow, QWidget, QApplication , QInputDialog , QMessageBox, QFileDialog
from PyQt6 import uic, QtGui
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys
import json
from PyQt6.QtWidgets import * # them tat ca thu ben trong thu vien
from PyQt6 import uic
from PyQt6.QtGui import QKeyEvent
from PyQt6.QtCore import Qt
import sys, json
import os
import subprocess

class LoginPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui_GiaoDien/login.ui",self)
        self.Resgister.clicked.connect(self.showSignUp)
        self.Login.clicked.connect(self.checkLogin)
    def checkLogin(self):
        txtUser = self.username.text()
        txtPass=self.password.text()
        if txtUser == "admin" and txtPass == "admin":
            admin.show()
            self.close()
        elif txtUser =="123" and txtPass == "123":
            h.show()
            self.close()
        else:
            print("Sai tên tài khoản hoặc mật khẩu") 
    def showSignUp(self):
        self.close()
        su.show()

class SignUpPage(QMainWindow):
        def __init__(self):
             super().__init__()
             uic.loadUi("Ui_GiaoDien/signup.ui",self)
             self.login.clicked.connect(self.showLogin)
        def showLogin(self):
             lg.show()
             self.close()



class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui_GiaoDien/Home.ui", self)
        # self.btnSearch.clicked.connect(lambda: self.stackedWidget.setCurrentIndex)
        # self.btnHome.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(3))
        # self.btnIntro.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(0))
        # self.btnProfile.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(1))
        # self.btnSetting.clicked.connect(lambda: self.stackedWidget.setCurrentIndex(2))
        self.btnSearch.clicked.connect(self.findSongByName)
        
        self.loadData()
    def findSongByName(self):
        search_text = self.lineEditSearch.text().lower()
        content_widget = QWidget()
        layout = QVBoxLayout(content_widget)
        with open("Data/Songs.json", "r") as FILEDATA:
            ListSong = json.load(FILEDATA)
            for song in ListSong:
                if search_text in song["name"].lower():
                    frame = SongFrame(song)
                    frame.ui.imageSong.setPixmap(QtGui.QPixmap(song["image"]))
                    frame.ui.nameSong.setText(song["name"])
                    frame.ui.duarationSong.setText("Nguồn: " + song["duration"])
                    frame.ui.nameArtist.setText("Tác giả: " + song["artist"])
                    frame.ui.viewSong.setText("Ngày viết: " + song["view"])
                    layout.addWidget(frame)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setWidget(content_widget)
        

    
    def loadData(self):
         content_widget = QWidget()
         layout = QVBoxLayout(content_widget)
         with open("Data/Songs.json","r") as FILEDATA :
            ListSong = json.load(FILEDATA)
            for song in ListSong :
                # print(song)
                frame = SongFrame(song)
                frame.ui.imageSong.setPixmap(QtGui.QPixmap(song["image"]))
                frame.ui.nameSong.setText(song["name"])
                frame.ui.duarationSong.setText("Nguồn: "+song["duration"])
                frame.ui.nameArtist.setText("Tác giả: "+song["artist"])
                frame.ui.viewSong.setText("Ngày viết: "+song["view"])
        
                layout.addWidget(frame)
            self.scrollArea.setWidgetResizable(True)
            self.scrollArea.setWidget(content_widget)


from PyQt6 import QtCore
from Ui_GiaoDien.SongFrame import Ui_Frame
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView


class SongFrame(QFrame):
     def __init__(self,inforSong,parent=None):
          super().__init__(parent)
          self.ui = Ui_Frame()
          self.ui.setupUi(self)
          self.ui.bao1.clicked.connect(lambda: self.show_bao(inforSong))
          
         

     def show_bao(self,infor) :
        self.a = QWebEngineView()
        self.a.setGeometry(0, 0, 1280, 900)
        self.a.setUrl(QUrl(infor["link"]))
        self.a.show()
        


from Lesson.lesson2 import Account, ListAccount
from Lesson.lesson3 import Bao, ListBao

class AdminPage(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("Ui_GiaoDien/Admin.Ui",self)
        self.btnAddAccount.clicked.connect(self.addAccount)
        self.btnDeleteAccount.clicked.connect(self.deleteAccount)
        self.btnEditAccount.clicked.connect(self.editAccount)
        self.counterAccount = 0
        self.btnAddSong.clicked.connect(self.addSong)
        self.btnEditSong.clicked.connect(self.editSong)
        self.btnDeleteSong.clicked.connect(self.deleteSong)
        self.counterSong = 0
        self.loadData()
        self.LB = ListBao()
    def loadData(self):
        self.listAccount.clear()
        self.listSong.clear()
        self.counterAccount = 0
        self.counterSong = 0

    # Đọc danh sách account
    try:
        with open("Data/Account.json", "r", encoding="utf-8") as file:
            dataLoad = json.load(file)
            for account in dataLoad:
                self.counterAccount += 1
                self.listAccount.addItem(f"Account {self.counterAccount}   -  {account['username']} -  {account['password']} -  {account['gmail']}")
    except Exception as e:
        print("Không tìm thấy hoặc lỗi file Account.json:", e)

    # Đọc danh sách bài báo
    try:
        with open("Data/Songs.json", "r", encoding="utf-8") as file:
            dataLoad = json.load(file)
            for song in dataLoad:
                self.counterSong += 1
                self.listSong.addItem("Song " + str(self.counterSong) + " :: " + song['name'] + " :: " + song['artist'] + " :: " + song['view'] + " :: " + song['rating'] + " :: " + song['duration'] + " :: " + song['image'] + " :: " + song['link'])
    except Exception as e:
        print("Không tìm thấy hoặc lỗi file Songs.json:", e)

                     
        
        # except :
        #     print("Check file Account and Song")


    def addAccount(self):
        username, ok = QInputDialog.getText(self,"Input","Enter username:")
        password, ok = QInputDialog.getText(self,"Input","Enter password:")
        email, ok = QInputDialog.getText(self,"Input","Enter email:")
        self.counterAccount += 1
        self.listAccount.addItem("Account" + str(self.counterAccount) + " - " + username + ' - ' + password + "-" + email)

    def editAccount(self):
        selected_item = self.listAccount.currentItem()
        if selected_item:
            ac, us , pw ,em = selected_item.text().split("-")
            username, ok = QInputDialog.getText(self,"Input","Enter username:",text = str(us))
            password, ok = QInputDialog.getText(self,"Input","Enter password:",text = str(pw))
            email, ok = QInputDialog.getText(self,"Input","Enter email:", text = str(em))
            selected_item.setText("Account" + str(self.counterAccount) + " - " + username + ' - ' + password + "-" + email)
    def deleteAccount(self):
        selected_item =  self.listAccount.currentItem()
        if selected_item:
             row = self.listAccount.row(selected_item)
             self.listAccount.takeItem(row)
    def addSong(self):
        name, ok = QInputDialog.getText(self,"Input","Tên bài báo")
        nameartist, ok = QInputDialog.getText(self,"Input","Tác giả")
        view, ok = QInputDialog.getText(self,"Input","Ngày viết")
        rating, ok = QInputDialog.getText(self,"Input","Đánh giá")
        duration, ok = QInputDialog.getText(self,"Input", "Nguồn")
        image, _ = QFileDialog.getOpenFileName(self, "Select Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        link, ok = QInputDialog.getText(self,"Input","Enter Link Song")
        self.counterSong += 1
        self.listSong.addItem("Song " + str(self.counterSong) + " :: " + name + " :: " + nameartist + " :: " + view + " :: " + rating + "::" + duration + "::" + image + " :: " + link)
        self.LB.add(Bao(name,nameartist,view, rating, duration, image, link))

    def deleteSong(self):
        selected_item = self.listSong.currentItem()
        if selected_item:
            row = self.listSong.row(selected_item)
            # Lấy thông tin từ chính selected_item
            song_id = selected_item.text().split("::")[1].strip()
            self.listSong.takeItem(row)
            self.LB.delete(song_id)
    def editSong(self):
        selected_item = self.listSong.currentItem()
        if selected_item:
            ct, n, ns, v, rt, dr, img, l = selected_item.text().split("::")
            name, ok = QInputDialog.getText(self,"Edit", "Tên bài báo", text=n)
            nameartist, ok = QInputDialog.getText(self,"Edit","Tác giả", text = ns)
            view, ok = QInputDialog.getText(self,"Edit", "Ngày viết", text=v)
            rating, ok = QInputDialog.getText(self,"Edit", "Đánh giá", text=rt)
            duration, ok = QInputDialog.getText(self,"Edit", "Nguồn", text=dr)
            image, _ = QFileDialog.getOpenFileName(self,"Edit", "Select New Image", "","Image Files(*.png *.jpg *.jpeg *.bmp)")
            link, ok = QInputDialog.getText(self,"Edit", "Edit link song", text=l)
            selected_item.setText("Song " + str(self.counterSong) + " :: " + name + " :: " + nameartist + " :: " + view + " :: " + rating + "::" + duration + "::" + image + " :: " + link)
            self.LB.update(n.strip(), Bao(name,nameartist,view, rating, duration, image, link))
    
    def keyPressEvent(self, event: QKeyEvent):
        if event.key() == Qt.Key.Key_Right:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() + 1)
        elif event.key() == Qt.Key.Key_Left:
            self.stackedWidget.setCurrentIndex(self.stackedWidget.currentIndex() - 1)
        super().keyPressEvent(event)

            
if __name__ == "__main__":
    subprocess.run(["python", "-m", "PyQt6.uic.pyuic", "-o", "Ui_GiaoDien/SongFrame.py", "Ui_GiaoDien/Song_Frame.ui"], check=True)
    app = QApplication(sys.argv)
    lg = LoginPage()
    su = SignUpPage()
    h = HomePage()
    admin = AdminPage()
    lg.show()
    sys.exit(app.exec())
    

