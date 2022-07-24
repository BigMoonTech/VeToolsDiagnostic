import os
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from DataAccess import DataAccess
from MainWindow import Ui_MainWindow

# noinspection PyUnresolvedReferences
import logo_resource


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # required for Qt: set up the UI
        self.setupUi(self)

        # data access layer
        self.Data = DataAccess()

        # display a critical QMessageBox if the yml data wasn't loaded properly and close the app
        if self.Data.yml_data is None:
            QMessageBox.critical(
                self,
                'File Error',
                f'The data file could not be found \n the filepath: {self.Data.filepath}'
            )
            sys.exit(1)

        # implant the logo
        self.stylesheet = """
                QStackedWidget {
                    image: url(':/static/img/logo.svg');
                }
            """
        self.setStyleSheet(self.stylesheet)

        # connect button actions
        self.start_button.clicked.connect(self.start_button_clicked)
        self.next_button.clicked.connect(self.next_button_clicked)
        self.prev_button.clicked.connect(self.prev_button_clicked)
        self.end_button.clicked.connect(self.end_button_clicked)
        self.actionQuit_VeTools.triggered.connect(sys.exit)

    def start_button_clicked(self):
        selected_disease = "".join(self.disease_selection.currentText().split()).strip()
        self.Data.disease_text = selected_disease
        self.Data.base_data = self.Data.get_disease_dict(self.Data.yml_data, selected_disease)  # reset the tree
        self.Data.flag = self.Data.get_current_flag(self.Data.yml_data, selected_disease)
        self.Data.data = self.Data.base_data.copy()  # will update to the current branch of the decision tree
        self.Data.text = self.Data.data['text']

        self.question.setText(self.Data.text)
        self.stackedWidget.setCurrentIndex(1)

    def next_button_clicked(self):
        # get the selected radio button
        if self.option_0.isChecked():
            self.Data.data = self.Data.data['affirmative']
            self.Data.text = self.Data.data['text']
            self.Data.question_history.append(self.Data.flag)
            self.question.setText(self.Data.text)
            self.Data.flag = self.Data.data['flag']

        elif self.option_1.isChecked():
            self.Data.data = self.Data.data['negative']
            self.Data.text = self.Data.data['text']
            self.Data.question_history.append(self.Data.flag)
            self.question.setText(self.Data.text)
            self.Data.flag = self.Data.data['flag']
        else:
            QMessageBox.critical(
                self,
                'Operation Error!',
                'Please select an option.'
            )

        if 'end' in self.Data.flag:
            self.hide_radios()
            self.next_button.setVisible(False)

    def prev_button_clicked(self):
        if self.Data.flag == 'start':
            self.end_button_clicked()
        else:
            self.show_radios()
            self.Data.data = self.Data.reset_to_flag(self.Data.base_data)
            self.Data.text = self.Data.data['text']
            self.Data.flag = self.Data.data['flag']
            self.question.setText(self.Data.text)
            self.next_button.setVisible(True)

    def end_button_clicked(self):
        self.show_radios()
        self.stackedWidget.setCurrentIndex(0)
        self.Data.reset_data()
        self.next_button.setVisible(True)

    def hide_radios(self):
        self.option_0.setVisible(False)
        self.option_1.setVisible(False)

    def show_radios(self):
        self.option_0.setVisible(True)
        self.option_1.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName('VeTools')
    main_window = MainWindow()
    main_window.setWindowTitle('VeTools')
    main_window.show()
    sys.exit(app.exec())
