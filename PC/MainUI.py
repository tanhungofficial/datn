from PyQt5 import QtCore, QtGui, QtWidgets
import cv2
import numpy as np
from MySerial import MySerialClass

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1500, 710)
        MainWindow.setDocumentMode(False)
        self.default = True
        self.run = False
        self.gtime = 15
        self.ytime = 3
        self.ptime = 5
        self.rtime = self.gtime + self.ytime
        # Load Yolo
        self.net = cv2.dnn.readNet("yolov3.weights", "yolov3.cfg")
        self.classes = []
        with open("coco.names", "r") as f:
            self.classes = [line.strip() for line in f.readlines()]
        self.layer_names = self.net.getLayerNames()
        self.output_layers = [self.layer_names[i[0] - 1] for i in self.net.getUnconnectedOutLayers()]
        self.colors = np.random.uniform(0, 255, size=(len(self.classes), 3))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(250, 10, 120, 100))
        self.lcdNumber.setDigitCount(2)
        self.lcdNumber.setObjectName("lcdNumber")
        self.lcdNumber.setStyleSheet("QLCDNumber {color: green;}")
        self.plainTextEdit = self.nameText = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(60, 190, 161, 31))
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.plainTextEdit.setFont(QtGui.QFont('sanserif', 17))
        self.plainTextEdit.setText("0")

        self.lcdNumber_2 = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber_2.setGeometry(QtCore.QRect(1210, 10, 120, 100))
        self.lcdNumber_2.setDigitCount(2)
        self.lcdNumber_2.setObjectName("lcdNumber_2")
        self.lcdNumber_2.setStyleSheet("QLCDNumber {color: red;}")
        self.plainTextEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit_2.setGeometry(QtCore.QRect(60, 240, 161, 31))
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.plainTextEdit_2.setFont(QtGui.QFont('sanserif', 17))
        self.plainTextEdit_2.setText("0")
        self.plainTextEdit_3 = QtWidgets.QTextEdit(self.centralwidget)
        self.plainTextEdit_3.setGeometry(QtCore.QRect(60, 290, 161, 31))
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.plainTextEdit_3.setFont(QtGui.QFont('sanserif', 17))
        self.plainTextEdit_3.setText("0")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(60, 10, 90, 30))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(60, 60, 90, 30))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(60, 110, 90, 30))
        self.pushButton_3.setObjectName("pushButton_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(0, 140, 1360, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(230, 150, 20, 610))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(785, 150, 20, 610))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 200, 46, 14))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 250, 46, 14))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 300, 46, 14))
        self.label_3.setObjectName("label_3")
        self.line_4 = QtWidgets.QFrame(self.centralwidget)
        self.line_4.setGeometry(QtCore.QRect(0, 340, 241, 45))
        self.line_4.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(250, 130, 51, 16))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(1280, 130, 51, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 51, 16))
        self.label_6.setObjectName("label_6")

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1084, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.image1 = QtWidgets.QLabel(MainWindow)
        self.image1.setGeometry(QtCore.QRect(250,160, 530, 530))
        self.image1.setPixmap(QtGui.QPixmap('cam1.jpg'))

        self.image2 = QtWidgets.QLabel(MainWindow)
        self.image2.setGeometry(QtCore.QRect(810, 160, 530, 530))
        self.image2.setPixmap(QtGui.QPixmap('cam1.jpg'))

        self.image3 = QtWidgets.QLabel(MainWindow)
        self.image3.setGeometry(QtCore.QRect(10, 375, 220, 220))
        self.image3.setPixmap(QtGui.QPixmap('cam1.jpg'))

        #Camera
        self.cap1 = cv2.VideoCapture(0)
        self.cap2 = cv2.VideoCapture(1)

        # create a timer
        self.timer = QtCore.QTimer()
        self.timer.start(30)
        self.timer.timeout.connect(self.viewCam)

        #Serial
        self.serialPort = MySerialClass()
        self.serialPort.start()

    # view camera
    def viewCam(self):
        try:
            # STREET 1 GO 
            if self.serialPort.mess > (self.rtime + self.ytime):
                if self.serialPort.mess == (self.rtime + self.ytime + self.gtime):
                    self.lcdNumber.setStyleSheet("QLCDNumber {color: green;}")
                    self.lcdNumber_2.setStyleSheet("QLCDNumber {color: red;}")
                self.lcdNumber.display(self.serialPort.mess - self.rtime - self.ytime)
                self.lcdNumber_2.display(self.serialPort.mess - self.rtime)
                if self.serialPort.mess == (self.rtime + self.ytime + 5):
                    print("check camera 1")
                    self.recognize()
                    self.image3.setPixmap(QtGui.QPixmap('result_image.jpg'))
                    self.plainTextEdit.setText('1')
                    self.plainTextEdit_2.setText('2')
                    self.plainTextEdit_3.setText('3')
            elif self.serialPort.mess > self.rtime:
                if self.serialPort.mess == (self.rtime + self.ytime):
                    self.lcdNumber.setStyleSheet("QLCDNumber {color: yellow;}")
                    self.lcdNumber_2.setStyleSheet("QLCDNumber {color: red;}")
                self.lcdNumber.display(self.serialPort.mess - self.rtime)
                self.lcdNumber_2.display(self.serialPort.mess - self.rtime)
            #STREET 2 GO
            elif self.serialPort.mess > self.ytime:
                if self.serialPort.mess == self.rtime:
                    self.lcdNumber.setStyleSheet("QLCDNumber {color: red;}")
                    self.lcdNumber_2.setStyleSheet("QLCDNumber {color: green;}")
                self.lcdNumber.display(self.serialPort.mess)
                self.lcdNumber_2.display(self.serialPort.mess - self.ytime)
                if self.serialPort.mess == (self.ytime + 5):
                    print("check camera 2")
                    self.recognize()
                    self.image3.setPixmap(QtGui.QPixmap('result_image.jpg'))
                    self.plainTextEdit.setText('3')
                    self.plainTextEdit_2.setText('2')
                    self.plainTextEdit_3.setText('1')
            elif self.serialPort.mess <= self.ytime:
                if self.serialPort.mess == self.ytime:
                    self.lcdNumber.setStyleSheet("QLCDNumber {color: red;}")
                    self.lcdNumber_2.setStyleSheet("QLCDNumber {color: yellow;}")
                self.lcdNumber.display(self.serialPort.mess)
                self.lcdNumber_2.display(self.serialPort.mess)

            frame1 = self.cap1.read()[1]
            frame1 = frame1[::,140:500]
            frame1 = cv2.resize(frame1, (530,530))
            cv2.imwrite('webcam1.jpg', frame1)
            self.image1.setPixmap(QtGui.QPixmap('webcam1.jpg'))

            frame2 = self.cap2.read()[1]
            #frame2 = frame2[::,140:500]
            frame2 = cv2.resize(frame2, (400,400))
            cv2.imwrite('webcam2.jpg', frame2)
            self.image2.setPixmap(QtGui.QPixmap('webcam2.jpg'))
        except:
            pass
    def recognize(self):
        img = cv2.imread("test.jpg")
        #img = cv2.resize(img, None, fx=0.4, fy=0.4)
        height, width, channels = img.shape
        # Detecting objects
        blob = cv2.dnn.blobFromImage(img, 0.00392, (416, 416), (0, 0, 0), True, crop=False)
        self.net.setInput(blob)
        outs = self.net.forward(self.output_layers)
        # Showing informations on the screen
        class_ids = []
        confidences = []
        boxes = []
        for out in outs:
            for detection in out:
                scores = detection[5:]
                class_id = np.argmax(scores)
                confidence = scores[class_id]
                if confidence > 0.5:
                    # Object detected
                    center_x = int(detection[0] * width)
                    center_y = int(detection[1] * height)
                    w = int(detection[2] * width)
                    h = int(detection[3] * height)
                    # Rectangle coordinates
                    x = int(center_x - w / 2)
                    y = int(center_y - h / 2)
                    boxes.append([x, y, w, h])
                    confidences.append(float(confidence))
                    class_ids.append(class_id)

        indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)
        print(indexes)
        font = cv2.FONT_HERSHEY_PLAIN
        for i in range(len(boxes)):
            if i in indexes:
                x, y, w, h = boxes[i]
                label = str(self.classes[class_ids[i]])
                color = self.colors[class_ids[i]]
                cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
                cv2.putText(img, label, (x, y + 30), font, 3, color, 3)
        img = cv2.resize(img, (220,220))
        cv2.imwrite('result_image.jpg', img)
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "START"))
        self.pushButton_2.setText(_translate("MainWindow", "DEFAULT"))
        self.pushButton_3.setText(_translate("MainWindow", "Google"))
        self.label.setText(_translate("MainWindow", "CAR"))
        self.label_2.setText(_translate("MainWindow", "BUS"))
        self.label_3.setText(_translate("MainWindow", "TRUCK"))
        self.label_4.setText(_translate("MainWindow", "STREET 1"))
        self.label_5.setText(_translate("MainWindow", "STREET 2"))
        self.label_6.setText(_translate("MainWindow", "RESULT:"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
