import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtSql import QSqlDatabase, QSqlTableModel
from PyQt5.QtCore import Qt

def initializeModel(model):
    model.setTable('peopleinfo')
    model.setEditStrategy(QSqlTableModel.OnFieldChange)
    model.select()
    model.setHeaderData(0, Qt.Horizontal, "ID")
    model.setHeaderData(1, Qt.Horizontal, "name")
    model.setHeaderData(2, Qt.Horizontal, "address")

def createView(title, model):
    view = QTableView()
    view.setModel(model)
    view.setWindowTitle(title)
    return view

def addrow():
    ret = model.insertRows(model.rowCount(), 1)
    print('insertRows=%s' % str(ret))

def findrow(i):
    delrow = i.row()
    print('del row=%s' % str(ret))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    db = QSqlDatabase.addDatabase('QSQLITE')
    db.setDatabaseName('database.db')
    model = QSqlTableModel()
    delrow = -1
    initializeModel(model)
    view1 = createView("Table Model (View 1)", model)
    view1.clicked.connect(findrow)

    dlg = QDialog()
    layout = QVBoxLayout()
    layout.addWidget(view1)

    addBtn = QPushButton("添加一行")
    addBtn.clicked.connect(addrow)
    layout.addWidget(addBtn)

    delBtn = QPushButton("删除一行")
    delBtn.clicked(lambda:
                   model.removeRow(view1.currentIndex().row()))
    layout.addWidget(delBtn)
    dlg.setLayout(layout)
    dlg.setWindowTitle("Database例子")
    dlg.resize(430, 500)
    dlg.show()
    sys.exit(app.exec_())
