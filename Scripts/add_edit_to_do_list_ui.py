import datetime

from PyQt5.QtWidgets import QMainWindow
from GUIs.add_edit_to_do_ui import Ui_MainWindow
from to_do_list_repository import ToDoListRepository

to_do_list_repository = ToDoListRepository()


class AddEditToDoListWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_events()
        self.item_id = None
        self.show()

    def setup_events(self):
        self.ui.btn_cansel.clicked.connect(self.event_btn_cansel)
        self.ui.btn_save.clicked.connect(self.event_btn_ok)
        self.ui.checkBox_use_date_time.stateChanged.connect(self.event_clicked_check_box_use_date_time)

    def event_clicked_check_box_use_date_time(self):
        self.use_date_time(self.ui.checkBox_use_date_time.isChecked())

    def event_btn_cansel(self):
        self.close()

    # save form base add or edit
    def event_btn_ok(self):
        title = self.ui.lineEdit_titile_to_do.text()
        details = self.ui.textEdit_details_to_do.toPlainText()
        start_datetime = None
        end_datetime = None

        if self.ui.checkBox_use_date_time.isChecked():
            start_date = self.ui.calendarWidget_start_date_to_do.selectedDate().toPyDate()
            start_time = self.ui.timeEdit_start_time_to_do.time().toPyTime()
            start_datetime = datetime.datetime.combine(start_date, start_time)

            end_date = self.ui.calendarWidget_end_date_to_do.selectedDate().toPyDate()
            end_time = self.ui.timeEdit_end_time_to_do.time().toPyTime()
            end_datetime = datetime.datetime.combine(end_date, end_time)

        if self.item_id is None:
            to_do_list_repository.insert_to_do_item(title, details, start_datetime, end_datetime)
        else:
            to_do_list_repository.update_to_do_item(self.item_id,title, details, start_datetime, end_datetime)

    def get_to_do_list_item_by_id(self, to_do_list_item_id):
        self.item_id = to_do_list_item_id
        to_do_item = to_do_list_repository.get_to_do_list_item_by_id(to_do_list_item_id)
        self.load_to_do_item_in_form(to_do_item)

    def load_to_do_item_in_form(self, to_do_item):
        self.setWindowTitle('Edit to do list')
        self.ui.lineEdit_titile_to_do.setText(to_do_item[1])
        self.ui.textEdit_details_to_do.setText(to_do_item[2])
        self.ui.checkBox_use_date_time.setChecked(self.use_date_time(bool(to_do_item[4]) and bool(to_do_item[5])))

        if to_do_item[4]:
            self.ui.calendarWidget_start_date_to_do.setSelectedDate(to_do_item[4])
            self.ui.timeEdit_start_time_to_do.setTime(to_do_item[4].time())
        if to_do_item[5]:
            self.ui.calendarWidget_end_date_to_do.setSelectedDate(to_do_item[5])
            self.ui.timeEdit_end_time_to_do.setTime(to_do_item[5].time())

    def use_date_time(self, used: bool):
        for widget in (self.ui.calendarWidget_start_date_to_do, self.ui.calendarWidget_end_date_to_do,
                       self.ui.timeEdit_start_time_to_do, self.ui.timeEdit_end_time_to_do,
                       self.ui.label_start_to_do, self.ui.label_end_to_do):
            if used:
                widget.show()
            else:
                widget.hide()
        return used
        # if used:
        # self.ui.calendarWidget_start_date_to_do.hide()
        # self.ui.calendarWidget_end_date_to_do.hide()
        # self.ui.timeEdit_start_time_to_do.hide()
        # self.ui.timeEdit_end_time_to_do.hide()
        # self.ui.label_start_to_do.hide()
        # self.ui.label_end_to_do.hide()
        # else:
        # self.ui.calendarWidget_start_date_to_do.show()
        # self.ui.calendarWidget_end_date_to_do.show()
        # self.ui.timeEdit_start_time_to_do.show()
        # self.ui.timeEdit_end_time_to_do.show()
        # self.ui.label_start_to_do.show()
        # self.ui.label_end_to_do.show()


if __name__ == '__main__':
    import sys
    from PyQt5.QtWidgets import QApplication

    item_id = to_do_list_repository.get_all_to_do_items()[0][0]
    app = QApplication(sys.argv)
    ui = AddEditToDoListWindow(None)
    # ui.get_to_do_list_item_by_id(item_id)
    sys.exit(app.exec_())
