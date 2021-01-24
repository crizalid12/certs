from gui import Ui_MainWindow
from PyQt5 import QtWidgets
import sys


class AppWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.initialize_UI()
        self.ui.search_toggle_cbox.currentIndexChanged.connect(
            self.toggle_search)
        self.show()

    def initialize_UI(self):
        """
            Initialze the ui and add basic functionality like:
            close buttons
            toggle between stackedWidget pages
            ...
        """
        self.ui.stdreg_number.hide()
        self.ui.stackedWidget.setCurrentIndex(0)
        self.ui.exit_btn.clicked.connect(self.close)
        self.ui.exit_btn_2.clicked.connect(self.close)
        self.ui.manage_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.main_btn.clicked.connect(
            lambda: self.ui.stackedWidget.setCurrentIndex(0))

    def toggle_search(self):
        if self.ui.search_toggle_cbox.currentIndex() == 1:
            self.ui.fname_edit.hide()
            self.ui.stdreg_number.show()
        else:
            self.ui.fname_edit.show()
            self.ui.stdreg_number.hide()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main_window = AppWindow()
    sys.exit(app.exec_())
