# -*- coding: utf-8 -*-

import sys

from PyQt5 import QtGui
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
    QHeaderView,
    QWidget,
    QVBoxLayout,
    QLabel,
    QAction,
)

from PIL import Image

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

        # режим воспроизведения, по умолчанию локально
        self.local = True

        self.track_number = 0

        # !!!!!url по умолчнию, заменить на первый в плейлисте
        self.url = url



        # о программе
        self.about_action = QAction(self)
        self.about_action.setText("О программе")
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)
        self.about_window = AboutWindow()

        # диалог добавления записей
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

        # непонятно
        # start with a callback
        # em = self.player.event_manager()
        # def call_vlc(self, player):
        #     player.get_time()
        #
        # em.event_attach(vlc.EventType.MediaPlayerTimeChanged, call_vlc, self.player)

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
        self.set_track_name(self.url)
        if self.local:
            # Define VLC media
            media = self.instance.media_new(self.url)
            # Set player media
            self.player.set_media(media)
            # Play the media
            self.player.play()
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
        else:
            pass

    def next_url(self) -> None:
        """
        Следующее радио
        :return: None
        """
        if self.local:
            pass
        else:
            pass

    def prev_url(self) -> None:
        """
        Предыдущее радио
        :return: None
        """
        if self.local:
            pass
        else:
            pass

    def radio_on_clicked(self) -> None:
        """
        обработчик режима воспроизведения
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
        self.TrackName.setText(
            f"{self.playlist[self.track_number]['name']} - "
            f"{self.playlist[self.track_number]['url']} - "
            f"{self.playlist[self.track_number]['bitrate']}kbps")

    def read_playlist(self) -> None:
        """
        Читает плейлист из базы в память ввиде списка словарей
        :return: None
        """
        self.playlist = []
        query = """SELECT "playlist".id, playlist.name, playlist.url, playlist.status, playlist.bitrate, image.image
         FROM playlist, image WHERE playlist.id = image.id"""
        res = self.connection.cursor().execute(query).fetchall()
        for n, name, url, status, bitrate, image in res:
            qimg = QtGui.QImage.fromData(image)
            pixmap = QtGui.QPixmap.fromImage(qimg)
            self.playlist.append({"name": name,
                                  "n": n,
                                  "url": url,
                                  "bitrate": bitrate,
                                  "status": status,
                                  "image": pixmap})

            # qimg = QtGui.QImage.fromData(image)
            # pixmap = QtGui.QPixmap.fromImage(qimg)
            # self.ImageLabel.setPixmap(pixmap)

    def fill_playlist(self, track_number: int = 0) -> None:
        """
        Заполняет первоначально плейлист
        :param track_number: int
        :return:
        """
        for i in self.playlist:
            self.PlayList.addItem(f"{i['n']}: {i['name']} - {i['bitrate']}kbps")
        self.ImageLabel.setPixmap(self.playlist[track_number].get("image"))
        self.PlayList.setCurrentRow(track_number)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
