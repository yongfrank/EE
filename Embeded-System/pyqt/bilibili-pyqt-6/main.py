'''
Author: Frank Chu
Date: 2022-12-11 15:08:51
LastEditors: Frank Chu
LastEditTime: 2022-12-11 16:01:31
FilePath: /EE/Embeded-System/pyqt/bilibili-pyqt-6/main.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''
from threading import Thread
from PySide6.QtWidgets import QApplication, QMainWindow
# PySide6-uic demo.ui -o ui_demo.py
from ui_demo import Ui_MainWindow

import time
from Signal import my_signal

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.bind()
    
    def bind(self):
        self.ui.pushButton.clicked.connect(self.handle_click)
        my_signal.setProgressBar.connect(self.set_progress_bar)
        
        my_signal.setResult.connect(self.set_result)
    
    def set_result(self, result: str):
        self.ui.result.setText(result)
        
    def set_progress_bar(self, progress: int):
        self.ui.progressBar.setValue(progress)
        
    def handle_click(self):
        def innerFunction():
            lhsInputValue = self.ui.lhsInputA.value()
            rhsInputValue = self.ui.rhsInputB.value()
            
            time_cost = self.ui.timeCost.value()
            
            for index, _ in enumerate(range(time_cost)):
                progress = index * 100 // time_cost
                # self.ui.progressBar.setValue(progress)
                
                my_signal.setProgressBar.emit(progress)
                time.sleep(1)
            
            my_signal.setProgressBar.emit(100)
            
            result = str(lhsInputValue + rhsInputValue)
            my_signal.setResult.emit(result)
            
        task = Thread(target=innerFunction)
        task.start()
        
if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()