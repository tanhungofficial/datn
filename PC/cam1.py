from PyQt5.QtCore import QThread, pyqtSignal
import  cv2
class MySerialClass(QThread):
    frame = pyqtSignal(list)
    def __init__(self, parent = None):
        cap = cv2.VideoCapture(0)

    def run(self):
        while True:
            self.
    def sendSerial(self):
        self.serialPort.write(b'A')
