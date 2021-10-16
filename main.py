import sys
import psutil
import PySide2extn

from PySide6 import QtGui, QtCore
from PySide6.QtCore import QPropertyAnimation
from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip, QPushButton

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
        self.ui.open_close_side_bar_btn.clicked.connect(lambda: self.slideLeftMenu())

        for w in self.ui.menu_frame.findChildren(QPushButton):
            w.clicked.connect(self.applyButtonStyle)

        self.cpu_ram()

        self.show()

    def cpu_ram(self):

        core = psutil.cpu_count()
        self.ui.cpu_count.setText(str(core))

        cpuPer = psutil.cpu_percent()
        self.ui.cpu_per.setText(str(cpuPer) + ' %')

        cpuMainCore = psutil.cpu_count(logical=False)
        self.ui.cpu_main_core.setText(str(cpuMainCore))

        self.ui.cpu_progress_bar.setRange(0, 100)
        self.ui.cpu_progress_bar.setValue(int(cpuPer))
        self.ui.label_cpu_progress_bar.setText(str(cpuPer))

        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0] * totalRam
        totalRam = totalRam / (1024 * 1024 * 1024)
        self.ui.total_ram.setText(str("{:.4f}".format(totalRam) + ' GB'))

        availRam = 1.0
        availRam = psutil.virtual_memory()[1] * availRam
        availRam = availRam / (1024 * 1024 * 1024)
        self.ui.available_ram.setText(str("{:.4f}".format(availRam) + ' GB'))

        ramUsed = 1.0
        ramUsed = psutil.virtual_memory()[3] * ramUsed
        ramUsed = ramUsed / (1024 * 1024 * 1024)
        self.ui.used_ram.setText(str("{:.4f}".format(ramUsed) + ' GB'))

        ramFree = 1.0
        ramFree = psutil.virtual_memory()[4] * ramFree
        ramFree = ramFree / (1024 * 1024 * 1024)
        self.ui.free_ram.setText(str("{:.4f}".format(ramFree) + ' GB'))

        ramUsage = str(psutil.virtual_memory()[2]) + '%'
        self.ui.ram_usage.setText(str("{:.4f}").format(totalRam) + ' GB')

        self.ui.ram_progress_bar.setRange(0, 100)
        self.ui.ram_progress_bar.setValue(int(psutil.virtual_memory()[2]))
        self.ui.label_ram_progress_bar.setText(str(psutil.virtual_memory()[2]))

    def secs2hours(self, secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d (H:M:S)" % (hh, mm, ss)

    def applyButtonStyle(self):
        for w in self.ui.menu_frame.findChildren(QPushButton):
            if w.objectName() != self.sender().objectName():
                w.setStyleSheet("border-bottom: none;")

        self.sender().setStyleSheet("border-bottom: 2px solid")
        return

    def slideLeftMenu(self):
        width = self.ui.left_menu_cont_frame.width()

        # If minimized
        if width == 55:
            # Expand menu
            newWidth = 250
        # If maximized
        else:
            # Restore menu
            newWidth = 55

        # Animate the transition
        self.animation = QPropertyAnimation(self.ui.left_menu_cont_frame, b"minimumWidth")
        self.animation.setDuration(250)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()

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
