import serial
from PyQt5.QtCore import QThread, pyqtSignal

class MySerialClass(QThread):
    mess = pyqtSignal(str)
    def __init__(self, parent = None):
        super(MySerialClass, self).__init__(parent)
        self.serialPort = serial.Serial()
        self.serialPort.baudrate = 9600
        self.serialPort.port = 'COM3'
        self.serialPort.open()
        self.mess = 0
    def run(self):
        while True:
            mess = self.serialPort.readline()
            lst = list(str(mess))
            if len(lst) > 8:
                self.mess = int(lst[2]+lst[3] )
            else:
                self.mess = int(lst[2])
    def sendSerial(self):
        self.serialPort.write(b'A')
