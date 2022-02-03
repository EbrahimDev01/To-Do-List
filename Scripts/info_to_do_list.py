from PyQt5.QtWidgets import QMainWindow, QApplication
from to_do_list_repository import ToDoListRepository
from GUIs import info_to_do_ui

to_do_list_repository = ToDoListRepository()


class InfoToDoListWindow(QMainWindow):
    def __init__(self, parent):
        super().__init__(parent=parent)
        self.ui = info_to_do_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()

    def get_to_do_list_item_by_id(self, to_do_list_item_id):
        to_do_item = to_do_list_repository.get_to_do_list_item_by_id(to_do_list_item_id)
        self.load_to_do_item_in_form(to_do_item)

    def load_to_do_item_in_form(self, to_do_item):
        self.ui.lineEdit_info_title_to_do.setText(to_do_item[1])
        self.ui.textEdit_info_details_to_do.setText(to_do_item[2])
        self.ui.checkBox_Done.setChecked(to_do_item[3])

        if to_do_item[4]:
            self.ui.calendarWidget_info_start_date_to_do.setDateRange(to_do_item[4], to_do_item[4])
            self.ui.timeEdit_info_start_time_to_do.setTimeRange(to_do_item[4].time(), to_do_item[4].time())
        else:
            self.ui.calendarWidget_info_start_date_to_do.hide()
            self.ui.timeEdit_info_start_time_to_do.hide()
            self.ui.label_start_to_do.hide()
        if to_do_item[5]:
            self.ui.calendarWidget_info_end_date_to_do.setDateRange(to_do_item[5], to_do_item[5])
            self.ui.timeEdit_info_end_time_to_do.setTimeRange(to_do_item[5].time(), to_do_item[5].time())
        else:
            self.ui.calendarWidget_info_end_date_to_do.hide()
            self.ui.timeEdit_info_end_time_to_do.hide()
            self.ui.label_end_to_do.hide()


if __name__ == '__main__':
    import sys

    item_id = to_do_list_repository.get_all_to_do_items()[0][0]
    app = QApplication(sys.argv)
    ui = InfoToDoListWindow(None)
    ui.get_to_do_list_item_by_id(item_id)
    sys.exit(app.exec_())
