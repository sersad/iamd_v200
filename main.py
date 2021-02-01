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
from imad import *
import sqlite3
import os.path

file_db_path = "playlist.sqlite"


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

        self.connection = sqlite3.connect(file_db_path)
        self.check_db()

    def about(self) -> None:
        """
        Вызывает окно about
        :return: none
        """
        self.about_window.show()

    def check_db(self) -> None:
        """
        Провереят что База работает. Если не работает то или битая, удаляет файл и создает снова чистую базу
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
            cursor.execute(
                """CREATE TABLE playlist (
                id      INTEGER PRIMARY KEY AUTOINCREMENT
                                UNIQUE,
                name    VARCHAR UNIQUE ON CONFLICT ROLLBACK,
                url     VARCHAR NOT NULL,
                status  INTEGER    DEFAULT (0),
                bitrate INTEGER);"""
            )

            cursor.execute(
                """CREATE TABLE image (
                id    INTEGER  REFERENCES playlist (id) ON DELETE CASCADE
                                                    ON UPDATE CASCADE,
                image BLOB );"""
            )

            cursor.execute(
                """INSERT INTO playlist (bitrate, status, url, name, id)
                 VALUES (256, 1, 'http://nashe1.hostingradio.ru/nashe-256', 'Наше Радио', 1 ),
                 (256, 1, 'http://retro256.streamr.ru', 'Ретро FM', 2 );"""
            )
            self.connection.commit()

    def select_playlist(self):
        query = """SELECT * FROM playlist, image WHERE playlist.id = image.id"""
        res = self.connection.cursor().execute(query).fetchall()
        # Заполним размеры таблицы
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        # Заполняем таблицу элементами
        for i, row in enumerate(res):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = MyWindow()
    ex.show()
    sys.exit(app.exec())
