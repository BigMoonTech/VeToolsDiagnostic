import os
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

from infrastructure.PathResolver import resolve_path

folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from DataAccess import DataAccess
from MainWindow import Ui_MainWindow

# noinspection PyUnresolvedReferences
import logo_resource

try:
    from ctypes import windll  # Only exists on Windows.
    app_id = 'BigMoonTech.VeTools.0.1'
    windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_id)
except ImportError:
    pass

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

        # connect the education page's buttons
        self.next_button_2.clicked.connect(self.edu_next_btn_clicked)
        self.prev_button_2.clicked.connect(self.edu_prev_btn_clicked)

        # end buttons
        self.end_button.clicked.connect(self.end_button_clicked)
        self.end_button_2.clicked.connect(self.end_button_clicked)

        # connect other actions
        self.actionQuit_VeTools.triggered.connect(sys.exit)

    def start_button_clicked(self):
        selected_disease = "".join(self.disease_selection.currentText().split()).strip()

        # filepath for the selected md file
        md_path = resolve_path(f'data/edu/{selected_disease}.md')

        # todo: if multiple fecal positives are selected then loop through the required texts
        # set the education_textbox to contain the selected md file
        self.education_textbox.setSource(md_path)

        self.stackedWidget.setCurrentIndex(2)

        self.Data.disease_text = selected_disease
        self.Data.base_data = self.Data.get_disease_dict(self.Data.yml_data, selected_disease)  # reset the tree
        self.Data.flag = self.Data.get_current_flag(self.Data.yml_data, selected_disease)
        self.Data.data = self.Data.base_data.copy()  # will update to the current branch of the decision tree
        self.Data.text = self.Data.data['text']
        self.question.setText(self.Data.text)

        # set center alignment for the little questions
        self.question.setAlignment(Qt.AlignCenter)

    def edu_next_btn_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def edu_prev_btn_clicked(self):
        # same as if end button clicked
        self.end_button_clicked()

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
            # set justified alignment for the longer texts
            self.question.setAlignment(Qt.AlignJustify | Qt.AlignVCenter)
            self.hide_radios()
            self.next_button.setVisible(False)

    def prev_button_clicked(self):
        print(self.Data.flag)
        if self.Data.flag == 'start':
            self.stackedWidget.setCurrentIndex(2)
        else:
            # set center alignment for the little questions
            self.question.setAlignment(Qt.AlignCenter)
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
        self.education_textbox.clear()
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
