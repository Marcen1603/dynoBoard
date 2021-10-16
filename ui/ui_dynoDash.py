# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dynoDash.ui'
##
## Created by: Qt User Interface Compiler version 6.2.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QMainWindow, QProgressBar,
    QPushButton, QScrollArea, QSizePolicy, QStackedWidget,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)
import ui_images_rc
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1067, 600)
        MainWindow.setStyleSheet(u"* {\n"
"	border: None;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"background-color: rgb(35, 35, 35);")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_right_frame = QFrame(self.header_frame)
        self.header_right_frame.setObjectName(u"header_right_frame")
        self.header_right_frame.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_right_frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.open_close_side_bar_btn = QPushButton(self.header_right_frame)
        self.open_close_side_bar_btn.setObjectName(u"open_close_side_bar_btn")
        font = QFont()
        font.setFamilies([u"Dosis"])
        font.setPointSize(14)
        font.setBold(True)
        self.open_close_side_bar_btn.setFont(font)
        self.open_close_side_bar_btn.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/images/ui_images/menu_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.open_close_side_bar_btn.setIcon(icon)
        self.open_close_side_bar_btn.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.open_close_side_bar_btn)


        self.horizontalLayout.addWidget(self.header_right_frame, 0, Qt.AlignLeft)

        self.header_center_frame = QFrame(self.header_frame)
        self.header_center_frame.setObjectName(u"header_center_frame")
        self.header_center_frame.setFrameShape(QFrame.StyledPanel)
        self.header_center_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_center_frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.header_center_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setPixmap(QPixmap(u":/logo/logo/analytics_white_36dp.svg"))

        self.horizontalLayout_3.addWidget(self.label_3)

        self.label_2 = QLabel(self.header_center_frame)
        self.label_2.setObjectName(u"label_2")
        font1 = QFont()
        font1.setFamilies([u"Dosis"])
        font1.setPointSize(26)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_3.addWidget(self.label_2)


        self.horizontalLayout.addWidget(self.header_center_frame, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.header_right_frame_2 = QFrame(self.header_frame)
        self.header_right_frame_2.setObjectName(u"header_right_frame_2")
        self.header_right_frame_2.setFrameShape(QFrame.StyledPanel)
        self.header_right_frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right_frame_2)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.minimize_window_button = QPushButton(self.header_right_frame_2)
        self.minimize_window_button.setObjectName(u"minimize_window_button")
        icon1 = QIcon()
        icon1.addFile(u":/images/ui_images/minimize_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.minimize_window_button.setIcon(icon1)
        self.minimize_window_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.minimize_window_button, 0, Qt.AlignTop)

        self.restore_window_button = QPushButton(self.header_right_frame_2)
        self.restore_window_button.setObjectName(u"restore_window_button")
        icon2 = QIcon()
        icon2.addFile(u":/images/ui_images/web_asset_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.restore_window_button.setIcon(icon2)
        self.restore_window_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.restore_window_button, 0, Qt.AlignTop)

        self.close_winow_button = QPushButton(self.header_right_frame_2)
        self.close_winow_button.setObjectName(u"close_winow_button")
        icon3 = QIcon()
        icon3.addFile(u":/images/ui_images/close_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.close_winow_button.setIcon(icon3)
        self.close_winow_button.setIconSize(QSize(24, 24))

        self.horizontalLayout_2.addWidget(self.close_winow_button, 0, Qt.AlignTop)


        self.horizontalLayout.addWidget(self.header_right_frame_2, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.main_body_frame = QFrame(self.centralwidget)
        self.main_body_frame.setObjectName(u"main_body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_body_frame.sizePolicy().hasHeightForWidth())
        self.main_body_frame.setSizePolicy(sizePolicy)
        self.main_body_frame.setFrameShape(QFrame.NoFrame)
        self.main_body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.main_body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.left_menu_cont_frame = QFrame(self.main_body_frame)
        self.left_menu_cont_frame.setObjectName(u"left_menu_cont_frame")
        self.left_menu_cont_frame.setMinimumSize(QSize(55, 0))
        self.left_menu_cont_frame.setMaximumSize(QSize(20, 16777215))
        self.left_menu_cont_frame.setFrameShape(QFrame.StyledPanel)
        self.left_menu_cont_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.left_menu_cont_frame)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.left_menu_cont_frame)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setMinimumSize(QSize(250, 0))
        self.menu_frame.setStyleSheet(u"background-color: rgb(30, 30, 30);")
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.overview_button = QPushButton(self.menu_frame)
        self.overview_button.setObjectName(u"overview_button")
        self.overview_button.setGeometry(QRect(10, 10, 34, 30))
        font2 = QFont()
        font2.setPointSize(12)
        self.overview_button.setFont(font2)
        self.overview_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon4 = QIcon()
        icon4.addFile(u":/images/ui_images/explore_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.overview_button.setIcon(icon4)
        self.overview_button.setIconSize(QSize(30, 30))
        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(60, 17, 71, 16))
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.internet_button = QPushButton(self.menu_frame)
        self.internet_button.setObjectName(u"internet_button")
        self.internet_button.setGeometry(QRect(10, 60, 34, 30))
        self.internet_button.setFont(font2)
        self.internet_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon5 = QIcon()
        icon5.addFile(u":/images/ui_images/public_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.internet_button.setIcon(icon5)
        self.internet_button.setIconSize(QSize(30, 30))
        self.computer_button = QPushButton(self.menu_frame)
        self.computer_button.setObjectName(u"computer_button")
        self.computer_button.setGeometry(QRect(10, 110, 34, 30))
        self.computer_button.setFont(font2)
        self.computer_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon6 = QIcon()
        icon6.addFile(u":/images/ui_images/computer_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.computer_button.setIcon(icon6)
        self.computer_button.setIconSize(QSize(30, 30))
        self.network_button = QPushButton(self.menu_frame)
        self.network_button.setObjectName(u"network_button")
        self.network_button.setGeometry(QRect(10, 310, 34, 30))
        self.network_button.setFont(font2)
        self.network_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon7 = QIcon()
        icon7.addFile(u":/images/ui_images/signal_wifi_statusbar_4_bar_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.network_button.setIcon(icon7)
        self.network_button.setIconSize(QSize(30, 30))
        self.sensor_button = QPushButton(self.menu_frame)
        self.sensor_button.setObjectName(u"sensor_button")
        self.sensor_button.setGeometry(QRect(10, 260, 34, 30))
        self.sensor_button.setFont(font2)
        self.sensor_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon8 = QIcon()
        icon8.addFile(u":/images/ui_images/thermostat_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.sensor_button.setIcon(icon8)
        self.sensor_button.setIconSize(QSize(30, 30))
        self.storage_button = QPushButton(self.menu_frame)
        self.storage_button.setObjectName(u"storage_button")
        self.storage_button.setGeometry(QRect(10, 210, 34, 30))
        self.storage_button.setFont(font2)
        self.storage_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon9 = QIcon()
        icon9.addFile(u":/images/ui_images/sd_storage_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.storage_button.setIcon(icon9)
        self.storage_button.setIconSize(QSize(30, 30))
        self.system_info_button = QPushButton(self.menu_frame)
        self.system_info_button.setObjectName(u"system_info_button")
        self.system_info_button.setGeometry(QRect(10, 160, 34, 30))
        self.system_info_button.setFont(font2)
        self.system_info_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u":/images/ui_images/info_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.system_info_button.setIcon(icon10)
        self.system_info_button.setIconSize(QSize(30, 30))
        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(60, 117, 47, 16))
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(60, 67, 47, 16))
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(60, 166, 151, 21))
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(60, 266, 81, 16))
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(60, 216, 81, 21))
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_10 = QLabel(self.menu_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(60, 316, 81, 16))
        self.label_10.setFont(font2)
        self.label_10.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.settings_button = QPushButton(self.menu_frame)
        self.settings_button.setObjectName(u"settings_button")
        self.settings_button.setGeometry(QRect(10, 360, 34, 30))
        self.settings_button.setFont(font2)
        self.settings_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u":/images/ui_images/settings_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon11)
        self.settings_button.setIconSize(QSize(30, 30))
        self.label_11 = QLabel(self.menu_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 366, 101, 21))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_9.addWidget(self.menu_frame)


        self.horizontalLayout_8.addWidget(self.left_menu_cont_frame)

        self.main_body_contents = QFrame(self.main_body_frame)
        self.main_body_contents.setObjectName(u"main_body_contents")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.main_body_contents.sizePolicy().hasHeightForWidth())
        self.main_body_contents.setSizePolicy(sizePolicy1)
        self.main_body_contents.setFrameShape(QFrame.StyledPanel)
        self.main_body_contents.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.overview_page = QWidget()
        self.overview_page.setObjectName(u"overview_page")
        self.stackedWidget.addWidget(self.overview_page)
        self.internet_page = QWidget()
        self.internet_page.setObjectName(u"internet_page")
        self.stackedWidget.addWidget(self.internet_page)
        self.computer_page = QWidget()
        self.computer_page.setObjectName(u"computer_page")
        self.verticalLayout_3 = QVBoxLayout(self.computer_page)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.cpu_info_frame = QFrame(self.computer_page)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.cpu_info_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_28 = QLabel(self.cpu_info_frame)
        self.label_28.setObjectName(u"label_28")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_28.setFont(font3)
        self.label_28.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_28, 0, 0, 1, 1)

        self.label_12 = QLabel(self.cpu_info_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_12, 1, 0, 1, 1)

        self.label_13 = QLabel(self.cpu_info_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_13, 2, 0, 1, 1)

        self.label_14 = QLabel(self.cpu_info_frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.label_14, 3, 0, 1, 1)

        self.cpu_per = QLabel(self.cpu_info_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cpu_per, 2, 1, 1, 1)

        self.cpu_count = QLabel(self.cpu_info_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cpu_count, 1, 1, 1, 1)

        self.cpu_main_core = QLabel(self.cpu_info_frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cpu_main_core, 3, 1, 1, 1)

        self.frame_18 = QFrame(self.cpu_info_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.cpu_progress_bar = QProgressBar(self.frame_18)
        self.cpu_progress_bar.setObjectName(u"cpu_progress_bar")
        self.cpu_progress_bar.setGeometry(QRect(80, 60, 150, 30))
        self.cpu_progress_bar.setMinimumSize(QSize(150, 30))
        self.cpu_progress_bar.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.cpu_progress_bar.setValue(24)
        self.label_cpu_progress_bar = QLabel(self.frame_18)
        self.label_cpu_progress_bar.setObjectName(u"label_cpu_progress_bar")
        self.label_cpu_progress_bar.setGeometry(QRect(87, 68, 31, 15))
        self.label_cpu_progress_bar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout.addWidget(self.frame_18, 1, 2, 3, 1)


        self.verticalLayout_3.addWidget(self.cpu_info_frame)

        self.ram_info = QFrame(self.computer_page)
        self.ram_info.setObjectName(u"ram_info")
        self.ram_info.setFrameShape(QFrame.StyledPanel)
        self.ram_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.ram_info)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_24 = QLabel(self.ram_info)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_24, 3, 0, 1, 1)

        self.free_ram = QLabel(self.ram_info)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.free_ram, 3, 1, 1, 1)

        self.ram_usage = QLabel(self.ram_info)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.ram_usage, 4, 1, 1, 1)

        self.label_18 = QLabel(self.ram_info)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_18, 0, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label2 = QLabel(self.ram_info)
        self.label2.setObjectName(u"label2")
        self.label2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label2, 2, 0, 1, 1)

        self.label1 = QLabel(self.ram_info)
        self.label1.setObjectName(u"label1")
        self.label1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label1, 1, 0, 1, 1)

        self.label_26 = QLabel(self.ram_info)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.label_26, 4, 0, 1, 1)

        self.available_ram = QLabel(self.ram_info)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.available_ram, 1, 1, 1, 1)

        self.used_ram = QLabel(self.ram_info)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.gridLayout_2.addWidget(self.used_ram, 2, 1, 1, 1)

        self.frame_19 = QFrame(self.ram_info)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.ram_progress_bar = QProgressBar(self.frame_19)
        self.ram_progress_bar.setObjectName(u"ram_progress_bar")
        self.ram_progress_bar.setGeometry(QRect(80, 60, 150, 30))
        self.ram_progress_bar.setMinimumSize(QSize(150, 30))
        self.ram_progress_bar.setStyleSheet(u"background-color: rgb(40, 40, 40);")
        self.ram_progress_bar.setValue(24)
        self.label_ram_progress_bar = QLabel(self.frame_19)
        self.label_ram_progress_bar.setObjectName(u"label_ram_progress_bar")
        self.label_ram_progress_bar.setGeometry(QRect(87, 68, 31, 15))
        self.label_ram_progress_bar.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);")

        self.gridLayout_2.addWidget(self.frame_19, 1, 2, 3, 1)


        self.verticalLayout_3.addWidget(self.ram_info)

        self.stackedWidget.addWidget(self.computer_page)
        self.system_info_page = QWidget()
        self.system_info_page.setObjectName(u"system_info_page")
        self.horizontalLayout_15 = QHBoxLayout(self.system_info_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, -1, -1, -1)
        self.frame = QFrame(self.system_info_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(9, 9, 9, 9)
        self.frame_10 = QFrame(self.frame)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.label_29 = QLabel(self.frame_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.label_29)


        self.verticalLayout_5.addWidget(self.frame_10, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_14.setContentsMargins(9, 9, 9, 9)
        self.label_30 = QLabel(self.frame_2)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.label_30)


        self.verticalLayout_5.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_12.setSpacing(0)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_4 = QFrame(self.frame_3)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.frame_5 = QFrame(self.frame_4)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_5)
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_32 = QLabel(self.frame_5)
        self.label_32.setObjectName(u"label_32")
        font4 = QFont()
        font4.setBold(True)
        self.label_32.setFont(font4)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_32)

        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font4)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_31)

        self.label_33 = QLabel(self.frame_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font4)
        self.label_33.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_33)


        self.horizontalLayout_10.addWidget(self.frame_5)

        self.frame_7 = QFrame(self.frame_4)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.label_35 = QLabel(self.frame_7)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_35)

        self.label_36 = QLabel(self.frame_7)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_36)

        self.label_34 = QLabel(self.frame_7)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.label_34)


        self.horizontalLayout_10.addWidget(self.frame_7)


        self.horizontalLayout_12.addWidget(self.frame_4)

        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.frame_8)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_37 = QLabel(self.frame_8)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font4)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_8)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font4)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font4)
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_39)


        self.horizontalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_40 = QLabel(self.frame_9)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_40)

        self.label_42 = QLabel(self.frame_9)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_42)

        self.label_41 = QLabel(self.frame_9)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.label_41)


        self.horizontalLayout_11.addWidget(self.frame_9)


        self.horizontalLayout_12.addWidget(self.frame_6)


        self.verticalLayout_5.addWidget(self.frame_3)


        self.horizontalLayout_15.addWidget(self.frame)

        self.stackedWidget.addWidget(self.system_info_page)
        self.storage_page = QWidget()
        self.storage_page.setObjectName(u"storage_page")
        self.verticalLayout_6 = QVBoxLayout(self.storage_page)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_11 = QFrame(self.storage_page)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_11)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_43 = QLabel(self.frame_11)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font3)
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_4.addWidget(self.label_43)

        self.tableWidget = QTableWidget(self.frame_11)
        if (self.tableWidget.columnCount() < 9):
            self.tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font4);
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.verticalHeader().setMinimumSectionSize(19)
        self.tableWidget.verticalHeader().setDefaultSectionSize(30)

        self.verticalLayout_4.addWidget(self.tableWidget)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.stackedWidget.addWidget(self.storage_page)
        self.sensor_page = QWidget()
        self.sensor_page.setObjectName(u"sensor_page")
        self.verticalLayout_11 = QVBoxLayout(self.sensor_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_12 = QFrame(self.sensor_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_12)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_44 = QLabel(self.frame_12)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font3)
        self.label_44.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_44)

        self.tableWidget_2 = QTableWidget(self.frame_12)
        if (self.tableWidget_2.columnCount() < 5):
            self.tableWidget_2.setColumnCount(5)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem13)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_12.addWidget(self.tableWidget_2)


        self.verticalLayout_11.addWidget(self.frame_12)

        self.stackedWidget.addWidget(self.sensor_page)
        self.network_page = QWidget()
        self.network_page.setObjectName(u"network_page")
        self.verticalLayout_13 = QVBoxLayout(self.network_page)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.frame_13 = QFrame(self.network_page)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_13)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_45 = QLabel(self.frame_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font3)
        self.label_45.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_14.addWidget(self.label_45)

        self.scrollArea = QScrollArea(self.frame_13)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 926, 507))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 50)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_46 = QLabel(self.frame_14)
        self.label_46.setObjectName(u"label_46")
        font5 = QFont()
        font5.setPointSize(10)
        font5.setBold(True)
        self.label_46.setFont(font5)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_46)

        self.tableWidget_3 = QTableWidget(self.frame_14)
        if (self.tableWidget_3.columnCount() < 5):
            self.tableWidget_3.setColumnCount(5)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_16.addWidget(self.tableWidget_3)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_47 = QLabel(self.frame_15)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font5)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.label_47)

        self.tableWidget_4 = QTableWidget(self.frame_15)
        if (self.tableWidget_4.columnCount() < 9):
            self.tableWidget_4.setColumnCount(9)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(8, __qtablewidgetitem27)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_4.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_17.addWidget(self.tableWidget_4)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_16)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_48 = QLabel(self.frame_16)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font5)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.label_48)

        self.tableWidget_5 = QTableWidget(self.frame_16)
        if (self.tableWidget_5.columnCount() < 5):
            self.tableWidget_5.setColumnCount(5)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget_5.setHorizontalHeaderItem(4, __qtablewidgetitem32)
        self.tableWidget_5.setObjectName(u"tableWidget_5")
        self.tableWidget_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_5.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_18.addWidget(self.tableWidget_5)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.label_49 = QLabel(self.frame_17)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font5)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.label_49)

        self.tableWidget_6 = QTableWidget(self.frame_17)
        if (self.tableWidget_6.columnCount() < 7):
            self.tableWidget_6.setColumnCount(7)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(5, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget_6.setHorizontalHeaderItem(6, __qtablewidgetitem39)
        self.tableWidget_6.setObjectName(u"tableWidget_6")
        self.tableWidget_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.tableWidget_6.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_19.addWidget(self.tableWidget_6)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.network_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.main_body_contents)


        self.verticalLayout.addWidget(self.main_body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.footer_left_frame)
        self.label.setObjectName(u"label")
        font6 = QFont()
        font6.setFamilies([u"Dosis"])
        font6.setPointSize(10)
        font6.setBold(False)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_7.addWidget(self.label)


        self.horizontalLayout_5.addWidget(self.footer_left_frame, 0, Qt.AlignLeft|Qt.AlignBottom)

        self.footer_right = QFrame(self.footer_frame)
        self.footer_right.setObjectName(u"footer_right")
        self.footer_right.setFrameShape(QFrame.StyledPanel)
        self.footer_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_right)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_2 = QPushButton(self.footer_right)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_6.addWidget(self.pushButton_2)


        self.horizontalLayout_5.addWidget(self.footer_right)

        self.size_grip = QFrame(self.footer_frame)
        self.size_grip.setObjectName(u"size_grip")
        self.size_grip.setMinimumSize(QSize(10, 10))
        self.size_grip.setMaximumSize(QSize(10, 10))
        self.size_grip.setFrameShape(QFrame.StyledPanel)
        self.size_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.size_grip, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(2)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.open_close_side_bar_btn.setText(QCoreApplication.translate("MainWindow", u"Men\u00fc", None))
        self.label_3.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"DynoDashboard", None))
        self.minimize_window_button.setText("")
        self.restore_window_button.setText("")
        self.close_winow_button.setText("")
        self.overview_button.setText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u00dcbersicht", None))
        self.internet_button.setText("")
        self.computer_button.setText("")
        self.network_button.setText("")
        self.sensor_button.setText("")
        self.storage_button.setText("")
        self.system_info_button.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"PC", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Internet", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sesnsoren", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Speicher", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Netzwerke", None))
        self.settings_button.setText("")
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Einstellungen", None))
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"CPU & Arbeitsspeicher", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU %", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_cpu_progress_bar.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Freier Ram", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Gesamter Ram", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Verwendeter Ram", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"Verf\u00fcgbarer Ram", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Ram-Nutzung", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_ram_progress_bar.setText(QCoreApplication.translate("MainWindow", u"Text", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Plattform", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"System Datum", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Prozessor", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Maschine", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"System Zeit", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Speicher", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Ger\u00e4t", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Gr\u00f6\u00dfte Datei", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Gr\u00f6\u00dfter Pfad", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Gesamter Speicher", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Benutzter Speicher", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Freier Speicher", None));
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"Sensoren", None))
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem9 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem10 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Aktuell", None));
        ___qtablewidgetitem11 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"High", None));
        ___qtablewidgetitem12 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Kritisch", None));
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Netzwerke", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem13 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem14 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem15 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Geschwindigkeit", None));
        ___qtablewidgetitem16 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Netzwerk I/O Z\u00e4hler", None))
        ___qtablewidgetitem17 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"I/O", None));
        ___qtablewidgetitem18 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Bytes gesendet", None));
        ___qtablewidgetitem19 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Bytes empfangen", None));
        ___qtablewidgetitem20 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Packete gesendet", None));
        ___qtablewidgetitem21 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Packete empfangen", None));
        ___qtablewidgetitem22 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Err In", None));
        ___qtablewidgetitem23 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Err Out", None));
        ___qtablewidgetitem24 = self.tableWidget_4.horizontalHeaderItem(7)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem25 = self.tableWidget_4.horizontalHeaderItem(8)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Netzwerk Adressen", None))
        ___qtablewidgetitem26 = self.tableWidget_5.horizontalHeaderItem(1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Familie", None));
        ___qtablewidgetitem27 = self.tableWidget_5.horizontalHeaderItem(2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem28 = self.tableWidget_5.horizontalHeaderItem(3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem29 = self.tableWidget_5.horizontalHeaderItem(4)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Netzwerk Verbindungen", None))
        ___qtablewidgetitem30 = self.tableWidget_6.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem31 = self.tableWidget_6.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem32 = self.tableWidget_6.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Familie", None));
        ___qtablewidgetitem33 = self.tableWidget_6.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Familie", None));
        ___qtablewidgetitem34 = self.tableWidget_6.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem35 = self.tableWidget_6.horizontalHeaderItem(5)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Tatus", None));
        ___qtablewidgetitem36 = self.tableWidget_6.horizontalHeaderItem(6)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version 0.1 | Copyright Marcel Peplies", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

