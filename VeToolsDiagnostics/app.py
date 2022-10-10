import os
import sys

from PySide6.QtCore import Qt, QUrl
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox

# to run outside pycharm
folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, folder)

from infrastructure.PathResolver import resolve_path
from DataAccess import DataAccess
from MainWindow import Ui_MainWindow

# noinspection PyUnresolvedReferences
import logo_rsrc

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
                    image: url(':/static/img/logo_transparent.png');
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

        # when the start button is clicked, set the data to the root node of the selected disease
        self.Data.base_data = self.Data.get_disease_root_node(self.Data.yml_data, selected_disease)
        self.Data.flag = self.Data.current_node_flag(self.Data.yml_data, selected_disease)

        # initially same as base_data; will be continuously updated as the user answers questions
        self.Data.current_data = self.Data.base_data.copy()

        # set the text to the current node's text
        self.Data.text = self.Data.current_data['text']
        self.question.setText(self.Data.text)

        # set center alignment for the little questions
        self.question.setAlignment(Qt.AlignCenter)

        # filepath for the selected disease's markdown file
        disease_education_fp = resolve_path(f'data/edu/{selected_disease}.md')
        disease_education_fp = QUrl.fromLocalFile(disease_education_fp)

        # todo: if multiple fecal positives are selected then loop through the required texts

        # set the education_textbox to contain the selected disease's education markdown
        self.education_textbox.setSource(disease_education_fp)

        # set the stacked widget to the education page
        self.stackedWidget.setCurrentIndex(2)

    def edu_next_btn_clicked(self):
        self.stackedWidget.setCurrentIndex(1)

    def edu_prev_btn_clicked(self):
        # same as if end button clicked
        self.end_button_clicked()

    def next_button_clicked(self):
        # get the selected radio button
        if self.option_0.isChecked():
            self.Data.update_data('affirmative')
            self.question.setText(self.Data.text)

        elif self.option_1.isChecked():
            self.Data.update_data('negative')
            self.question.setText(self.Data.text)

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
        if self.Data.flag == 'start':
            self.stackedWidget.setCurrentIndex(2)
        else:
            # set center alignment for the little questions
            self.question.setAlignment(Qt.AlignCenter)

            # only calls .isVisible(true) if radios are hidden
            self.show_radios()

            # update the data to the previous node
            self.Data.current_data = self.Data.reset_to_flag(self.Data.base_data)
            self.Data.text = self.Data.current_data['text']
            self.Data.flag = self.Data.current_data['flag']

            self.question.setText(self.Data.text)
            self.next_button.setVisible(True)

    def end_button_clicked(self):
        self.show_radios()
        self.stackedWidget.setCurrentIndex(0)
        self.Data.reset_data()
        self.education_textbox.clear()
        self.next_button.setVisible(True)

    def hide_radios(self):
        if self.option_0.isVisible():
            self.option_0.setVisible(False)
            self.option_1.setVisible(False)

    def show_radios(self):
        if not self.option_0.isVisible():
            self.option_0.setVisible(True)
            self.option_1.setVisible(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setApplicationDisplayName('VeTools')
    main_window = MainWindow()
    main_window.setWindowTitle('VeTools')
    main_window.show()
    sys.exit(app.exec())
