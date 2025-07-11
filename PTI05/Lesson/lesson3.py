import json
import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import QApplication

class Bao:
    def __init__(self, _name, _nameartist, _view, _rating, _duration, _image, _link):
        self.name = _name
        self.artist = _nameartist
        self.view = _view
        self.rating = _rating
        self.duration = _duration
        self.image = _image
        self.link = _link

    def Show(self):
        print(self.__dict__)

    def openLinkSpotify(self):
        self.browser = QWebEngineView()
        self.browser.setGeometry(100, 100, 1280, 900)
        self.browser.setUrl(QUrl(self.link))
        self.browser.setWindowTitle(f"Đang mở: {self.name}")
        self.browser.show()

class ListBao:
    def __init__(self):
        self._list = []
        self.filepath = "Data/Songs.json"
        self.loadAll()

    # Thêm
    def add(self, newSong):
        self._list.append(newSong)
        self.saveAll()

    # Đọc
    def loadAll(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as filedata:
                data = json.load(filedata)
                self._list.clear()
                for item in data:
                    song = Bao(item["name"], item["artist"], item["view"],
                               item["rating"], item["duration"], item["image"], item["link"])
                    self._list.append(song)
        except FileNotFoundError:
            print("⚠️ File chưa tồn tại. Sẽ tạo mới khi lưu.")
        except Exception as e:
            print("❌ Lỗi đọc file:", e)

    # Ghi
    def saveAll(self):
        try:
            with open(self.filepath, "w", encoding="utf-8") as filedata:
                dataSave = []
                for song in self._list:
                    dataSave.append({
                        "name": song.name,
                        "artist": song.artist,
                        "view": song.view,
                        "rating": song.rating,
                        "duration": song.duration,
                        "image": song.image,
                        "link": song.link
                    })
                json.dump(dataSave, filedata, indent=4, ensure_ascii=False)
        except Exception as e:
            print("❌ Lỗi ghi file:", e)

    # Tìm theo tên
    def findByName(self, name):
        for song in self._list:
            if song.name.lower() == name.lower():
                return song
        return None

    # Sửa (update)
    def update(self, name, newInfo: Bao):
        for i, song in enumerate(self._list):
            if song.name.lower() == name.lower():
                self._list[i] = newInfo
                self.saveAll()
                print(f"✅ Đã cập nhật: {name}")
                return
        print(f"❌ Không tìm thấy bài hát để cập nhật: {name}")

    # Xoá
    def delete(self, name):
        before = len(self._list)
        self._list = [song for song in self._list if song.name.lower() not in name.lower()]
        after = len(self._list)
        self.saveAll()
        if before != after:
            print(f"🗑️ Đã xoá: {name}")
        else:
            print(f"❌ Không tìm thấy để xoá: {name}")

    # Mở bài hát
    def openSongByName(self, inputName):
        song = self.findByName(inputName)
        if song:
            song.openLinkSpotify()
        else:
            print("❌ Không tìm thấy bài hát")

    # Hiển thị danh sách
    def showAll(self):
        print("🎵 Danh sách bài hát:")
        for song in self._list:
            song.Show()
            print("-----")


























































# # Song: tên bài hát, tên nghệ sĩ, lượt xem, đánh giá, thời lượng,
# # hình ảnh, đường link

# import json, sys
# from PyQt6.QtCore import QUrl
# from PyQt6.QtWebEngineWidgets import QWebEngineView
# from PyQt6.QtWidgets import QApplication

# class Bao:
#     def __init__(self, _name, _nameartist, _view, _rating, _duration, _image, _link):
#         self.name = _name
#         self.artist = _nameartist
#         self.view = _view
#         self.rating = _rating
#         self.duration = _duration
#         self.image = _image
#         self.link = _link

#     def Show(self):
#         print(self.__dict__)

#     def openLinkSpotify(self):
#         main = QApplication(sys.argv)
#         app = QWebEngineView()
#         app.setGeometry(0, 0, 1280, 900)
#         app.setUrl(QUrl(self.link))
#         app.show()
#         main.exec()

# # s1 = Song("Song Gio", "797", 1000000, 10, "3:50", "none", "https://open.spotify.com/track/1O8bQhEDEd0O0gQyYtirRFN")
# # s1.Show()
# # s1.openLinkSpotify()

# class ListBao:
#     def __init__(self):
#         self._list = []
#         self.loadAll()

#     # CRUD
#     # Thêm
#     def add(self, newSong):
#         self._list.append(newSong)
#         self.saveAll()

#     # Đọc
#     def loadAll(self, filepath="Data/Songs.json"):
#         try:
#             with open(filepath, "r") as filedata:
#                 data = json.load(filedata)
#                 print(data)
#         except:
#             print("Check file Songs.json")

#     # Ghi
#     def saveAll(self, filepath="Data/Songs.json"):
#         # try:
#             with open(filepath, "w") as filedata:
#                 dataSave = []
#                 for song in self._list:
#                     print(song)
#                     dataSave.append({
#                         "name": song.name,
#                         "nameartist": song.artist,
#                         "view": song.view,
#                         "rating": song.rating,
#                         "duration": song.duration,
#                         "image": song.image,
#                         "link": song.link
#                     })
#                 # json.dump(filedata, dataSave, indent=7)
#                 print(dataSave)
#         # except:
#         #     print("Check file ")

#     # Mở
#     def openSongByName(self, inputName):
#         for song in self._list:
#             if song.name == inputName:
#                 song.openLinkSpotify()

#     # Xoá
#     def delete(self, inputName):
#         for song in self._list:
#             if song.name == inputName:
#                 self._list.remove(song)

#     # Hiển thị
#     def showAll(self):
#         print("Danh sách bài hát")
#         for song in self._list:
#             song.show()
#             print("-----")
