# -*- coding: utf-8 -*-

import sys
import time

from PyQt5 import QtGui
from PyQt5 import QtCore
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
    QHeaderView,
    QWidget,
    QVBoxLayout,
    QLabel,
    QAction, QMessageBox,
)

from typing import Any


from iamd import *
import sqlite3
import os.path

# https://git.videolan.org/?p=vlc/bindings/python.git;a=tree;f=examples;hb=HEAD
import vlc
# https://wiki.python.org/moin/PyQt/Playing%20a%20sound%20with%20QtMultimedia

from main_wnd import Ui_MainWindow
from form_add import Ui_Form

url = "http://nashe1.hostingradio.ru/nashe-256"


file_db_path = "resource/playlist.sqlite"
file_db_blank = "resource/db_blank.sql"


class AboutWindow(QWidget):
    """
    TODO: Написать о программе
    ВИджет About
    """

    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setWindowTitle("О программе")
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText(
            """Инфа о плеере
            потом надо написать
            много строчек и зачем это нужно
            и то что аналогов нет"""
        )
        self.layout().addWidget(self.info)


class AddWidget(QMainWindow, Ui_Form):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.con = sqlite3.connect("films.db")
        # self.params = {}
        # self.setupUi(self)
        # self.selectGenres()
        # self.pushButton.clicked.connect(self.add_elem)

    def selectGenres(self):
        pass
        # req = "SELECT * from genres"
        # cur = self.con.cursor()
        # for value, key in cur.execute(req).fetchall():
        #     self.params[key] = value
        # self.comboBox.addItems(list(self.params.keys()))

    def add_elem(self):
        pass
        # cur = self.con.cursor()
        # id_off = cur.execute("SELECT max(id) FROM films").fetchone()[0]
        # new_data = (id_off + 1, self.title.toPlainText(), int(self.year.toPlainText()),
        #             self.params.get(self.comboBox.currentText()), int(self.duration.toPlainText()))
        # cur.execute("INSERT INTO films VALUES (?,?,?,?,?)", new_data)
        # self.con.commit()
        # self.close()


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Конструктор класса
        """
        super().__init__()
        self.setupUi(self)
        self.playlist = []
        self.track_number = 0

        # режим воспроизведения, по умолчанию локально
        self.local = True

        # о программе
        self.about_action = QAction(self)
        self.about_action.setText("О программе")
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)
        self.about_window = AboutWindow()

        # !!!!диалог добавления записей
        self.add_dialog = AddWidget()
        self.OpenButton.clicked.connect(self.adding)

        # коннект к БД и запуск проверки целостности БД
        self.connection = sqlite3.connect(file_db_path)
        self.check_db()

        # чтение плейлиста
        self.read_playlist()
        self.fill_playlist()
        self.set_track_name()

        # Define VLC player
        self.instance = vlc.Instance("--input-repeat=-1", "--fullscreen")
        self.player = self.instance.media_player_new()

        # print(self.player.get_time()) # время
        # print(self.player.audio_get_track_description()) # список tuple есть ли там инфа хоть у одной станции о стриме?

        # Play/Stop/Next/Prev/Local
        self.PlayButton.clicked.connect(self.play)
        self.StopButton.clicked.connect(self.stop)
        self.NextButton.clicked.connect(self.next_url)
        self.PrevButton.clicked.connect(self.prev_url)
        self.RadioBtnGroup.buttonToggled.connect(self.radio_on_clicked)

        # Регулировка громкости, работает только для локального воспроизведения
        # На I.AM.D в силу схемотехники включения интерфейса WIFI к усилителю по цифровой шине
        # громкость регулировать невозможно, так как в DSP не заходит сигнал громкости
        # модуль регулирует громкость, но на громкости воспроизведения это не отражается
        # Возможно через ssh можно попытаться регулировать громксть, но это очень медленно и не надежно
        # управление громкости с панели усилителя или с пульта работает.
        self.VolumeSlider.setValue(self.player.audio_get_volume())
        self.VolumeSlider.setProperty("value", 50)
        self.set_volume(50)
        self.VolumeSlider.setToolTip("Volume")
        self.VolumeSlider.valueChanged.connect(self.set_volume)

        # управление плейлистом, на одиночное и на двойное нажатие
        self.PlayList.itemClicked.connect(self.playlist_clicked)
        self.PlayList.itemDoubleClicked.connect(self.playlist_double_clicked)

        # таймер раз в секунду,запускается при нажатии Play и останавливается по Stop
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time_label)

    @QtCore.pyqtSlot()
    def update_time_label(self) -> None:
        """
        Обновляет время проигрывания радио. Данные берутся с плеера.
        :return: None
        """
        self.TimeLabel.display(time.strftime('%H:%M:%S', time.gmtime(self.player.get_time() // 1000)))

    def playlist_clicked(self, item: Any) -> None:
        """
        На одиночное нажатие выбирает элемент из плейлиста
        :param item: Any
        :return: None
        """
        self.track_number = int(item.text().split(":")[0])
        self.ImageLabel.setPixmap(self.playlist[self.track_number].get("image"))
        # QMessageBox.information(self, "Info", item.text())

    def playlist_double_clicked(self, item: Any):
        print(type(item))
        """
        На двойной клик выбирает элемент из плейлиста и включает play
        :param item: Any
        :return: None
        """
        self.track_number = int(item.text().split(":")[0])
        self.ImageLabel.setPixmap(self.playlist[self.track_number].get("image"))
        self.play()

    def about(self) -> None:
        """
        Вызывает окно about
        :return: none
        """
        self.about_window.show()

    def adding(self) -> None:
        """
        Открывает диалог добавления записей в плейлисты
        :return: None
        """
        self.add_dialog.show()

    def set_volume(self, volume: int) -> None:
        """
        Регулирует громкость
        :param volume: int
        :return: None
        """
        self.player.audio_set_volume(volume)

    def play(self) -> None:
        """
        Обработчик кнопки play
        :return: None
        """
        self.set_track_name()
        if self.local:
            # Define VLC media
            media = self.instance.media_new(self.playlist[self.track_number]["url"])
            # Set player media
            self.player.set_media(media)
            # Play the media
            self.player.play()
            self.timer.start()
        else:
            pass

    def stop(self) -> None:
        """
        Обработчик кнопки stop
        :return: None
        """
        self.set_track_name("Stoped")
        if self.local:
            self.player.stop()
            self.timer.stop()
        else:
            pass

    def next_url(self) -> None:
        """
        Следующее радио
        :return: None
        """
        if self.track_number < len(self.playlist) - 1:
            self.track_number += 1
            self.change_row_playlist(self.track_number)
            if self.player.is_playing():
                self.play()

    def prev_url(self) -> None:
        """
        Предыдущее радио
        :return: None
        """
        if self.track_number > 0:
            self.track_number -= 1
            self.change_row_playlist(self.track_number)
            if self.player.is_playing():
                self.play()

    def radio_on_clicked(self) -> None:
        """
        Обработчик режима воспроизведения
        :return: None
        """
        if self.RadioBtnGroup.checkedButton().objectName() == "LocalButton":
            self.local = True
            self.play()
        else:
            self.stop()
            self.local = False

    def check_db(self) -> None:
        """
        Проверяет что База работает. Если не работает или битая, удаляет файл и создает снова чистую базу
        Пример пустой базы в виде SQL команд в file_db_blank
        :return: None
        """
        query = """SELECT * FROM playlist, image WHERE playlist.id = image.id"""
        try:
            self.connection.cursor().execute(query).fetchall()
        except:
            if os.path.exists(file_db_path):
                os.remove(file_db_path)
                sqlite3.connect(file_db_path)
                self.connection = sqlite3.connect(file_db_path)
            cursor = self.connection.cursor()
            with open(file_db_blank) as file:
                res = " ".join(file.readlines()).split(";")
                print(res)
            _ = [cursor.execute(query.strip()) for query in res if res]
            self.connection.commit()

    def set_track_name(self, name=""):
        if name:
            self.TrackName.setText(name)
        else:
            self.TrackName.setText(
                f"{self.playlist[self.track_number]['name']} - "
                f"{self.playlist[self.track_number]['url']} - "
                f"{self.playlist[self.track_number]['bitrate']}kbps")

    def read_playlist(self) -> None:
        """
        Читает плейлист из базы в память в виде списка словарей
        :return: None
        """
        query = """SELECT playlist.id, playlist.name, playlist.url, playlist.status, playlist.bitrate, image.image
         FROM playlist, image WHERE playlist.id = image.id ORDER BY playlist.name ASC"""
        res = self.connection.cursor().execute(query).fetchall()
        for n, name, url, status, bitrate, image in res:
            qimg = QtGui.QImage.fromData(image)
            pixmap = QtGui.QPixmap.fromImage(qimg)
            self.playlist.append({"name": name,
                                  "url": url,
                                  "bitrate": bitrate,
                                  "status": status,
                                  "image": pixmap})

    def fill_playlist(self) -> None:
        """
        Заполняет первоначально плейлист
        :return: None
        """
        for n, i in enumerate(self.playlist):
            self.PlayList.addItem(f"{n}: {i['name']} - {i['bitrate']}kbps")
        self.change_row_playlist(self.track_number)

    def change_row_playlist(self, track_number: int = 0) -> None:
        """
        Меняет ячейку в плейлисте
        :param track_number: int
        :return: None
        """
        self.ImageLabel.setPixmap(self.playlist[track_number].get("image"))
        self.PlayList.setCurrentRow(track_number)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
