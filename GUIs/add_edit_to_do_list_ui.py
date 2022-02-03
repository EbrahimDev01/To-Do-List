# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\Designs\add_edit_to_do_list_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(560, 683)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 10, 541, 628))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.lineEdit_titile_to_do = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.lineEdit_titile_to_do.setObjectName("lineEdit_titile_to_do")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_titile_to_do)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.textEdit_details_to_do = QtWidgets.QTextEdit(self.formLayoutWidget)
        self.textEdit_details_to_do.setObjectName("textEdit_details_to_do")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_details_to_do)
        self.checkBox_use_date_time = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.checkBox_use_date_time.setChecked(True)
        self.checkBox_use_date_time.setObjectName("checkBox_use_date_time")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.checkBox_use_date_time)
        self.label_start_to_do = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_start_to_do.setObjectName("label_start_to_do")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_start_to_do)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.calendarWidget_start_date_to_do = QtWidgets.QCalendarWidget(self.formLayoutWidget)
        self.calendarWidget_start_date_to_do.setObjectName("calendarWidget_start_date_to_do")
        self.verticalLayout_4.addWidget(self.calendarWidget_start_date_to_do)
        self.timeEdit_start_time_to_do = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.timeEdit_start_time_to_do.setObjectName("timeEdit_start_time_to_do")
        self.verticalLayout_4.addWidget(self.timeEdit_start_time_to_do)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_4)
        self.label_end_to_do = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_end_to_do.setObjectName("label_end_to_do")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_end_to_do)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.calendarWidget_end_date_to_do = QtWidgets.QCalendarWidget(self.formLayoutWidget)
        self.calendarWidget_end_date_to_do.setObjectName("calendarWidget_end_date_to_do")
        self.verticalLayout_5.addWidget(self.calendarWidget_end_date_to_do)
        self.timeEdit_end_time_to_do = QtWidgets.QTimeEdit(self.formLayoutWidget)
        self.timeEdit_end_time_to_do.setObjectName("timeEdit_end_time_to_do")
        self.verticalLayout_5.addWidget(self.timeEdit_end_time_to_do)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btn_save = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_3.addWidget(self.btn_save)
        self.btn_cansel = QtWidgets.QPushButton(self.formLayoutWidget)
        self.btn_cansel.setObjectName("btn_cansel")
        self.horizontalLayout_3.addWidget(self.btn_cansel)
        self.formLayout.setLayout(6, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_3)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 560, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add To Do List"))
        self.label.setText(_translate("MainWindow", "Title To Do"))
        self.label_4.setText(_translate("MainWindow", "Details To Do"))
        self.checkBox_use_date_time.setText(_translate("MainWindow", "use date time ???"))
        self.label_start_to_do.setText(_translate("MainWindow", "Start To Do"))
        self.label_end_to_do.setText(_translate("MainWindow", "End To Do"))
        self.btn_save.setText(_translate("MainWindow", "Save"))
        self.btn_cansel.setText(_translate("MainWindow", "Cansel"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
