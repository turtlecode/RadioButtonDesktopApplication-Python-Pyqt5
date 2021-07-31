import sys
from PyQt5 import QtWidgets
from radiobutton import Ui_MainWindow

class my_app(QtWidgets.QMainWindow):
    def __init__(self):
        super(my_app, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.turkey.toggled.connect(self.country_onclick)
        self.ui.england.toggled.connect(self.country_onclick)
        self.ui.germany.toggled.connect(self.country_onclick)
        self.ui.france.toggled.connect(self.country_onclick)

        self.ui.carpenter.toggled.connect(self.job_onclick)
        self.ui.doctor.toggled.connect(self.job_onclick)
        self.ui.teacher.toggled.connect(self.job_onclick)
        self.ui.police.toggled.connect(self.job_onclick)

        self.ui.get_selected.clicked.connect(self.get_selected)


    def job_onclick(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())


    def country_onclick(self):
        rb = self.sender()
        if rb.isChecked():
            print(rb.text())

    def get_selected(self):
        text_country = ''
        text_job = ''
        full_text = ''
        items_country = self.ui.country_box.findChildren(QtWidgets.QRadioButton)
        for item_country in items_country:
            if item_country.isChecked():
                text_country = "You are from " + item_country.text() + '\n'
        items_job = self.ui.job_group.findChildren(QtWidgets.QRadioButton)
        for item_job in items_job:
            if item_job.isChecked():
                text_job = "Your job is " + item_job.text()
        full_text = text_country + text_job

        self.ui.label.setText(full_text)


def create_app():
    app = QtWidgets.QApplication(sys.argv)
    win = my_app()
    win.show()
    sys.exit(app.exec_())

create_app()