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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QScrollArea, QSizePolicy, QStackedWidget, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)
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
        self.label_6.setGeometry(QRect(60, 67, 111, 16))
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
        self.settings_button.setGeometry(QRect(10, 410, 34, 30))
        self.settings_button.setFont(font2)
        self.settings_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon11 = QIcon()
        icon11.addFile(u":/images/ui_images/settings_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.settings_button.setIcon(icon11)
        self.settings_button.setIconSize(QSize(30, 30))
        self.label_11 = QLabel(self.menu_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(60, 416, 101, 21))
        self.label_11.setFont(font2)
        self.label_11.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.activity_button = QPushButton(self.menu_frame)
        self.activity_button.setObjectName(u"activity_button")
        self.activity_button.setGeometry(QRect(10, 360, 34, 30))
        icon12 = QIcon()
        icon12.addFile(u":/images/ui_images/show_chart_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_button.setIcon(icon12)
        self.activity_button.setIconSize(QSize(30, 30))
        self.label_15 = QLabel(self.menu_frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(60, 366, 91, 21))
        self.label_15.setFont(font2)
        self.label_15.setStyleSheet(u"color: rgb(255, 255, 255);")

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
        self.verticalLayout_3 = QVBoxLayout(self.main_body_contents)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.stackedWidget = QStackedWidget(self.main_body_contents)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setMinimumSize(QSize(0, 0))
        self.overview_page = QWidget()
        self.overview_page.setObjectName(u"overview_page")
        self.stackedWidget.addWidget(self.overview_page)
        self.internet_page = QWidget()
        self.internet_page.setObjectName(u"internet_page")
        self.verticalLayout_29 = QVBoxLayout(self.internet_page)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.frame_37 = QFrame(self.internet_page)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setFrameShape(QFrame.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Raised)
        self.verticalLayout_30 = QVBoxLayout(self.frame_37)
        self.verticalLayout_30.setSpacing(0)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.verticalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.label_21 = QLabel(self.frame_37)
        self.label_21.setObjectName(u"label_21")
        font3 = QFont()
        font3.setPointSize(14)
        font3.setBold(True)
        self.label_21.setFont(font3)
        self.label_21.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_30.addWidget(self.label_21)


        self.verticalLayout_29.addWidget(self.frame_37)

        self.scrollArea_2 = QScrollArea(self.internet_page)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.scrollArea_2.sizePolicy().hasHeightForWidth())
        self.scrollArea_2.setSizePolicy(sizePolicy2)
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_5 = QWidget()
        self.scrollAreaWidgetContents_5.setObjectName(u"scrollAreaWidgetContents_5")
        self.scrollAreaWidgetContents_5.setGeometry(QRect(0, -106, 944, 510))
        self.verticalLayout_47 = QVBoxLayout(self.scrollAreaWidgetContents_5)
        self.verticalLayout_47.setSpacing(0)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_57 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_57.setObjectName(u"frame_57")
        sizePolicy2.setHeightForWidth(self.frame_57.sizePolicy().hasHeightForWidth())
        self.frame_57.setSizePolicy(sizePolicy2)
        self.frame_57.setFrameShape(QFrame.StyledPanel)
        self.frame_57.setFrameShadow(QFrame.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_57)
        self.verticalLayout_41.setSpacing(0)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_41.setContentsMargins(0, -1, 0, 0)
        self.frame_58 = QFrame(self.frame_57)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Raised)
        self.verticalLayout_42 = QVBoxLayout(self.frame_58)
        self.verticalLayout_42.setSpacing(0)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.verticalLayout_42.setContentsMargins(0, -1, 0, 10)
        self.label_53 = QLabel(self.frame_58)
        self.label_53.setObjectName(u"label_53")
        font4 = QFont()
        font4.setPointSize(10)
        font4.setBold(True)
        self.label_53.setFont(font4)
        self.label_53.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_42.addWidget(self.label_53)


        self.verticalLayout_41.addWidget(self.frame_58)

        self.frame_59 = QFrame(self.frame_57)
        self.frame_59.setObjectName(u"frame_59")
        sizePolicy2.setHeightForWidth(self.frame_59.sizePolicy().hasHeightForWidth())
        self.frame_59.setSizePolicy(sizePolicy2)
        self.frame_59.setFrameShape(QFrame.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_59)
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.frame_60 = QFrame(self.frame_59)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setFrameShape(QFrame.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.frame_60)
        self.verticalLayout_43.setSpacing(0)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.verticalLayout_43.setContentsMargins(0, 0, 0, 0)
        self.label_55 = QLabel(self.frame_60)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_55)

        self.label_56 = QLabel(self.frame_60)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_56)

        self.label_57 = QLabel(self.frame_60)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_60)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_58)

        self.label_59 = QLabel(self.frame_60)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_59)

        self.label_60 = QLabel(self.frame_60)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_43.addWidget(self.label_60)


        self.horizontalLayout_30.addWidget(self.frame_60)

        self.frame_61 = QFrame(self.frame_59)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.frame_61)
        self.verticalLayout_44.setSpacing(0)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.verticalLayout_44.setContentsMargins(0, 0, 0, 0)
        self.is_connected_2 = QLabel(self.frame_61)
        self.is_connected_2.setObjectName(u"is_connected_2")
        self.is_connected_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.is_connected_2)

        self.is_linked_2 = QLabel(self.frame_61)
        self.is_linked_2.setObjectName(u"is_linked_2")
        self.is_linked_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.is_linked_2)

        self.external_ip_v4_2 = QLabel(self.frame_61)
        self.external_ip_v4_2.setObjectName(u"external_ip_v4_2")
        self.external_ip_v4_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.external_ip_v4_2)

        self.external_ip_v6_2 = QLabel(self.frame_61)
        self.external_ip_v6_2.setObjectName(u"external_ip_v6_2")
        self.external_ip_v6_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.external_ip_v6_2)

        self.connection_uptime_2 = QLabel(self.frame_61)
        self.connection_uptime_2.setObjectName(u"connection_uptime_2")
        self.connection_uptime_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.connection_uptime_2)

        self.device_uptime_2 = QLabel(self.frame_61)
        self.device_uptime_2.setObjectName(u"device_uptime_2")
        self.device_uptime_2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_44.addWidget(self.device_uptime_2)


        self.horizontalLayout_30.addWidget(self.frame_61)

        self.frame_62 = QFrame(self.frame_59)
        self.frame_62.setObjectName(u"frame_62")
        sizePolicy2.setHeightForWidth(self.frame_62.sizePolicy().hasHeightForWidth())
        self.frame_62.setSizePolicy(sizePolicy2)
        self.frame_62.setFrameShape(QFrame.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_62)
        self.verticalLayout_45.setSpacing(0)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(0, 0, 0, -1)
        self.frame_63 = QFrame(self.frame_62)
        self.frame_63.setObjectName(u"frame_63")
        sizePolicy3 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.frame_63.sizePolicy().hasHeightForWidth())
        self.frame_63.setSizePolicy(sizePolicy3)
        self.frame_63.setMinimumSize(QSize(150, 150))
        self.frame_63.setMaximumSize(QSize(150, 150))
        self.frame_63.setStyleSheet(u"border: 3px solid;\n"
"border-color: green;\n"
"border-radius: 75px;")
        self.frame_63.setFrameShape(QFrame.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Raised)
        self.internet_button_4 = QPushButton(self.frame_63)
        self.internet_button_4.setObjectName(u"internet_button_4")
        self.internet_button_4.setGeometry(QRect(59, 10, 31, 41))
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.internet_button_4.sizePolicy().hasHeightForWidth())
        self.internet_button_4.setSizePolicy(sizePolicy4)
        self.internet_button_4.setFont(font2)
        self.internet_button_4.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        icon13 = QIcon()
        icon13.addFile(u":/images/ui_images/get_app_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.internet_button_4.setIcon(icon13)
        self.internet_button_4.setIconSize(QSize(40, 40))
        self.current_download_2 = QLabel(self.frame_63)
        self.current_download_2.setObjectName(u"current_download_2")
        self.current_download_2.setGeometry(QRect(22, 66, 111, 21))
        font5 = QFont()
        font5.setPointSize(16)
        font5.setBold(True)
        self.current_download_2.setFont(font5)
        self.current_download_2.setLayoutDirection(Qt.LeftToRight)
        self.current_download_2.setStyleSheet(u"border:none;")
        self.current_download_2.setAlignment(Qt.AlignCenter)
        self.max_download_2 = QLabel(self.frame_63)
        self.max_download_2.setObjectName(u"max_download_2")
        self.max_download_2.setGeometry(QRect(65, 100, 64, 16))
        font6 = QFont()
        font6.setPointSize(10)
        self.max_download_2.setFont(font6)
        self.max_download_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")
        self.label_61 = QLabel(self.frame_63)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(31, 100, 31, 16))
        self.label_61.setFont(font6)
        self.label_61.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_45.addWidget(self.frame_63, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_64 = QFrame(self.frame_62)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_31.setSpacing(0)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.horizontalLayout_31.setContentsMargins(0, 0, 0, 0)
        self.label_62 = QLabel(self.frame_64)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_31.addWidget(self.label_62)

        self.total_bytes_received_2 = QLabel(self.frame_64)
        self.total_bytes_received_2.setObjectName(u"total_bytes_received_2")
        font7 = QFont()
        font7.setBold(True)
        self.total_bytes_received_2.setFont(font7)
        self.total_bytes_received_2.setMargin(5)

        self.horizontalLayout_31.addWidget(self.total_bytes_received_2)


        self.verticalLayout_45.addWidget(self.frame_64, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_30.addWidget(self.frame_62, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.frame_65 = QFrame(self.frame_59)
        self.frame_65.setObjectName(u"frame_65")
        sizePolicy2.setHeightForWidth(self.frame_65.sizePolicy().hasHeightForWidth())
        self.frame_65.setSizePolicy(sizePolicy2)
        self.frame_65.setFrameShape(QFrame.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_65)
        self.verticalLayout_46.setSpacing(0)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(0, 0, 0, -1)
        self.frame_66 = QFrame(self.frame_65)
        self.frame_66.setObjectName(u"frame_66")
        sizePolicy3.setHeightForWidth(self.frame_66.sizePolicy().hasHeightForWidth())
        self.frame_66.setSizePolicy(sizePolicy3)
        self.frame_66.setMinimumSize(QSize(150, 150))
        self.frame_66.setMaximumSize(QSize(150, 150))
        self.frame_66.setStyleSheet(u"border: 3px solid;\n"
"border-color: yellow;\n"
"border-radius: 75px;")
        self.frame_66.setFrameShape(QFrame.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Raised)
        self.internet_button_5 = QPushButton(self.frame_66)
        self.internet_button_5.setObjectName(u"internet_button_5")
        self.internet_button_5.setGeometry(QRect(59, 10, 31, 41))
        sizePolicy4.setHeightForWidth(self.internet_button_5.sizePolicy().hasHeightForWidth())
        self.internet_button_5.setSizePolicy(sizePolicy4)
        self.internet_button_5.setFont(font2)
        self.internet_button_5.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"border: none;")
        icon14 = QIcon()
        icon14.addFile(u":/images/ui_images/upload_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.internet_button_5.setIcon(icon14)
        self.internet_button_5.setIconSize(QSize(40, 40))
        self.current_upload_2 = QLabel(self.frame_66)
        self.current_upload_2.setObjectName(u"current_upload_2")
        self.current_upload_2.setGeometry(QRect(22, 66, 111, 21))
        self.current_upload_2.setFont(font5)
        self.current_upload_2.setLayoutDirection(Qt.LeftToRight)
        self.current_upload_2.setStyleSheet(u"border:none;")
        self.current_upload_2.setAlignment(Qt.AlignCenter)
        self.label_63 = QLabel(self.frame_66)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setGeometry(QRect(31, 100, 31, 16))
        self.label_63.setFont(font6)
        self.label_63.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")
        self.max_upload_2 = QLabel(self.frame_66)
        self.max_upload_2.setObjectName(u"max_upload_2")
        self.max_upload_2.setGeometry(QRect(65, 100, 66, 16))
        self.max_upload_2.setFont(font6)
        self.max_upload_2.setStyleSheet(u"border:none;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_46.addWidget(self.frame_66)

        self.frame_67 = QFrame(self.frame_65)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_32 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_64 = QLabel(self.frame_67)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_32.addWidget(self.label_64)

        self.total_bytes_sent_2 = QLabel(self.frame_67)
        self.total_bytes_sent_2.setObjectName(u"total_bytes_sent_2")
        self.total_bytes_sent_2.setFont(font7)

        self.horizontalLayout_32.addWidget(self.total_bytes_sent_2)


        self.verticalLayout_46.addWidget(self.frame_67, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_30.addWidget(self.frame_65, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_41.addWidget(self.frame_59)


        self.verticalLayout_47.addWidget(self.frame_57)

        self.frame_38 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_38)
        self.verticalLayout_37.setSpacing(0)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(0, -1, 0, 0)
        self.frame_40 = QFrame(self.frame_38)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setFrameShape(QFrame.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_40)
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.frame_40)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font4)
        self.label_40.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_29.addWidget(self.label_40)


        self.verticalLayout_37.addWidget(self.frame_40)

        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_39)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_51 = QFrame(self.frame_39)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setFrameShape(QFrame.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Raised)
        self.verticalLayout_38 = QVBoxLayout(self.frame_51)
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(0, 0, 0, 0)
        self.label_43 = QLabel(self.frame_51)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_38.addWidget(self.label_43)

        self.label_42 = QLabel(self.frame_51)
        self.label_42.setObjectName(u"label_42")
        self.label_42.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_38.addWidget(self.label_42)


        self.horizontalLayout_33.addWidget(self.frame_51)

        self.frame_52 = QFrame(self.frame_39)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setFrameShape(QFrame.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_52)
        self.verticalLayout_39.setSpacing(0)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_39.setContentsMargins(0, 0, 0, 0)
        self.ssid = QLabel(self.frame_52)
        self.ssid.setObjectName(u"ssid")
        self.ssid.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.ssid)

        self.connected_devices = QLabel(self.frame_52)
        self.connected_devices.setObjectName(u"connected_devices")
        self.connected_devices.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_39.addWidget(self.connected_devices)


        self.horizontalLayout_33.addWidget(self.frame_52)

        self.frame_53 = QFrame(self.frame_39)
        self.frame_53.setObjectName(u"frame_53")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.frame_53.sizePolicy().hasHeightForWidth())
        self.frame_53.setSizePolicy(sizePolicy5)
        self.frame_53.setMinimumSize(QSize(75, 75))
        self.frame_53.setFrameShape(QFrame.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_53)

        self.frame_54 = QFrame(self.frame_39)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setFrameShape(QFrame.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_33.addWidget(self.frame_54)


        self.verticalLayout_37.addWidget(self.frame_39)


        self.verticalLayout_47.addWidget(self.frame_38)

        self.frame_55 = QFrame(self.scrollAreaWidgetContents_5)
        self.frame_55.setObjectName(u"frame_55")
        self.frame_55.setFrameShape(QFrame.StyledPanel)
        self.frame_55.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.frame_55)
        self.verticalLayout_40.setSpacing(0)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(0, 0, 0, 0)
        self.frame_68 = QFrame(self.frame_55)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_68)
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.label_65 = QLabel(self.frame_68)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font4)
        self.label_65.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_34.addWidget(self.label_65)


        self.verticalLayout_40.addWidget(self.frame_68)

        self.frame_56 = QFrame(self.frame_55)
        self.frame_56.setObjectName(u"frame_56")
        self.frame_56.setFrameShape(QFrame.StyledPanel)
        self.frame_56.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_56)
        self.horizontalLayout_35.setSpacing(0)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_35.setContentsMargins(0, 10, 0, 0)
        self.call_tableWidget = QTableWidget(self.frame_56)
        if (self.call_tableWidget.columnCount() < 4):
            self.call_tableWidget.setColumnCount(4)
        __qtablewidgetitem = QTableWidgetItem()
        self.call_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.call_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.call_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.call_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        self.call_tableWidget.setObjectName(u"call_tableWidget")
        sizePolicy6 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.call_tableWidget.sizePolicy().hasHeightForWidth())
        self.call_tableWidget.setSizePolicy(sizePolicy6)
        self.call_tableWidget.setMinimumSize(QSize(0, 150))
        self.call_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.call_tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.horizontalLayout_35.addWidget(self.call_tableWidget)


        self.verticalLayout_40.addWidget(self.frame_56)


        self.verticalLayout_47.addWidget(self.frame_55)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_5)

        self.verticalLayout_29.addWidget(self.scrollArea_2)

        self.stackedWidget.addWidget(self.internet_page)
        self.computer_page = QWidget()
        self.computer_page.setObjectName(u"computer_page")
        self.verticalLayout_2 = QVBoxLayout(self.computer_page)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_24 = QFrame(self.computer_page)
        self.frame_24.setObjectName(u"frame_24")
        sizePolicy5.setHeightForWidth(self.frame_24.sizePolicy().hasHeightForWidth())
        self.frame_24.setSizePolicy(sizePolicy5)
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_24)
        self.horizontalLayout_19.setSpacing(0)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.label_50 = QLabel(self.frame_24)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font3)
        self.label_50.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_19.addWidget(self.label_50)


        self.verticalLayout_2.addWidget(self.frame_24, 0, Qt.AlignTop)

        self.cpu_info_frame = QFrame(self.computer_page)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        sizePolicy2.setHeightForWidth(self.cpu_info_frame.sizePolicy().hasHeightForWidth())
        self.cpu_info_frame.setSizePolicy(sizePolicy2)
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.cpu_info_frame)
        self.horizontalLayout_16.setSpacing(0)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.frame_20 = QFrame(self.cpu_info_frame)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.frame_20)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_22 = QFrame(self.frame_20)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_22)
        self.horizontalLayout_17.setSpacing(0)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.frame_23 = QFrame(self.frame_22)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_23)
        self.verticalLayout_21.setSpacing(0)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.label_12 = QLabel(self.frame_23)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_23)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.label_13)

        self.label_14 = QLabel(self.frame_23)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_21.addWidget(self.label_14)


        self.horizontalLayout_17.addWidget(self.frame_23)

        self.frame_25 = QFrame(self.frame_22)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_25)
        self.verticalLayout_22.setSpacing(0)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(0, 0, 0, 0)
        self.cpu_count = QLabel(self.frame_25)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.cpu_count)

        self.cpu_per = QLabel(self.frame_25)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.cpu_per)

        self.cpu_main_core = QLabel(self.frame_25)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_22.addWidget(self.cpu_main_core)


        self.horizontalLayout_17.addWidget(self.frame_25)


        self.verticalLayout_20.addWidget(self.frame_22)


        self.horizontalLayout_16.addWidget(self.frame_20)

        self.frame_18 = QFrame(self.cpu_info_frame)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_18)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_20 = QLabel(self.frame_18)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font3)
        self.label_20.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_28.addWidget(self.label_20, 0, Qt.AlignHCenter)

        self.frame_35 = QFrame(self.frame_18)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setMinimumSize(QSize(150, 150))
        self.frame_35.setMaximumSize(QSize(150, 150))
        self.frame_35.setStyleSheet(u"border: 3px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 75px;")
        self.frame_35.setFrameShape(QFrame.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Raised)
        self.cpu_percent_large = QLabel(self.frame_35)
        self.cpu_percent_large.setObjectName(u"cpu_percent_large")
        self.cpu_percent_large.setGeometry(QRect(43, 55, 91, 41))
        font8 = QFont()
        font8.setPointSize(20)
        font8.setBold(True)
        self.cpu_percent_large.setFont(font8)
        self.cpu_percent_large.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_28.addWidget(self.frame_35)


        self.horizontalLayout_16.addWidget(self.frame_18, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.cpu_info_frame)

        self.ram_info = QFrame(self.computer_page)
        self.ram_info.setObjectName(u"ram_info")
        sizePolicy2.setHeightForWidth(self.ram_info.sizePolicy().hasHeightForWidth())
        self.ram_info.setSizePolicy(sizePolicy2)
        self.ram_info.setFrameShape(QFrame.StyledPanel)
        self.ram_info.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.ram_info)
        self.horizontalLayout_18.setSpacing(0)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.frame_26 = QFrame(self.ram_info)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_20.setSpacing(0)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_21 = QFrame(self.frame_26)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.verticalLayout_24 = QVBoxLayout(self.frame_21)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_18 = QLabel(self.frame_21)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.label_18)

        self.label1 = QLabel(self.frame_21)
        self.label1.setObjectName(u"label1")
        self.label1.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.label1)

        self.label2 = QLabel(self.frame_21)
        self.label2.setObjectName(u"label2")
        self.label2.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.label2)

        self.label_24 = QLabel(self.frame_21)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.label_24)

        self.label_26 = QLabel(self.frame_21)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_24.addWidget(self.label_26)


        self.horizontalLayout_20.addWidget(self.frame_21)

        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_27)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.ram_usage = QLabel(self.frame_27)
        self.ram_usage.setObjectName(u"ram_usage")
        self.ram_usage.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_23.addWidget(self.ram_usage)

        self.total_ram = QLabel(self.frame_27)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_23.addWidget(self.total_ram)

        self.available_ram = QLabel(self.frame_27)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_23.addWidget(self.available_ram)

        self.used_ram = QLabel(self.frame_27)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_23.addWidget(self.used_ram)

        self.free_ram = QLabel(self.frame_27)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_23.addWidget(self.free_ram)


        self.horizontalLayout_20.addWidget(self.frame_27)


        self.horizontalLayout_18.addWidget(self.frame_26)

        self.frame_19 = QFrame(self.ram_info)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_19)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_23 = QLabel(self.frame_19)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font3)
        self.label_23.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.label_23, 0, Qt.AlignHCenter)

        self.frame_36 = QFrame(self.frame_19)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setMinimumSize(QSize(150, 150))
        self.frame_36.setMaximumSize(QSize(150, 150))
        self.frame_36.setStyleSheet(u"border: 3px solid;\n"
"border-color: rgb(255, 255, 255);\n"
"border-radius: 75px;")
        self.frame_36.setFrameShape(QFrame.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Raised)
        self.ram_percent_large = QLabel(self.frame_36)
        self.ram_percent_large.setObjectName(u"ram_percent_large")
        self.ram_percent_large.setGeometry(QRect(43, 55, 91, 41))
        self.ram_percent_large.setFont(font8)
        self.ram_percent_large.setStyleSheet(u"border: none;\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_12.addWidget(self.frame_36)


        self.horizontalLayout_18.addWidget(self.frame_19, 0, Qt.AlignHCenter)


        self.verticalLayout_2.addWidget(self.ram_info)

        self.stackedWidget.addWidget(self.computer_page)
        self.system_info_page = QWidget()
        self.system_info_page.setObjectName(u"system_info_page")
        self.horizontalLayout_15 = QHBoxLayout(self.system_info_page)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(9, -1, -1, -1)
        self.frame = QFrame(self.system_info_page)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_28 = QFrame(self.frame)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_28)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.label_29 = QLabel(self.frame_28)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)
        self.label_29.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_26.addWidget(self.label_29)


        self.verticalLayout_5.addWidget(self.frame_28, 0, Qt.AlignTop)

        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_2)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.system_system = QLabel(self.frame_2)
        self.system_system.setObjectName(u"system_system")
        font9 = QFont()
        font9.setPointSize(12)
        font9.setBold(True)
        self.system_system.setFont(font9)
        self.system_system.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.system_system)

        self.system_release = QLabel(self.frame_2)
        self.system_release.setObjectName(u"system_release")
        font10 = QFont()
        font10.setPointSize(8)
        font10.setBold(True)
        self.system_release.setFont(font10)
        self.system_release.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_25.addWidget(self.system_release)


        self.verticalLayout_5.addWidget(self.frame_2, 0, Qt.AlignTop)

        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy7)
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
        self.label_32.setFont(font7)
        self.label_32.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_32)

        self.label_31 = QLabel(self.frame_5)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font7)
        self.label_31.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_8.addWidget(self.label_31)

        self.label_33 = QLabel(self.frame_5)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font7)
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
        self.system_version = QLabel(self.frame_7)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.system_version)

        self.system_platform = QLabel(self.frame_7)
        self.system_platform.setObjectName(u"system_platform")
        self.system_platform.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.system_platform)

        self.system_date = QLabel(self.frame_7)
        self.system_date.setObjectName(u"system_date")
        self.system_date.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_9.addWidget(self.system_date)


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
        self.label_37.setFont(font7)
        self.label_37.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_37)

        self.label_38 = QLabel(self.frame_8)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font7)
        self.label_38.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_38)

        self.label_39 = QLabel(self.frame_8)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font7)
        self.label_39.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_7.addWidget(self.label_39)


        self.horizontalLayout_11.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_9)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.system_processor = QLabel(self.frame_9)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.system_processor)

        self.system_machine = QLabel(self.frame_9)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.system_machine)

        self.system_time = QLabel(self.frame_9)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_10.addWidget(self.system_time)


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
        self.horizontalLayout_24 = QHBoxLayout(self.frame_11)
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.frame_11)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font3)
        self.label_17.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_24.addWidget(self.label_17)


        self.verticalLayout_6.addWidget(self.frame_11)

        self.frame_33 = QFrame(self.storage_page)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_23 = QHBoxLayout(self.frame_33)
        self.horizontalLayout_23.setSpacing(0)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.storage_tableWidget = QTableWidget(self.frame_33)
        if (self.storage_tableWidget.columnCount() < 10):
            self.storage_tableWidget.setColumnCount(10)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.storage_tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem13)
        self.storage_tableWidget.setObjectName(u"storage_tableWidget")
        self.storage_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.storage_tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.horizontalLayout_23.addWidget(self.storage_tableWidget)


        self.verticalLayout_6.addWidget(self.frame_33)

        self.stackedWidget.addWidget(self.storage_page)
        self.sensor_page = QWidget()
        self.sensor_page.setObjectName(u"sensor_page")
        self.verticalLayout_11 = QVBoxLayout(self.sensor_page)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_34 = QFrame(self.sensor_page)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setFrameShape(QFrame.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_34)
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.label_19 = QLabel(self.frame_34)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font3)
        self.label_19.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_25.addWidget(self.label_19)


        self.verticalLayout_11.addWidget(self.frame_34)

        self.frame_12 = QFrame(self.sensor_page)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_12)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.sensor_tableWidget = QTableWidget(self.frame_12)
        if (self.sensor_tableWidget.columnCount() < 6):
            self.sensor_tableWidget.setColumnCount(6)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.sensor_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.sensor_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.sensor_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.sensor_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.sensor_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.sensor_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        self.sensor_tableWidget.setObjectName(u"sensor_tableWidget")
        self.sensor_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.sensor_tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_4.addWidget(self.sensor_tableWidget)


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
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 926, 819))
        self.verticalLayout_15 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_15.setSpacing(5)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 10, 0, 50)
        self.frame_14 = QFrame(self.scrollAreaWidgetContents)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.frame_14)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 20)
        self.label_46 = QLabel(self.frame_14)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font4)
        self.label_46.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_16.addWidget(self.label_46)

        self.net_stats_tableWidget = QTableWidget(self.frame_14)
        if (self.net_stats_tableWidget.columnCount() < 5):
            self.net_stats_tableWidget.setColumnCount(5)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.net_stats_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.net_stats_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.net_stats_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.net_stats_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.net_stats_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem24)
        self.net_stats_tableWidget.setObjectName(u"net_stats_tableWidget")
        self.net_stats_tableWidget.setMinimumSize(QSize(0, 150))
        self.net_stats_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.net_stats_tableWidget.setMidLineWidth(-3)
        self.net_stats_tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_16.addWidget(self.net_stats_tableWidget)


        self.verticalLayout_15.addWidget(self.frame_14)

        self.frame_15 = QFrame(self.scrollAreaWidgetContents)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_15)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 20)
        self.label_47 = QLabel(self.frame_15)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font4)
        self.label_47.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_17.addWidget(self.label_47)

        self.net_io_tableWidget = QTableWidget(self.frame_15)
        if (self.net_io_tableWidget.columnCount() < 9):
            self.net_io_tableWidget.setColumnCount(9)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.net_io_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem33)
        self.net_io_tableWidget.setObjectName(u"net_io_tableWidget")
        self.net_io_tableWidget.setMinimumSize(QSize(0, 150))
        self.net_io_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.net_io_tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_17.addWidget(self.net_io_tableWidget)


        self.verticalLayout_15.addWidget(self.frame_15)

        self.frame_16 = QFrame(self.scrollAreaWidgetContents)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.frame_16)
        self.verticalLayout_18.setSpacing(0)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.verticalLayout_18.setContentsMargins(0, 0, 0, 20)
        self.label_48 = QLabel(self.frame_16)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setFont(font4)
        self.label_48.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_18.addWidget(self.label_48)

        self.net_addresses_tableWidget = QTableWidget(self.frame_16)
        if (self.net_addresses_tableWidget.columnCount() < 5):
            self.net_addresses_tableWidget.setColumnCount(5)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.net_addresses_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.net_addresses_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.net_addresses_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.net_addresses_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.net_addresses_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem38)
        self.net_addresses_tableWidget.setObjectName(u"net_addresses_tableWidget")
        self.net_addresses_tableWidget.setMinimumSize(QSize(0, 150))
        self.net_addresses_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.net_addresses_tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_18.addWidget(self.net_addresses_tableWidget)


        self.verticalLayout_15.addWidget(self.frame_16)

        self.frame_17 = QFrame(self.scrollAreaWidgetContents)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_17)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 20)
        self.label_49 = QLabel(self.frame_17)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font4)
        self.label_49.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.verticalLayout_19.addWidget(self.label_49)

        self.net_connections_tableWidget = QTableWidget(self.frame_17)
        if (self.net_connections_tableWidget.columnCount() < 7):
            self.net_connections_tableWidget.setColumnCount(7)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.net_connections_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem45)
        self.net_connections_tableWidget.setObjectName(u"net_connections_tableWidget")
        self.net_connections_tableWidget.setMinimumSize(QSize(0, 150))
        self.net_connections_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.net_connections_tableWidget.horizontalHeader().setDefaultSectionSize(200)

        self.verticalLayout_19.addWidget(self.net_connections_tableWidget)


        self.verticalLayout_15.addWidget(self.frame_17)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout_14.addWidget(self.scrollArea)


        self.verticalLayout_13.addWidget(self.frame_13)

        self.stackedWidget.addWidget(self.network_page)
        self.activity_page = QWidget()
        self.activity_page.setObjectName(u"activity_page")
        self.verticalLayout_27 = QVBoxLayout(self.activity_page)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.frame_10 = QFrame(self.activity_page)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_13 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_13.setSpacing(0)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.frame_30 = QFrame(self.frame_10)
        self.frame_30.setObjectName(u"frame_30")
        sizePolicy7.setHeightForWidth(self.frame_30.sizePolicy().hasHeightForWidth())
        self.frame_30.setSizePolicy(sizePolicy7)
        self.frame_30.setFrameShape(QFrame.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Raised)
        self.label_16 = QLabel(self.frame_30)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(9, 9, 111, 21))
        self.label_16.setFont(font3)
        self.label_16.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_13.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_10)
        self.frame_31.setObjectName(u"frame_31")
        sizePolicy7.setHeightForWidth(self.frame_31.sizePolicy().hasHeightForWidth())
        self.frame_31.setSizePolicy(sizePolicy7)
        self.frame_31.setFrameShape(QFrame.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_31)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.activity_search = QLineEdit(self.frame_31)
        self.activity_search.setObjectName(u"activity_search")
        self.activity_search.setEnabled(True)
        sizePolicy5.setHeightForWidth(self.activity_search.sizePolicy().hasHeightForWidth())
        self.activity_search.setSizePolicy(sizePolicy5)
        self.activity_search.setMinimumSize(QSize(200, 30))
        self.activity_search.setStyleSheet(u"background-color: rgb(30, 30, 30);\n"
"color: rgb(255, 255, 255);")

        self.horizontalLayout_14.addWidget(self.activity_search)

        self.activity_search_button = QPushButton(self.frame_31)
        self.activity_search_button.setObjectName(u"activity_search_button")
        sizePolicy1.setHeightForWidth(self.activity_search_button.sizePolicy().hasHeightForWidth())
        self.activity_search_button.setSizePolicy(sizePolicy1)
        self.activity_search_button.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon15 = QIcon()
        icon15.addFile(u":/images/ui_images/search_white_36dp.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.activity_search_button.setIcon(icon15)
        self.activity_search_button.setIconSize(QSize(26, 26))

        self.horizontalLayout_14.addWidget(self.activity_search_button)


        self.horizontalLayout_13.addWidget(self.frame_31, 0, Qt.AlignRight)


        self.verticalLayout_27.addWidget(self.frame_10)

        self.frame_32 = QFrame(self.activity_page)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_22 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.activities_tableWidget = QTableWidget(self.frame_32)
        if (self.activities_tableWidget.columnCount() < 8):
            self.activities_tableWidget.setColumnCount(8)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.activities_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem53)
        self.activities_tableWidget.setObjectName(u"activities_tableWidget")
        self.activities_tableWidget.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.activities_tableWidget.horizontalHeader().setDefaultSectionSize(150)

        self.horizontalLayout_22.addWidget(self.activities_tableWidget)


        self.verticalLayout_27.addWidget(self.frame_32)

        self.frame_29 = QFrame(self.activity_page)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.pushButton_3 = QPushButton(self.frame_29)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setFont(font7)
        self.pushButton_3.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.frame_29)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setFont(font7)
        self.pushButton_4.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.frame_29)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setFont(font7)
        self.pushButton_5.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.frame_29)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setFont(font7)
        self.pushButton_6.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_21.addWidget(self.pushButton_6)


        self.verticalLayout_27.addWidget(self.frame_29)

        self.stackedWidget.addWidget(self.activity_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_3.addWidget(self.stackedWidget)


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
        font11 = QFont()
        font11.setFamilies([u"Dosis"])
        font11.setPointSize(10)
        font11.setBold(False)
        self.label.setFont(font11)
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

        self.stackedWidget.setCurrentIndex(1)


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
        self.activity_button.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Aktivit\u00e4ten", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Internet", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Status-Verbindung:", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Status-Linked:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Externe IP-V4:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Externe IP-V6:", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Verbunden seit:", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Ger\u00e4t onlien seit:", None))
        self.is_connected_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.is_linked_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.external_ip_v4_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.external_ip_v6_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.connection_uptime_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.device_uptime_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.internet_button_4.setText("")
        self.current_download_2.setText(QCoreApplication.translate("MainWindow", u"1,1 MB/s", None))
        self.max_download_2.setText(QCoreApplication.translate("MainWindow", u"52,4 MB", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Insgesamt erhalten:", None))
        self.total_bytes_received_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.internet_button_5.setText("")
        self.current_upload_2.setText(QCoreApplication.translate("MainWindow", u"1,1 MB/s", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Max:", None))
        self.max_upload_2.setText(QCoreApplication.translate("MainWindow", u"52,4 MB", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Insgesamt gesendet:", None))
        self.total_bytes_sent_2.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"W-Lan", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"SSID:", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Anzahl verbundene Ger\u00e4te:", None))
        self.ssid.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.connected_devices.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Telefonie", None))
        ___qtablewidgetitem = self.call_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Typ", None));
        ___qtablewidgetitem1 = self.call_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nummer", None));
        ___qtablewidgetitem2 = self.call_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Datum", None));
        ___qtablewidgetitem3 = self.call_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Dauer", None));
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"CPU & Ram", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"CPU Count", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"CPU %", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"CPU Main Core", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.cpu_percent_large.setText(QCoreApplication.translate("MainWindow", u"99%", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Gesamter Ram", None))
        self.label1.setText(QCoreApplication.translate("MainWindow", u"Verf\u00fcgbarer Ram", None))
        self.label2.setText(QCoreApplication.translate("MainWindow", u"Verwendeter Ram", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Freier Ram", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Ram-Nutzung", None))
        self.ram_usage.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"RAM", None))
        self.ram_percent_large.setText(QCoreApplication.translate("MainWindow", u"99%", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"System Information", None))
        self.system_system.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_release.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"Plattform", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"System Datum", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_platform.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_date.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Prozessor", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Maschine", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"System Zeit", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Speicher", None))
        ___qtablewidgetitem4 = self.storage_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Ger\u00e4t", None));
        ___qtablewidgetitem5 = self.storage_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Mount Point", None));
        ___qtablewidgetitem6 = self.storage_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"FS Typ", None));
        ___qtablewidgetitem7 = self.storage_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"OPTS", None));
        ___qtablewidgetitem8 = self.storage_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Max Datei", None));
        ___qtablewidgetitem9 = self.storage_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Max Pfad", None));
        ___qtablewidgetitem10 = self.storage_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Gesamter Speicher", None));
        ___qtablewidgetitem11 = self.storage_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Verwendeter Speicher", None));
        ___qtablewidgetitem12 = self.storage_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Freier Speicher", None));
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Sensoren", None))
        ___qtablewidgetitem13 = self.sensor_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Sensor", None));
        ___qtablewidgetitem14 = self.sensor_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Label", None));
        ___qtablewidgetitem15 = self.sensor_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Aktuell", None));
        ___qtablewidgetitem16 = self.sensor_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"H\u00f6chste", None));
        ___qtablewidgetitem17 = self.sensor_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Kritisch", None));
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Netzwerke", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        ___qtablewidgetitem18 = self.net_stats_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"ISUP", None));
        ___qtablewidgetitem19 = self.net_stats_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Duplex", None));
        ___qtablewidgetitem20 = self.net_stats_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Geschwindigkeit", None));
        ___qtablewidgetitem21 = self.net_stats_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"MTU", None));
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Netzwerk I/O Z\u00e4hler", None))
        ___qtablewidgetitem22 = self.net_io_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"I/O", None));
        ___qtablewidgetitem23 = self.net_io_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Bytes gesendet", None));
        ___qtablewidgetitem24 = self.net_io_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Bytes empfangen", None));
        ___qtablewidgetitem25 = self.net_io_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Packete gesendet", None));
        ___qtablewidgetitem26 = self.net_io_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Packete empfangen", None));
        ___qtablewidgetitem27 = self.net_io_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Err In", None));
        ___qtablewidgetitem28 = self.net_io_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Err Out", None));
        ___qtablewidgetitem29 = self.net_io_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Drop In", None));
        ___qtablewidgetitem30 = self.net_io_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Drop Out", None));
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Netzwerk Adressen", None))
        ___qtablewidgetitem31 = self.net_addresses_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Familie", None));
        ___qtablewidgetitem32 = self.net_addresses_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Netmask", None));
        ___qtablewidgetitem33 = self.net_addresses_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Broadcast", None));
        ___qtablewidgetitem34 = self.net_addresses_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"PTP", None));
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Netzwerk Verbindungen", None))
        ___qtablewidgetitem35 = self.net_connections_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"FD", None));
        ___qtablewidgetitem36 = self.net_connections_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"New Column", None));
        ___qtablewidgetitem37 = self.net_connections_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Familie", None));
        ___qtablewidgetitem38 = self.net_connections_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Familie", None));
        ___qtablewidgetitem39 = self.net_connections_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"RADDR", None));
        ___qtablewidgetitem40 = self.net_connections_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Tatus", None));
        ___qtablewidgetitem41 = self.net_connections_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"PID", None));
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Aktivit\u00e4ten", None))
        self.activity_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Suchen", None))
        self.activity_search_button.setText("")
        ___qtablewidgetitem42 = self.activities_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Prozess ID", None));
        ___qtablewidgetitem43 = self.activities_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Prozess Name", None));
        ___qtablewidgetitem44 = self.activities_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Prozess Status", None));
        ___qtablewidgetitem45 = self.activities_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Gestartet", None));
        ___qtablewidgetitem46 = self.activities_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Unterbrechen", None));
        ___qtablewidgetitem47 = self.activities_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Fortsetzen", None));
        ___qtablewidgetitem48 = self.activities_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Beenden", None));
        ___qtablewidgetitem49 = self.activities_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Killen", None));
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Unterbrechen", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"Fortsetzen", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"Beenden", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Killen", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Version 0.1 | Copyright Marcel Peplies", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"PushButton", None))
    # retranslateUi

