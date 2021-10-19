from PySide6 import QtGui
from PySide6.QtGui import Qt, QColor
from PySide6.QtWidgets import QGraphicsDropShadowEffect, QSizeGrip


def setup(self):
    self.setWindowFlags(Qt.FramelessWindowHint)
    self.setAttribute(Qt.WA_TranslucentBackground)

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
    self.ui.system_info_button.clicked.connect(
        lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.system_info_page))
    self.ui.storage_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage_page))
    self.ui.sensor_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensor_page))
    self.ui.network_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network_page))
    self.ui.settings_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))
    self.ui.activity_button.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activity_page))

    self.ui.show_internet_password.clicked.connect(lambda: self.show_hide_internet_password())
    self.ui.save_internet_password.clicked.connect(lambda: self.save_internet_password())
    self.ui.clear_internet_password.clicked.connect(lambda: self.clear_internet_password())

    QSizeGrip(self.ui.size_grip)
    return self