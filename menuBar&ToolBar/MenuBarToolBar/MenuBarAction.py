import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
from MenuBarToolBar.MainFrom import Ui_MainWindow

class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainForm, self).__init__()
        self.setupUi(self)

        self.CloseFileAction.triggered.connect(self.close)
        self.CreateNewFileAction.triggered.connect(self.openMsg)

    def openMsg(self):

        file, ok = QFileDialog.getOpenFileName(self, "打开", "C:/", "Al Files (*);;Text Files (*.txt)")
        self.statusbar.showMessage(file)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainForm()
    win.show()
    sys.exit(app.exec_())