# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Interface_Detect_Cancer.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1579, 800)
        Form.setMinimumSize(QtCore.QSize(1579, 800))
        Form.setMaximumSize(QtCore.QSize(1579, 800))
        font = QtGui.QFont()
        font.setPointSize(10)
        Form.setFont(font)
        self.comboX = QtWidgets.QComboBox(Form)
        self.comboX.setGeometry(QtCore.QRect(1020, 760, 151, 31))
        font = QtGui.QFont()
        font.setFamily("PMingLiU")
        font.setPointSize(10)
        self.comboX.setFont(font)
        self.comboX.setTabletTracking(True)
        self.comboX.setObjectName("comboX")
        self.btnResult = QtWidgets.QPushButton(Form)
        self.btnResult.setGeometry(QtCore.QRect(1210, 760, 161, 31))
        self.btnResult.setObjectName("btnResult")
        self.label_Input = QtWidgets.QLabel(Form)
        self.label_Input.setGeometry(QtCore.QRect(20, 170, 500, 500))
        self.label_Input.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.label_Input.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Input.setLineWidth(1)
        self.label_Input.setText("")
        self.label_Input.setScaledContents(True)
        self.label_Input.setWordWrap(False)
        self.label_Input.setObjectName("label_Input")
        self.label_Pre_Processing = QtWidgets.QLabel(Form)
        self.label_Pre_Processing.setGeometry(QtCore.QRect(540, 170, 500, 500))
        self.label_Pre_Processing.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Pre_Processing.setLineWidth(1)
        self.label_Pre_Processing.setText("")
        self.label_Pre_Processing.setScaledContents(True)
        self.label_Pre_Processing.setWordWrap(False)
        self.label_Pre_Processing.setObjectName("label_Pre_Processing")
        self.label_Output = QtWidgets.QLabel(Form)
        self.label_Output.setGeometry(QtCore.QRect(1060, 170, 500, 500))
        self.label_Output.setFrameShape(QtWidgets.QFrame.Box)
        self.label_Output.setLineWidth(1)
        self.label_Output.setText("")
        self.label_Output.setScaledContents(True)
        self.label_Output.setWordWrap(False)
        self.label_Output.setObjectName("label_Output")
        self.link_Browser = QtWidgets.QTextBrowser(Form)
        self.link_Browser.setGeometry(QtCore.QRect(270, 760, 731, 31))
        self.link_Browser.setObjectName("link_Browser")
        self.result_Browser = QtWidgets.QTextBrowser(Form)
        self.result_Browser.setGeometry(QtCore.QRect(1210, 720, 351, 31))
        self.result_Browser.setObjectName("result_Browser")
        self.btnBrowser = QtWidgets.QPushButton(Form)
        self.btnBrowser.setGeometry(QtCore.QRect(110, 760, 121, 31))
        self.btnBrowser.setObjectName("btnBrowser")
        self.name_label = QtWidgets.QLabel(Form)
        self.name_label.setGeometry(QtCore.QRect(340, 10, 961, 131))
        font = QtGui.QFont()
        font.setFamily("PMingLiU")
        font.setPointSize(27)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name_label.setFont(font)
        self.name_label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_label.setTextFormat(QtCore.Qt.AutoText)
        self.name_label.setScaledContents(False)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.Input_label = QtWidgets.QLabel(Form)
        self.Input_label.setGeometry(QtCore.QRect(190, 670, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Input_label.setFont(font)
        self.Input_label.setObjectName("Input_label")
        self.Preprocessing_label = QtWidgets.QLabel(Form)
        self.Preprocessing_label.setGeometry(QtCore.QRect(710, 670, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.Preprocessing_label.setFont(font)
        self.Preprocessing_label.setObjectName("Preprocessing_label")
        self.detectionimage = QtWidgets.QLabel(Form)
        self.detectionimage.setGeometry(QtCore.QRect(1260, 670, 141, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.detectionimage.setFont(font)
        self.detectionimage.setObjectName("detectionimage")
        self.btnprocessing = QtWidgets.QPushButton(Form)
        self.btnprocessing.setGeometry(QtCore.QRect(1390, 760, 171, 31))
        self.btnprocessing.setObjectName("btnprocessing")
        self.Slider_process = QtWidgets.QSlider(Form)
        self.Slider_process.setGeometry(QtCore.QRect(270, 720, 731, 22))
        self.Slider_process.setOrientation(QtCore.Qt.Horizontal)
        self.Slider_process.setObjectName("Slider_process")
        self.Input_label_3 = QtWidgets.QLabel(Form)
        self.Input_label_3.setGeometry(QtCore.QRect(110, 710, 151, 31))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.Input_label_3.setFont(font)
        self.Input_label_3.setObjectName("Input_label_3")
        self.result_slide_process = QtWidgets.QTextBrowser(Form)
        self.result_slide_process.setGeometry(QtCore.QRect(1020, 720, 151, 31))
        self.result_slide_process.setObjectName("result_slide_process")
        self.name_label_2 = QtWidgets.QLabel(Form)
        self.name_label_2.setGeometry(QtCore.QRect(20, 100, 1531, 101))
        font = QtGui.QFont()
        font.setFamily("PMingLiU")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(True)
        self.name_label_2.setFont(font)
        self.name_label_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.name_label_2.setTextFormat(QtCore.Qt.AutoText)
        self.name_label_2.setScaledContents(False)
        self.name_label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label_2.setObjectName("name_label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Detection Nodules"))
        self.btnResult.setText(_translate("Form", "Detect"))
        self.btnBrowser.setText(_translate("Form", "Browser"))
        self.name_label.setText(_translate("Form", "Evaluate The Malignancy Of Pulmonary Nodules \n"
        "Using 3-D Deep Leaky Noisy-OR Network"))
        self.Input_label.setText(_translate("Form", "Original Image"))
        self.Preprocessing_label.setText(_translate("Form", "Preprocessing Image"))
        self.detectionimage.setText(_translate("Form", "Detection Image"))
        self.btnprocessing.setText(_translate("Form", "Show Image of Result"))
        self.Input_label_3.setText(_translate("Form", "Processing Slice"))
        self.name_label_2.setText(_translate("Form", "Le Phong Phu, Nguyen Vu Le Minh, Tran Thi Ai, Nguyen Thanh Binh, Nguyen Duc Nhat Quang"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
