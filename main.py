# -*- coding: utf-8 -*-

import sys
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
from main_wnd import Ui_MainWindow
from iamd import *
import sqlite3
import os.path

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


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        """
        Конструктор класса
        """
        super().__init__()
        self.setupUi(self)

        # о программе
        self.about_action = QAction(self)
        self.about_action.setText("О программе")
        self.about_action.triggered.connect(self.about)
        self.menuBar().addAction(self.about_action)
        self.about_window = AboutWindow()

        # коннект к БД и запуск проверки целостности БД
        self.connection = sqlite3.connect(file_db_path)
        self.check_db()

        self.read_playlist()

    def about(self) -> None:
        """
        Вызывает окно about
        :return: none
        """
        self.about_window.show()

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

    def read_playlist(self):
        query = """SELECT playlist.id, playlist.name, playlist.url, playlist.status, playlist.bitrate, image.image
         FROM playlist, image WHERE playlist.id = image.id"""
        res = self.connection.cursor().execute(query).fetchall()
        for n, name, url, status, bitrate, image in res:
            self.PlayList.addItem(f"{name} - {bitrate} kbps - {url}")
        # self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(0)
        # # Заполняем таблицу элементами
        # for i, row in enumerate(res):
        #     self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
        #     for j, elem in enumerate(row):
        #         self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
