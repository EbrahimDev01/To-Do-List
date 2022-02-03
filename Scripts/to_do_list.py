import sys
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QTableWidgetItem, QMessageBox
from to_do_list_repository import ToDoListRepository, initialize_database
from GUIs import to_do_list_ui
from info_to_do_list import InfoToDoListWindow
from add_edit_to_do_list_ui import AddEditToDoListWindow

to_do_list_repository = ToDoListRepository()
initialize_database()


class ToDoListWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = to_do_list_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        self.setup_events()

        self.refresh_table_widget_to_do_list()
        self.ui.tableWidget_to_do_list.setHorizontalHeaderLabels(
            ['', 'Title', 'Details', 'Active', 'Start DateTime', 'End DateTime'])
        self.children_window = None
        self.show()

    def setup_events(self):
        # button events
        self.ui.btn_refresh_to_do_item.clicked.connect(self.event_clicked_btn_refresh_to_do_item)
        self.ui.btn_delete_to_do_item.clicked.connect(self.event_clicked_btn_delete_to_do_item)
        self.ui.btn_show_info_to_do_item.clicked.connect(self.event_clicked_btn_show_info_to_do_item)
        self.ui.btn_add_to_do_item.clicked.connect(self.event_btn_add_to_do_item)
        self.ui.btn_edit_to_do_item.clicked.connect(self.event_btn_edit_to_do_item)
        self.ui.btn_to_or_do.clicked.connect(self.event_clicked_btn_to_or_do)

        # line edit events
        self.ui.lineEdit_search_in_to_do_list.textEdited.connect(
            self.event_key_press_event_line_edit_search_in_to_do_list)

    def event_clicked_btn_refresh_to_do_item(self):
        self.refresh_table_widget_to_do_list()

    def event_clicked_btn_delete_to_do_item(self):
        item_id = self.get_id_row_table()
        if item_id:
            to_do_list_repository.delete_to_do_item(item_id)
            self.refresh_table_widget_to_do_list()

    def event_clicked_btn_show_info_to_do_item(self):
        self.create_new_children(InfoToDoListWindow, True)

    def event_btn_add_to_do_item(self):
        self.create_new_children(AddEditToDoListWindow, False)

    def event_btn_edit_to_do_item(self):
        self.create_new_children(AddEditToDoListWindow, True)

    def event_key_press_event_line_edit_search_in_to_do_list(self):
        text = self.ui.lineEdit_search_in_to_do_list.text()
        self.search(text)

    def event_clicked_btn_to_or_do(self):
        item_id = self.get_id_row_table()
        if item_id:
            to_do_list_repository.to_or_do(item_id)
            self.refresh_active_table_to_do_list(item_id)

    def load_data_to_tableWidget_to_do_list(self, data):
        self.ui.tableWidget_to_do_list.clearContents()
        self.ui.tableWidget_to_do_list.setRowCount(len(data))
        if not data:
            return
        self.ui.tableWidget_to_do_list.setColumnCount(len(data[0]))
        self.ui.tableWidget_to_do_list.setColumnHidden(0, True)

        for i, (to_do_list_id, title, details, active, start_datetime, end_datetime) in enumerate(data):
            item_id = QTableWidgetItem(str(to_do_list_id))
            item_title = QTableWidgetItem(title)
            item_details = QTableWidgetItem(details[0:25] + '...')

            item_active = QTableWidgetItem(active)
            item_active.setCheckState(QtCore.Qt.Checked if active else QtCore.Qt.Unchecked)

            item_start_datetime = QTableWidgetItem('Not Defined' if start_datetime is None else str(start_datetime))
            item_end_datetime = QTableWidgetItem('Not Defined' if end_datetime is None else str(end_datetime))

            for item in (item_id, item_title, item_details, item_start_datetime, item_end_datetime, item_active):
                item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

            self.ui.tableWidget_to_do_list.setItem(i, 0, item_id)
            self.ui.tableWidget_to_do_list.setItem(i, 1, item_title)
            self.ui.tableWidget_to_do_list.setItem(i, 2, item_details)
            self.ui.tableWidget_to_do_list.setItem(i, 3, item_active)
            self.ui.tableWidget_to_do_list.setItem(i, 4, item_start_datetime)
            self.ui.tableWidget_to_do_list.setItem(i, 5, item_end_datetime)

    def get_id_row_table(self):
        current_row = self.ui.tableWidget_to_do_list.currentRow()

        if not (row_selected := self.ui.tableWidget_to_do_list.item(current_row, 0)):
            self.msg = QMessageBox()
            self.msg.setText('row not selected')
            self.msg.setIcon(QMessageBox.Critical)
            self.msg.setStandardButtons(QMessageBox.Ok)
            self.msg.show()
            return False

        return int(row_selected.text())

    def refresh_active_table_to_do_list(self, to_do_item_id):
        active = to_do_list_repository.get_to_do_list_item_by_id(to_do_item_id)[3]
        current_row = self.ui.tableWidget_to_do_list.currentRow()
        item_active = QTableWidgetItem()
        item_active.setCheckState(QtCore.Qt.Checked if active else QtCore.Qt.Unchecked)
        self.ui.tableWidget_to_do_list.setItem(current_row, 3, item_active)

    def refresh_table_widget_to_do_list(self):
        to_do_list_data = to_do_list_repository.get_all_to_do_items()
        self.load_data_to_tableWidget_to_do_list(to_do_list_data)

    def search(self, text: str):
        result = to_do_list_repository.search_to_do_item(text)
        self.load_data_to_tableWidget_to_do_list(result)

    def create_new_children(self, type_children_window, has_initial_value: bool = False):
        if not self.children_window or type(self.children_window) is not type(type_children_window):
            if has_initial_value:
                if item_id := self.get_id_row_table():
                    self.children_window = type_children_window(self)
                    self.children_window.get_to_do_list_item_by_id(item_id)
                    self.children_window.show()
            else:
                self.children_window = type_children_window(self)
                self.children_window.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ui = ToDoListWindow()
    sys.exit(app.exec_())
