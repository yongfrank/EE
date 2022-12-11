'''
Author: Frank Chu
Date: 2022-12-11 17:02:25
LastEditors: Frank Chu
LastEditTime: 2022-12-11 17:11:19
FilePath: /EE/Embeded-System/pyqt/info_mysignal.py
Description: 

Copyright (c) 2022 by Frank Chu, All Rights Reserved. 
'''

from PySide6.QtCore import QObject, Signal
from info_client import SendInfo

class MySignal(QObject):
    setEditLine = Signal(SendInfo)
    
my_signal = MySignal()