import os
import sys
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from VeToolsDiagnostics.DataAccess import DataAccess
from VeToolsDiagnostics.MainWindow import Ui_MainWindow

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # required for Qt: set up the UI
        self.setupUi(self)

        # create data access layer
        self.da = DataAccess()

        # display a critical QMessageBox if the yml data wasn't loaded properly and close the app
        if self.da.yml_data is None:
            QMessageBox.critical(
                self,
                'File Error',
                f'The data file could not be found \n the filepath: {self.da.filepath}'
            )
            sys.exit(1)

        self.start_button.clicked.connect(self.start_button_clicked)
        self.next_button.clicked.connect(self.next_button_clicked)
        self.prev_button.clicked.connect(self.prev_button_clicked)
        self.end_button.clicked.connect(self.end_button_clicked)
        self.actionQuit_VeTools.triggered.connect(sys.exit)


    def start_button_clicked(self):
        selected_disease = "".join(self.disease_selection.currentText().split()).strip()
        self.da.disease_text = selected_disease
        self.da.base_data = self.da.get_disease_dict(self.da.yml_data, selected_disease)  # to reset the decision tree
        self.da.flag = self.da.get_current_flag(self.da.yml_data, selected_disease)
        self.da.data = self.da.base_data.copy()  # will update to the current branch of the decision tree
        self.da.text = self.da.data['text']

        self.question.setText(self.da.text)
        self.stackedWidget.setCurrentIndex(1)

    def next_button_clicked(self):
        # get the selected radio button
        if self.option_0.isChecked():
            self.da.data = self.da.data['affirmative']
            self.da.text = self.da.data['text']
            self.da.question_history.append(self.da.flag)
            self.question.setText(self.da.text)
            self.da.flag = self.da.data['flag']

        elif self.option_1.isChecked():
            self.da.data = self.da.data['negative']
            self.da.text = self.da.data['text']
            self.da.question_history.append(self.da.flag)
            self.question.setText(self.da.text)
            self.da.flag = self.da.data['flag']
        else:
            QMessageBox.critical(
                self,
                'Operation Error!',
                'Please select an option.'
            )

        if 'end' in self.da.flag:
            self.next_button.setVisible(False)

    def prev_button_clicked(self):
        if self.da.flag == 'start':
            self.end_button_clicked()
        else:
            self.da.data = self.da.reset_to_flag(self.da.base_data)
            self.da.text = self.da.data['text']
            self.da.flag = self.da.data['flag']
            self.question.setText(self.da.text)
            self.next_button.setVisible(True)


    def end_button_clicked(self):
        self.stackedWidget.setCurrentIndex(0)
        self.da.reset_data()
        self.next_button.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName('VeTools')
    main_window = MainWindow()
    main_window.setWindowTitle('VeTools')
    main_window.show()
    sys.exit(app.exec())
