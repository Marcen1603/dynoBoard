import datetime
import platform
import shutil
import string
import sys
import threading
import psutil

from ping3 import ping
from PySide6 import QtGui, QtCore
from PySide6.QtCore import QPropertyAnimation, QSettings
from PySide6.QtGui import QColor, Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QGraphicsDropShadowEffect, QSizeGrip, QPushButton, \
    QTableWidgetItem, QProgressBar, QLineEdit
from fritzconnection import FritzConnection
from fritzconnection.lib.fritzcall import FritzCall
from fritzconnection.lib.fritzstatus import FritzStatus
from fritzconnection.lib.fritzwlan import FritzWLAN

from pages.setup import setup
from ui.ui_dynoDash import Ui_MainWindow

# Import Qt-Material
import qt_material

platforms = {
    'linux': 'Linux',
    'linux1': 'Linux',
    'linux2': 'Linux',
    'darwin': 'OS X',
    'win32': 'Windows'
}

correct_internet_password = True


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        qt_material.apply_stylesheet(app, theme="dark_cyan.xml")

        self = setup(self)

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

        self.show()

        self.overview()
        self.internet()
        self.call()
        self.cpu_ram()
        self.system_info()
        self.processes()
        self.storage()
        self.sensors()
        self.networks()
        self.load_internet_password()

        self.update()

        def looper():
            # i as interval in seconds
            threading.Timer(1, looper).start()
            # put your action here
            self.cpu_ram()
            self.internet()
            self.overview()

        # to start
        looper()

    def clear_internet_password(self):
        self.ui.internet_password_display.clear()

    def load_internet_password(self):
        settings = QtCore.QSettings("DynoDashboard", "Settings")
        self.ui.internet_password_display.setText(settings.value('internet_password'))

    def save_internet_password(self):
        global correct_internet_password
        settings = QtCore.QSettings("DynoDashboard", "Settings")
        settings.setValue("internet_password", self.ui.internet_password.text())
        self.ui.internet_password_display.setText(self.ui.internet_password.text())
        self.ui.internet_password.clear()
        correct_internet_password = True

    def show_hide_internet_password(self):
        if self.ui.internet_password_display.echoMode() == QLineEdit.EchoMode.Password:
            self.ui.internet_password_display.setEchoMode(QLineEdit.EchoMode.Normal)
        else:
            self.ui.internet_password_display.setEchoMode(QLineEdit.EchoMode.Password)

    def overview(self):

        # System
        self.ui.overview_system_system.setText(str(platform.system()) + " " + str(platform.release()))
        self.ui.overview_system_version.setText(str(platform.version()))

        time = datetime.datetime.now().strftime("%H:%M:%S")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.overview_system_date_time.setText(date + " | " + time)

        # CPU & RAM
        self.ui.overview_cpu.setText(str(psutil.cpu_percent()) + " %")
        self.ui.overview_ram.setText(str(psutil.virtual_memory()[2]) + " %")

        # Internet
        if self.ui.internet_password_display.text() != "":
            fc = FritzConnection(address='192.168.178.1', password=self.ui.internet_password_display.text())
            fstatus = FritzStatus(fc)
            self.ui.overview_current_download.setText(str(fstatus.str_transmission_rate[1]))
            self.ui.overview_current_upload.setText(str(fstatus.str_transmission_rate[0]))
            self.ui.overview_google_ping.setText(str(int(ping('www.google.de') * 1000)) + " ms")
            self.ui.overview_telekom_ping.setText(str(int(ping('t-online.de') * 1000)) + " ms")

    def internet(self):
        global correct_internet_password

        if correct_internet_password is True:
            try:
                fc = FritzConnection(address='192.168.178.1', password=self.ui.internet_password_display.text())
                fstatus = FritzStatus(fc)
                fwlan = FritzWLAN(fc)

                # Status
                total_bytes_received = round((fstatus.bytes_received / 1024 / 1024 / 1024), 2)
                self.ui.total_bytes_received_2.setText(str(total_bytes_received) + " GB")

                total_bytes_sent = round((fstatus.bytes_sent / 1024 / 1024 / 1024), 2)
                self.ui.total_bytes_sent_2.setText(str(total_bytes_sent) + " GB")

                connection_uptime = self.to_day_min_sec(fstatus.connection_uptime)
                self.ui.connection_uptime_2.setText(str(connection_uptime))

                device_uptime = self.to_day_min_sec(fstatus.device_uptime)
                self.ui.device_uptime_2.setText(str(device_uptime))

                external_ip_v4 = fstatus.external_ip
                self.ui.external_ip_v4_2.setText(str(external_ip_v4))

                external_ip_v6 = fstatus.external_ipv6
                self.ui.external_ip_v6_2.setText(str(external_ip_v6))

                is_connected = fstatus.is_connected
                self.ui.is_connected_2.setText(str(is_connected))

                is_linked = fstatus.is_linked
                self.ui.is_linked_2.setText(str(is_linked))

                max_upload = fstatus.str_max_bit_rate[0]
                self.ui.max_upload_2.setText(str(max_upload))

                max_download = fstatus.str_max_bit_rate[1]
                self.ui.max_download_2.setText(str(max_download))

                current_upload = fstatus.str_transmission_rate[0]
                self.ui.current_upload_2.setText(str(current_upload))

                current_download = fstatus.str_transmission_rate[1]
                self.ui.current_download_2.setText(str(current_download))

                # W-Lan
                ssid = fwlan.ssid
                self.ui.ssid.setText(str(ssid))

                connected_devices = fwlan.host_number
                self.ui.connected_devices.setText(str(connected_devices))

                self.ui.ping_google.setText(str(int(ping('www.google.de') * 1000)) + " ms")
                self.ui.ping_telekom.setText(str(int(ping('t-online.de') * 1000)) + " ms")

            except Exception as e:
                correct_internet_password = False

    def call(self):

        call_types = {
            "0": 'ALL_CALL_TYPES',
            "1": 'Eingehend',
            "2": 'Verpasst',
            "3": 'Ausgehend',
            "9": 'Aktiv eingehend',
            "10": 'Abgelehnt',
            "11": 'Aktib ausgehend',
        }

        if self.ui.internet_password_display.text() != "":
            fc = FritzConnection(address='192.168.178.1', password="jogger2285")
            fcall = FritzCall(fc)

            last_10_call = fcall.get_calls(calltype=0, update=True, num=10, days=None)

            for call in last_10_call:
                call_entry = str(call).split()
                call_type = call_types[call_entry[0]]
                call_number = call_entry[1]
                call_date = call_entry[2] + " - " + call_entry[3]
                call_duration = call_entry[4]

                rowPosition = self.ui.call_tableWidget.rowCount()
                self.ui.call_tableWidget.insertRow(rowPosition)

                self.create_table_widget(rowPosition, 0, str(call_type), "call_tableWidget")
                self.create_table_widget(rowPosition, 1, str(call_number), "call_tableWidget")
                self.create_table_widget(rowPosition, 2, str(call_date), "call_tableWidget")
                self.create_table_widget(rowPosition, 3, str(call_duration), "call_tableWidget")

    def to_day_min_sec(self, sec):
        seconds = sec
        seconds_in_day = 60 * 60 * 24
        seconds_in_hour = 60 * 60
        seconds_in_minute = 60

        days = seconds // seconds_in_day
        hours = (seconds - (days * seconds_in_day)) // seconds_in_hour
        minutes = (seconds - (days * seconds_in_day) - (hours * seconds_in_hour)) // seconds_in_minute

        return str(days) + " Tage " + str(hours) + " Stunden " + str(minutes) + " Minuten"

    def sensors(self):
        if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
            for x in psutil.sensors_temperatures():
                for y in psutil.sensors_temperatures()[x]:
                    rowPosition = self.ui.sensor_tableWidget.rowCount()
                    self.ui.sensor_tableWidget.insertRow(rowPosition)

                    self.create_table_widget(rowPosition, 0, x, "sensor_tableWidget")
                    self.create_table_widget(rowPosition, 1, y.label, "sensor_tableWidget")
                    self.create_table_widget(rowPosition, 2, str(y.current), "sensor_tableWidget")
                    self.create_table_widget(rowPosition, 3, str(y.high), "sensor_tableWidget")
                    self.create_table_widget(rowPosition, 4, str(y.critical), "sensor_tableWidget")

                    temp_per = (y.current / y.high) * 100

                    progressBar = QProgressBar(self.ui.sensor_tableWidget)
                    progressBar.setObjectName(u"progressBar")
                    progressBar.setValue(temp_per)
                    self.ui.sensor_tableWidget.setCellWidget(rowPosition, 5, progressBar)
        else:
            global platforms

            rowPosition = self.ui.sensor_tableWidget.rowCount()
            self.ui.sensor_tableWidget.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, "Funktion nicht verfügbar auf " + platforms[sys.platform],
                                     "sensor_tableWidget")
            self.create_table_widget(rowPosition, 1, "N/A", "sensor_tableWidget")
            self.create_table_widget(rowPosition, 2, "N/A", "sensor_tableWidget")
            self.create_table_widget(rowPosition, 3, "N/A", "sensor_tableWidget")
            self.create_table_widget(rowPosition, 4, "N/A", "sensor_tableWidget")

    def networks(self):
        # Net stats
        for x in psutil.net_if_stats():
            z = psutil.net_if_stats()

            rowPosition = self.ui.net_stats_tableWidget.rowCount()
            self.ui.net_stats_tableWidget.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_stats_tableWidget")
            self.create_table_widget(rowPosition, 1, str(z[x].isup), "net_stats_tableWidget")
            self.create_table_widget(rowPosition, 2, str(z[x].duplex), "net_stats_tableWidget")
            self.create_table_widget(rowPosition, 3, str(z[x].speed), "net_stats_tableWidget")
            self.create_table_widget(rowPosition, 4, str(z[x].mtu), "net_stats_tableWidget")

        # Net io counter
        for x in psutil.net_io_counters(pernic=True):
            z = psutil.net_io_counters(pernic=True)

            rowPosition = self.ui.net_io_tableWidget.rowCount()
            self.ui.net_io_tableWidget.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x, "net_io_tableWidget")
            self.create_table_widget(rowPosition, 1, str(z[x].bytes_sent), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 2, str(z[x].bytes_recv), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 3, str(z[x].packets_sent), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 4, str(z[x].packets_recv), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 5, str(z[x].errin), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 6, str(z[x].errout), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 7, str(z[x].dropin), "net_io_tableWidget")
            self.create_table_widget(rowPosition, 8, str(z[x].dropout), "net_io_tableWidget")

        # Net addresses
        for x in psutil.net_if_addrs():
            z = psutil.net_if_addrs()

            for y in z[x]:
                rowPosition = self.ui.net_addresses_tableWidget.rowCount()
                self.ui.net_addresses_tableWidget.insertRow(rowPosition)

                self.create_table_widget(rowPosition, 0, str(x), "net_addresses_tableWidget")
                self.create_table_widget(rowPosition, 1, str(y.family), "net_addresses_tableWidget")
                self.create_table_widget(rowPosition, 2, str(y.address), "net_addresses_tableWidget")
                self.create_table_widget(rowPosition, 3, str(y.netmask), "net_addresses_tableWidget")
                self.create_table_widget(rowPosition, 4, str(y.broadcast), "net_addresses_tableWidget")
                self.create_table_widget(rowPosition, 4, str(y.ptp), "net_addresses_tableWidget")

        # Net connections
        for x in psutil.net_connections():
            z = psutil.net_connections()

            rowPosition = self.ui.net_connections_tableWidget.rowCount()
            self.ui.net_connections_tableWidget.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, str(x.fd), "net_connections_tableWidget")
            self.create_table_widget(rowPosition, 1, str(x.family), "net_connections_tableWidget")
            self.create_table_widget(rowPosition, 2, str(x.type), "net_connections_tableWidget")
            self.create_table_widget(rowPosition, 3, str(x.laddr), "net_connections_tableWidget")
            self.create_table_widget(rowPosition, 4, str(x.raddr), "net_connections_tableWidget")
            self.create_table_widget(rowPosition, 5, str(x.status), "net_connections_tableWidget")
            self.create_table_widget(rowPosition, 6, str(x.pid), "net_connections_tableWidget")

    def storage(self):
        global platforms
        storage_device = psutil.disk_partitions(all=False)
        z = 0
        for x in storage_device:
            rowPosition = self.ui.storage_tableWidget.rowCount()
            self.ui.storage_tableWidget.insertRow(rowPosition)

            self.create_table_widget(rowPosition, 0, x.device, "storage_tableWidget")
            self.create_table_widget(rowPosition, 1, x.mountpoint, "storage_tableWidget")
            self.create_table_widget(rowPosition, 2, x.fstype, "storage_tableWidget")
            self.create_table_widget(rowPosition, 3, x.opts, "storage_tableWidget")

            # if sys.platform == 'linux' or sys.platform == 'linux1' or sys.platform == 'linux2':
            self.create_table_widget(rowPosition, 4, str(x.maxfile), "storage_tableWidget")
            self.create_table_widget(rowPosition, 5, str(x.maxpath), "storage_tableWidget")
            # else:
            #     self.create_table_widget(rowPosition, 4, "Funktion nicht verfügbar auf " + platforms[sys.platform], "storage_tableWidget")
            #     self.create_table_widget(rowPosition, 5, "Funktion nicht verfügbar auf " + platforms[sys.platform], "storage_tableWidget")

            disk_usage = shutil.disk_usage(x.mountpoint)

            self.create_table_widget(rowPosition, 6, str(round((disk_usage.total / (1024 * 1024 * 1024)), 2)) + " GB",
                                     "storage_tableWidget")
            self.create_table_widget(rowPosition, 7, str(round((disk_usage.used / (1024 * 1024 * 1024)), 2)) + " GB",
                                     "storage_tableWidget")
            self.create_table_widget(rowPosition, 8, str(round((disk_usage.free / (1024 * 1024 * 1024)), 2)) + " GB",
                                     "storage_tableWidget")

            full_disk = (disk_usage.used / disk_usage.total) * 100
            progressBar = QProgressBar(self.ui.storage_tableWidget)
            progressBar.setObjectName(u"progressBar")
            progressBar.setValue(full_disk)
            self.ui.storage_tableWidget.setCellWidget(rowPosition, 9, progressBar)

    def create_table_widget(self, rowPosition, columnPosition, text, tableName):
        qtablewidgetitem = QTableWidgetItem()

        getattr(self.ui, tableName).setItem(rowPosition, columnPosition, qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui, tableName).item(rowPosition, columnPosition)

        qtablewidgetitem.setText(text)

    def processes(self):
        for x in psutil.pids():
            rowPosition = self.ui.activities_tableWidget.rowCount()
            self.ui.activities_tableWidget.insertRow(rowPosition)

            try:
                process = psutil.Process(x)

                self.create_table_widget(rowPosition, 0, str(process.pid), "activities_tableWidget")
                self.create_table_widget(rowPosition, 1, process.name(), "activities_tableWidget")
                self.create_table_widget(rowPosition, 2, process.status(), "activities_tableWidget")
                self.create_table_widget(rowPosition, 3,
                                         str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime(
                                             '%Y-%m-%d %H:%M:%S')), "activities_tableWidget")

                suspend_btn = QPushButton(self.ui.activities_tableWidget)
                suspend_btn.setText('Unterbrechen')
                suspend_btn.setStyleSheet("color: brown")
                self.ui.activities_tableWidget.setCellWidget(rowPosition, 4, suspend_btn)

                resume_btn = QPushButton(self.ui.activities_tableWidget)
                resume_btn.setText('Fortsetzen')
                resume_btn.setStyleSheet("color: green")
                self.ui.activities_tableWidget.setCellWidget(rowPosition, 5, resume_btn)

                terminate_btn = QPushButton(self.ui.activities_tableWidget)
                terminate_btn.setText('Beenden')
                terminate_btn.setStyleSheet("color: orange")
                self.ui.activities_tableWidget.setCellWidget(rowPosition, 6, terminate_btn)

                kill_btn = QPushButton(self.ui.activities_tableWidget)
                kill_btn.setText('Killen')
                kill_btn.setStyleSheet("color: red")
                self.ui.activities_tableWidget.setCellWidget(rowPosition, 7, kill_btn)

            except Exception as e:
                print(e)

        self.ui.activity_search.textChanged.connect(self.findName)

    def findName(self):
        name = self.ui.activity_search.text().lower()
        for row in range(self.ui.activities_tableWidget.rowCount()):
            item = self.ui.activities_tableWidget.item(row, 1)
            self.ui.activities_tableWidget.setRowHidden(row, name not in item.text().lower())

    def system_info(self):
        time = datetime.datetime.now().strftime("%H:%M:%S")
        self.ui.system_time.setText(str(time))
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.system_date.setText(str(date))

        self.ui.system_machine.setText(platform.machine())
        self.ui.system_version.setText(platform.version())
        self.ui.system_platform.setText(platform.platform())
        self.ui.system_system.setText(platform.system())
        self.ui.system_processor.setText(platform.processor())
        self.ui.system_release.setText(platform.release())

    def cpu_ram(self):

        core = psutil.cpu_count()
        self.ui.cpu_count.setText(str(core))

        cpuPer = psutil.cpu_percent()
        self.ui.cpu_per.setText(str(cpuPer) + ' %')
        self.ui.cpu_percent_large.setText(str(cpuPer) + '%')

        cpuMainCore = psutil.cpu_count(logical=False)
        self.ui.cpu_main_core.setText(str(cpuMainCore))

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

        self.ui.ram_usage.setText(str(psutil.virtual_memory()[2]) + " %")
        self.ui.ram_percent_large.setText(str(psutil.virtual_memory()[2]) + "%")

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
