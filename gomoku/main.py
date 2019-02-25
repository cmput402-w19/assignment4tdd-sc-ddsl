from PyQt5 import QtWidgets
from gomoku.GUI import GUI
import sys

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = GUI()
    ex.show()
    sys.exit(app.exec_())
