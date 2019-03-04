#!/usr/bin/env python

import sys

from PyQt5.QtWidgets import QMainWindow, QApplication
from ui_esriapp import Ui_EsriApp


class EsriAppMain(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)

        # Set up the user interface from Designer.
        self.ui = Ui_EsriApp()
        self.ui.setupUi(self)

        # Connect up menu actions
        # self.ui.actionExit.triggered.connect(self.close)

        # Connect up buttons.
        # self.ui.BUTTON_NAME.clicked.connect(self._pushed)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = EsriAppMain()
    main.show()
    sys.exit(app.exec_())


