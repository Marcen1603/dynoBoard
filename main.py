import sys

from PySide6 import *
from PySide6 import QtGui
from PySide6.QtCore import Qt
from PySide6.QtGui import QColor
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip

from ui.ui_dynoDash import Ui_MainWindow

# Import Qt-Material
import qt_material


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        qt_material.apply_stylesheet(app, theme="dark_cyan.xml")

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(50)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 92, 157, 550))

        self.ui.centralwidget.setGraphicsEffect(self.shadow)

        self.setWindowIcon(QtGui.QIcon("images/logo/logo_photoshoped.png"))
        self.setWindowTitle("DynoDashboard")

        # Minimize window
        self.ui.minimize_window_button.clicked.connect(lambda: self.showMinimized())

        # Close window
        self.ui.close_winow_button.clicked.connect(lambda: self.close())

        # Restore/maximize window
        self.ui.restore_window_button.clicked.connect(lambda: self.restore_or_maximize_window())

        # Navigate to pages
        self.ui.overview_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.overview_page))
        self.ui.internet_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.internet_page))
        self.ui.computer_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.computer_page))
        self.ui.system_info_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_info_page))
        self.ui.storage_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage_page))
        self.ui.sensor_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensor_page))
        self.ui.network_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network_page))
        self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

        QSizeGrip(self.ui.size_grip)

        # Function to move the window, because the window is borderless
        def moveWindow(e):
            if not self.isMaximized():
                if e.buttons() == Qt.LeftButton:
                    self.move(self.pos() + e.globalPos() - self.clickPosition)
                    self.clickPosition = e.globalPos()
                    e.accept()

        self.ui.header_frame.mouseMoveEvent = moveWindow

        self.show()

    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    # Function to restore or maximize the window
    def restore_or_maximize_window(self):
        if self.isMaximized():
            self.showNormal()
            self.ui.restore_window_button.setIcon(QtGui.QIcon("images/ui_images/web_asset_white_36dp.svg"))
        else:
            self.showMaximized()
            self.ui.restore_window_button.setIcon(QtGui.QIcon("images/ui_images/branding_watermark_white_36dp.svg"))


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
