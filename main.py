#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys



import time
import vlc
from PyQt5 import QtCore
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QCloseEvent
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QTableWidgetItem,
    QWidget,
    QVBoxLayout,
    QLabel,
    QAction, QMessageBox, QFileDialog,
)
import platform
if platform.system().lower() == "windows":
    import os
    os.add_dll_directory(os.getcwd() + '\module')


from ui.form_add import Ui_Form
from module.iamd import *
from ui.main_wnd import Ui_MainWindow

from module.iamd import commands, get_config, set_player, get_player_status
from module.database import db_add_row, db_delete_row, db_show_items, db_show_table, check_db, db_update_row


logging.basicConfig(level=logging.ERROR)


class AboutWindow(QWidget):
    """
    Виджет About
    """
    def __init__(self):
        super(AboutWindow, self).__init__()
        self.setWindowTitle("О программе")
        self.setLayout(QVBoxLayout(self))
        self.info = QLabel(self)
        self.info.setText(
            """Радио для усилителя IAMD v200.
Для демонстрации возможностей, можно 
слушать радио локально, через устройство
вывода звука по умолчанию.
Плейлисты и иконки хранятся в sqlite базе
Подробности в readme.MD"""
        )
        self.layout().addWidget(self.info)


class AddWidget(QMainWindow, Ui_Form):
    # кастомный сигнал для отлавливания закрытия окна
    signalExit = pyqtSignal()

    def __init__(self, parent=None) -> None:
        super().__init__(parent)
        self.setupUi(self)
        self.modified = {}
        self.titles = None
        self.show_table()
        self.pushButtonAdd.clicked.connect(self.add_row)
        self.pushButtonDelete.clicked.connect(self.delete_row)
        self.pushButtonAddImage.clicked.connect(self.file_dialog)
        self.tableWidget.itemChanged.connect(self.item_changed)
        self.tableWidget.itemClicked.connect(self.show_items)
        self.binary_image = None

    def file_dialog(self) -> None:
        """
        Диалоговое окно для выбора иконки радиостанции
        :return:
        """
        file = QFileDialog.getOpenFileName(self, "Открыть изображение", ".")[0]
        with open(file, 'rb') as file:
            binary_data = file.read()
        self.binary_image = binary_data

    def add_row(self) -> None:
        """
        Добавляет строку плейлиста
        :return:
        """
        name = self.lineEditName.text()
        url = self.lineEditURL.text()
        bitrate = self.lineEditBitrate.text() if self.lineEditBitrate.text() else 0
        # если ошибка при вводе посвечиваем поле
        if not name:
            self.labelName.setStyleSheet("background-color: red")
            return None
        if not url:
            self.labelURL.setStyleSheet("background-color: red")
            return None

        self.labelName.setStyleSheet("background-color: None")
        self.labelURL.setStyleSheet("background-color: None")
        db_add_row(name, url, bitrate, self.binary_image)
        # послед добавление сбрасываем image
        self.binary_image = None
        self.show_table()

    def delete_row(self) -> None:
        """
        Удаление строк
        :return:
        """
        # Получаем список элементов без повторов и их id
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        ids = [self.tableWidget.item(i, 0).text() for i in rows]
        # Спрашиваем у пользователя подтверждение на удаление элементов
        valid = QMessageBox.question(
            self, '', "Действительно удалить элементы с id " + ",".join(ids),
            QMessageBox.Yes, QMessageBox.No)
        # Если пользователь ответил утвердительно, удаляем элементы.
        if valid == QMessageBox.Yes:
            db_delete_row(ids)
        # обновляем tableWidget
        self.show_table()

    def item_changed(self, item) -> None:
        """
        Отслеживаем изменения в tableWidget
        :param item:
        :return:
        """
        self.modified["id"] = self.tableWidget.item(item.row(), 0).text()
        # Если значение в ячейке было изменено,
        # то в словарь записывается пара: название поля, новое значение
        self.modified[self.titles[item.column()]] = item.text()
        self.save_results()

    def show_items(self) -> None:
        """
        Заполняет LineEdit выбранной строчкой
        :return:
        """
        row_number = self.tableWidget.selectedIndexes()[0].row()
        id_ = self.tableWidget.item(row_number, 0).text()
        result = db_show_items(id_)
        self.lineEditName.setText(result['name'])
        self.lineEditURL.setText(result['url'])
        self.lineEditBitrate.setText(str(result['bitrate']))

    def show_table(self) -> None:
        """
        Заполняет таблицу в редакторе плейлиста
        :return: None
        """
        result = db_show_table()
        self.tableWidget.setRowCount(len(result))
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setColumnWidth(0, 0)
        self.tableWidget.setColumnWidth(1, 215)
        self.tableWidget.setColumnWidth(2, 470)
        self.tableWidget.setColumnWidth(3, 30)
        self.tableWidget.setHorizontalHeaderLabels(("", "Имя", "URL", "Bps"))
        self.titles = ['id', 'name', 'url', 'bitrate']
        for i, elem in enumerate(result):
            self.tableWidget.setItem(i, 0, QTableWidgetItem(str(result[i]['id'])))
            self.tableWidget.setItem(i, 1, QTableWidgetItem(result[i]['name']))
            self.tableWidget.setItem(i, 2, QTableWidgetItem(result[i]['url']))
            self.tableWidget.setItem(i, 3, QTableWidgetItem(str(result[i]['bitrate'])))
        self.modified = {}

    def save_results(self) -> None:
        """
        Сохраняет таблицу при прямом изменении в таблице строки
        :return:
        """
        if self.modified and any(key for key in self.modified.keys() if key != "id"):
            db_update_row(self.modified)
            self.modified.clear()

    def closeEvent(self, event: QCloseEvent) -> None:
        """
        При закрытии окна посылаем сигнал в основное окно для пересчитывания плейлиста
        :param event: QCloseEvent
        :return: None
        """
        self.signalExit.emit()


class MyWindow(QMainWindow, Ui_MainWindow):

    def __init__(self) -> None:
        """
        Конструктор класса
        """
        super().__init__()
        self.setupUi(self)
        self.playlist = []
        self.track_number = 0

        # режим воспроизведения, по умолчанию локально
        self.local = True
        self.iamd_is_playing = False

        # о программе
        self.about_action = QAction(self)
        self.about_action.setText("О программе")
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)
        self.about_window = AboutWindow()

        # проверки целостности БД
        check_db()

        # диалог редактирования плейлиста
        self.add_dialog = AddWidget()
        self.OpenButton.clicked.connect(self.adding)
        self.add_dialog.signalExit.connect(self.fill_playlist)

        # чтение плейлиста
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

        # управление плейлистом, на одиночное и на двойное нажатие
        self.PlayList.itemClicked.connect(self.playlist_clicked)
        self.PlayList.itemDoubleClicked.connect(self.playlist_double_clicked)

        # таймер запускается при нажатии Play и останавливается по Stop
        self.timer = QtCore.QTimer(self)
        self.timer.setInterval(1000)
        self.timer.timeout.connect(self.update_time_label)

        # iamd commands
        self.host = get_config()
        self.iamd_status()

    @QtCore.pyqtSlot()
    def update_time_label(self) -> None:
        """
        Обновляет время проигрывания радио. Данные берутся с плеера или усилителя
        Для плеера раз в 1 сек, для усилителя раз в 10 сек
        Для усилителя так же обновляется статус бар
        :return: None
        """
        if self.local:
            self.timer.setInterval(1000)
            self.TimeLabel.display(time.strftime('%H:%M:%S', time.gmtime(self.player.get_time() // 1000)))
        else:
            self.timer.setInterval(10000)
            self.iamd_status()

    def adding(self) -> None:
        """
        Открывает диалог добавления записей в плейлисты
        диалоговое окно посылает сигнал о своем закрытии для обновления плейлиста
        :return: None
        """
        self.add_dialog.show()

    def playlist_clicked(self, item: Any) -> None:
        """
        На одиночное нажатие выбирает элемент из плейлиста
        :param item: Any
        :return: None
        """
        self.track_number = int(item.text().split(":")[0])
        self.ImageLabel.setPixmap(self.playlist[self.track_number].get("image"))

    def playlist_double_clicked(self, item: Any) -> None:
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
            set_player(self.host["url"],
                       commands["play"] + self.playlist[self.track_number]["url"])
            self.timer.start()

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
            set_player(self.host["url"], commands["stop"])
            self.iamd_is_playing = False
            self.timer.stop()

    def next_url(self) -> None:
        """
        Следующее радио
        :return: None
        """
        if self.track_number < len(self.playlist) - 1:
            self.track_number += 1
            self.change_row_playlist(self.track_number)
            if self.player.is_playing() and self.local:
                self.play()
            elif not self.local:
                self.play()

    def prev_url(self) -> None:
        """
        Предыдущее радио
        :return: None
        """
        if self.track_number > 0:
            self.track_number -= 1
            self.change_row_playlist(self.track_number)
            if self.player.is_playing() and self.local:
                self.play()
            elif not self.local:
                self.play()

    def radio_on_clicked(self) -> None:
        """
        Обработчик режима воспроизведения
        :return: None
        """
        if self.RadioBtnGroup.checkedButton().objectName() == "LocalButton":
            self.stop()
            self.local = True
            self.play()
        else:
            if self.player.is_playing():
                self.local = False
                self.play()
            else:
                self.local = False

    def set_track_name(self, name: str = "") -> None:
        """
        Показывает имя радиостанции
        :param name:
        :return:
        """
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
        self.playlist = db_show_table()

    def fill_playlist(self) -> None:
        """
        Заполняет плейлист
        :return: None
        """
        self.read_playlist()
        self.PlayList.clear()
        for n, i in enumerate(self.playlist):
            self.PlayList.addItem(f"{n}: {i['name']} - {i['bitrate']}kbps")
        self.change_row_playlist(self.track_number)

    def change_row_playlist(self, track_number: int = 0) -> None:
        """
        Меняет ячейку в плейлисте
        :param track_number: int
        :return: None
        """
        try:
            self.ImageLabel.setPixmap(self.playlist[track_number].get("image"))
            self.PlayList.setCurrentRow(track_number)
        except IndexError:
            pass

    def iamd_status(self) -> None:
        """
        Получение статуса с усилителя
        :return:
        """
        res = get_player_status(self.host["url"])
        if not res:
            self.statusbar.setStyleSheet("background-color: #FFDDDD")
            self.statusbar.showMessage(f"IAMD amplifier ip: {self.host['ip']} not available")
        else:
            if res["status"] == "play":
                self.iamd_is_playing = True
                self.local = False
                self.RadioButton.setChecked(True)
                self.timer.start()
            else:
                self.iamd_is_playing = False
            self.statusbar.setStyleSheet("background-color: None")
            self.statusbar.showMessage(f"IAMD({self.host['ip']}) {res['status']} "
                                       f"Artist:{res['artist']} Title: {res['title']}")
            self.TimeLabel.display(time.strftime('%H:%M:%S', time.gmtime(res["curpos"] // 1000)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
