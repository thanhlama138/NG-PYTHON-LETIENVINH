# class Student():
#     def __init__(self, name = "Chua biet", age = 0, gender ="Chua biet", school="School"):
#         self.name = name
#         self.age = age
#         self.gender = gender
#         self.school = school
#     def show(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Gender:",self.gender)
#         print("school:", self.school)

# hs1 = Student("Long",13 ,"Nam","Mindx School")
# hs2 = Student("Hai", 14 ,"Nu","Mindx school")
# hs1.show()
# hs2.show()
import json
# lop cua 1  tai khoan
class Account():
    def __init__(self, _username,_password,_gmail):
        self.username = _username
        self.password = _password
        self.gmail = _gmail
    def show(self):
        print("Username", self.username, "Passoword:", self.password, "Email:",self.gmail)
    def changePassword(self, newPassword):
        self.password = newPassword
        print("Account:",self.username,"Change Password:", self.password)
    def resetPassword(self,gamil):
        if(gamil == self.gmail):
            print("Reset password success!")
            self.password = "1"
        else:
            print("Reset password fail!")
#lop cua nhieu tai khoan
class ListAccount():
    def __init__(self):
        self.listAcc = []
        self.loadAllAccounts()
    def addAccount(self, newAcc):
        self.listAcc.append(newAcc)
    def loadAllAccounts(self, filepath="Data/Account.json"):
        try:
            with open(filepath,"r") as filedata:
                data = json.load(filedata)
                print(data)
                for acc in data :
                    self.addAccount(Account(acc["username"],acc["password"],acc["gmail"]))


        except:
            print("kiem tra lai file accounts")
    
    
    def saveAllAccounts(self,filepath="Data/Account.json"):
        try:
            with open(filepath,"w") as filedata:
                dataSave = []
                for acc in self.listAcc:
                    dataSave.append({"username":acc.username,"password":acc.password,"gmail":acc.gmail})
                json.dump(dataSave, filedata, indent=3)
                print("luu du lieu thanh cong!")
        except:
            print("Luu du lieu that bai!kiem tra lai file accounts")

    def deleteAccount(self,inputUsername):
        for acc in self.listAcc:
            if acc.username == inputUsername:
                self.listAcc.remove(acc)
                print("xoa tai khoan thanh cong!")
    def updateAccount(self, inputUsername, inputNewPassword, inputNewGmail):
        for acc in self.listAcc:
            if acc.username == inputUsername:
                acc.password == inputNewPassword
                acc.gmail == inputNewGmail
                print("cap nhat tai khoan", acc.username,"thanh cong")
    def showAllAccount(self):
        print("Danh sach tai khoan dang co")
        for acc in self.listAcc:
            acc.show()
        print("-------------------------")

# listAcc = ListAccount() 
# listAcc.loadAllAccounts()
# listAcc.addAccount(Account("long1","123","minhlong08092012@gmail.com"))
# listAcc.addAccount(Account("long2","123","minhlong08092012@gmail.com"))
# listAcc.addAccount(Account("long3","123","minhlong08092012@gmail.com"))
# listAcc.addAccount(Account("long4","123","minhlong08092012@gmail.com"))
# listAcc.addAccount(Account("long5","123","minhlong08092012@gmail.com"))
# listAcc.deleteAccount("long3")
# listAcc.showAllAccount()

# listAcc.updateAccount ("long1","2206","minhlong22062012@gmail.com")
# listAcc.saveAllAccounts()
        
