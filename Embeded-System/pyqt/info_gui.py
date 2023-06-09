'''
Author: Frank Chu
Date: 2022-12-11 15:08:51
LastEditors: Frank Chu
LastEditTime: 2022-12-14 17:57:45
FilePath: /EE/Embeded-System/pyqt/info_gui.py
Description: 【Python图形界面 15分钟快速入门PySide/PyQt】 
https://www.bilibili.com/video/BV18F411W7y2/?share_source=copy_web&vd_source=bf4952280cde801b178268abc99a7047

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic demo.ui -o ui_demo.py
from ui_info_gui_design import Ui_MainWindow
from info_client import connectAndPrint, SendInfo
from info_mysignal import my_signal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind()
    
    def bind(self):
        # self.ui.hostnameLineEdit.setText("raspberrypi.local")
        self.ui.hostnameLineEdit.setText("frank-parallels-vm.local")
        # self.ui.hostnameLineEdit.setText("10.203.1.120")

        my_signal.setEditLine.connect(self.set_line_edit)
        self.ui.getInfoPushButton.clicked.connect(self.handle_click)
        def inner_thread():
            self.connectToRemote()
        task = Thread(target=inner_thread)
        task.start()
    
    def connectToRemote(self):
        try:
            host = self.ui.hostnameLineEdit.text()
            remote_system_info = connectAndPrint(host_to_connect=host)
            self.set_line_edit(remote_system_info)
        except:
            print("Please input a valid hostname")
    
    def set_line_edit(self, info: SendInfo):
        self.ui.hostnameLineEdit.setText(info.host_name)
        self.ui.ipAddressLineEdit.setText(info.ip_address)
        self.ui.processorLineEdit.setText(info.cpu_info)
        self.ui.osLineEdit.setText(info.platform_info)
        
    
    def handle_click(self):
        def side_thread():
            self.connectToRemote()
        task = Thread(target=side_thread)
        task.start()
        
    
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()
    