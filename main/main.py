from fnmatch import fnmatch
import sys
import sqlite3
import os
from datetime import date
from docxtpl import DocxTemplate
from pathlib import Path
from string import ascii_letters
from types import NoneType
from typing import List, Union
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QTableWidgetItem, QTableWidget
from PySide6.QtCore import QFile, Qt
from PySide6.QtGui import QPixmap
from PySide6 import QtCore, QtWidgets
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    """Library Management System"""

    BASE_DIR = Path(__file__).parent
    MEDIA_DIR = os.path.join(BASE_DIR, 'photos')
    REZ = QtCore.QSize(200, 266)

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.passUserWindow: bool = False
        self.passLibrarianWindow: bool = False

        self.ui.actionUser.triggered.connect(
            lambda: self.setting(self.ui.WindowUserMain.parent() if self.passUserWindow else self.ui.WindowUserAuthentication.parent()))
        self.ui.actionLibrarian.triggered.connect(
            lambda: self.setting(self.ui.WindowLibrarianMain.parent() if self.passLibrarianWindow else self.ui.WindowLibrarianAuthentication.parent()))
        self.ui.but_Continue.clicked.connect(self.addUserDataBase)
        self.ui.but_Take.clicked.connect(lambda: self.operationTakeBook(src=self.ui.table_Library,
                                                                        target=self.ui.table_UserTake))
        self.ui.but_Give.clicked.connect(lambda: self.operationGiveBook(src=self.ui.table_UserYour,
                                                                        target=self.ui.table_UserTake))
        self.ui.buttonGroup.buttonClicked.connect(self.onClicked)
        self.ui.butLibrarian.clicked.connect(self.passLibrarian)

        self.ui.but_MakeChanges.clicked.connect(self.updateDataBase)

        self.ui.table_UserYour.itemDoubleClicked.connect(lambda: self.operationGiveBook(src=self.ui.table_UserYour,
                                                                                        target=self.ui.table_UserTake))

        self.ui.tableLibLibrary.itemDoubleClicked.connect(lambda: self.operationTakeBook(src=self.ui.tableLibLibrary,
                                                                                         target=self.ui.table_OperationsLibrary))

        self.ui.table_UserBooksLibrary.itemDoubleClicked.connect(lambda: self.operationGiveBook(src=self.ui.table_UserBooksLibrary,
                                                                                                target=self.ui.table_OperationsLibrary))

        self.ui.table_Library.itemClicked.connect(self.showDescription)
        self.ui.table_Library.itemDoubleClicked.connect(lambda: self.operationTakeBook(src=self.ui.table_Library,
                                                                                       target=self.ui.table_UserTake))
        self.ui.table_UserTake.itemDoubleClicked.connect(
            lambda: self.remove_books(object=self.ui.table_UserTake))
        self.ui.table_OperationsLibrary.itemDoubleClicked.connect(
            lambda: self.remove_books(object=self.ui.table_OperationsLibrary)
        )

        self.ui.but_Printout.clicked.connect(self.printout)

        self.ui.table_Library.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.table_UserTake.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.table_UserYour.setEditTriggers(QTableWidget.NoEditTriggers)

        self.ui.tableLibLibrary.setEditTriggers(QTableWidget.NoEditTriggers)
        self.ui.table_OperationsLibrary.setEditTriggers(
            QTableWidget.NoEditTriggers)
        self.ui.table_UserBooksLibrary.setEditTriggers(
            QTableWidget.NoEditTriggers)

        # Clear Window
        self.ui.WindowLibrarianMain.parent().setParent(None)
        self.ui.WindowLibrarianAuthentication.parent().setParent(None)

        self.ui.WindowUserMain.parent().setParent(None)
        self.ui.WindowUserAuthentication.parent().setParent(None)

        self.ui.WindowStart.parent().setParent(None)

        # Setting WindowLibrarianAuthentication
        self.ui.line_Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.line_Login.setPlaceholderText("Login")
        self.ui.line_Password.setPlaceholderText("Password")

        # Setting WindowUserAuthentication
        self.ui.line_FirstName.setPlaceholderText("First Name")
        self.ui.line_LastName.setPlaceholderText("Last Name")
        self.ui.line_MiddleName.setPlaceholderText("Middle Name")
        self.ui.line_AddressCity.setPlaceholderText("City")
        self.ui.line_AddressStreet.setPlaceholderText("Street")
        self.ui.line_Address_ZipCode.setPlaceholderText("Zip-code")
        self.ui.line_Email.setPlaceholderText("E-mail")
        self.ui.line_PhoneNumber.setPlaceholderText(
            "International Phone Number")
        self.ui.line_Day.setPlaceholderText("dd")
        self.ui.line_Day.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.line_Day.setMaxLength(2)
        self.ui.line_Month.setPlaceholderText("mm")
        self.ui.line_Month.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.line_Month.setMaxLength(2)
        self.ui.line_Year.setPlaceholderText("yyyy")
        self.ui.line_Year.setAlignment(QtCore.Qt.AlignCenter)
        self.ui.line_Year.setMaxLength(4)

        # DataBase
        self.connectionDB = sqlite3.connect("library.sqlite3")
        self.cur = self.connectionDB.cursor()

        self.ui.line_FirstNameLib.setPlaceholderText("First Name")
        self.ui.line_LastNameLib.setPlaceholderText("Last name")
        self.ui.line_MiddleNameLib.setPlaceholderText("Midde Name")

        hor_lab_User = [i[1] for i in self.cur.execute(
            "PRAGMA table_info(Book);").fetchall()[:2]] + ["Amount", "Operation"]
        self.ui.table_OperationsLibrary.setColumnCount(len(hor_lab_User))
        self.ui.table_OperationsLibrary.setHorizontalHeaderLabels(hor_lab_User)
        self.ui.table_OperationsLibrary.resizeColumnsToContents()
        self.ui.table_OperationsLibrary.horizontalHeader().setStretchLastSection(True)

        self.ui.but_Enter.clicked.connect(
            lambda: self.update_table_UserBooks(self.ui.table_UserBooksLibrary))
###############################################################
        self.ui.line_FirstName.setText("Egor")
        self.ui.line_LastName.setText("Nedospasov")
        self.ui.line_MiddleName.setText("Dmitrievich")
        self.ui.line_FirstNameLib.setText("Egor")
        self.ui.line_LastNameLib.setText("Nedospasov")
        self.ui.line_MiddleNameLib.setText("Dmitrievich")
###############################################################

        # Start Screen
        self.CURRENT_GRID_LAYOUT = None
        self.setting(self.ui.WindowStart.parent())

    def updateDataBase(self):
        take = []
        give = []
        for row in range(self.ui.table_OperationsLibrary.rowCount()):
            _ = []
            for col in range(self.ui.table_OperationsLibrary.columnCount()):
                item = self.ui.table_OperationsLibrary.item(row, col).text()
                if self.ui.table_OperationsLibrary.item(row, 3).text() == "Give":
                    if item != "Give":
                        _.append(item)
                        var = "Give"
                elif self.ui.table_OperationsLibrary.item(row, 3).text() == "Take":
                    if item != "Take":
                        _.append(item)
                        var = "Take"
            if var == "Give":
                give.append(_)
            elif var == "Take":
                take.append(_)

        fn = self.ui.line_FirstNameLib.text()
        ln = self.ui.line_LastNameLib.text()
        md = self.ui.line_MiddleNameLib.text()
        indexUser = self.cur.execute(
            f'SELECT user_id FROM User WHERE FirstName="{fn}" AND LastName="{ln}" AND MiddleName="{md}"').fetchone()[0]
        res = self.cur.execute(
            f'SELECT * FROM Journal WHERE user_id={indexUser} AND Time_giveback IS NULL').fetchall()

        for record in take:
            amount = self.cur.execute(
                f'SELECT Amount_giveback FROM Journal WHERE user_id={indexUser} AND book_id={int(record[0])} AND Time_giveback IS NULL').fetchone()[0]
            self.cur.execute(
                f'UPDATE Journal SET Amount_giveback={amount+int(record[2])} WHERE user_id={indexUser} AND book_id={int(record[0])} AND Time_giveback IS NULL')
            oper_id = self.cur.execute(
                f'SELECT *  FROM Journal WHERE user_id={indexUser} AND book_id={int(record[0])} and Amount_giveback={amount+int(record[2])}').fetchall()[0]
            if oper_id[4] == oper_id[6]:
                self.cur.execute(
                    f'UPDATE Journal SET Time_giveback=CURRENT_TIMESTAMP WHERE Amount_giveback={amount+int(record[2])} AND user_id={indexUser} AND book_id={int(record[0])}')
            self.connectionDB.commit()

        for record in give:
            self.cur.execute(f"""INSERT INTO Journal(
                librarian_id,
                book_id,
                user_id,
                Amount
            )
            VALUES(
                {self.indexLibrarian},
                {int(record[0])},
                {indexUser},
                {int(record[2])}
                );
""")
            self.connectionDB.commit()

        self.update_table_UserBooks(self.ui.table_UserYour)
        self.update_table_UserBooks(self.ui.table_UserBooksLibrary)
        self.ui.table_OperationsLibrary.clearContents()
        self.ui.table_OperationsLibrary.setRowCount(0)

    def printout(self):
        take = []
        give = []
        for row in range(self.ui.table_UserTake.rowCount()):
            _ = []
            for col in range(self.ui.table_UserTake.columnCount()):
                item = self.ui.table_UserTake.item(row, col).text()
                if self.ui.table_UserTake.item(row, 3).text() == "Give":
                    if item != "Give":
                        _.append(item)
                        var = "Give"
                elif self.ui.table_UserTake.item(row, 3).text() == "Take":
                    if item != "Take":
                        _.append(item)
                        var = "Take"
            if var == "Give":
                give.append(_)
            elif var == "Take":
                take.append(_)
        print(take)
        print(give)

        doc = DocxTemplate("maket.docx")
        context = {
            'Name': f"{self.ui.line_LastName.text()} {self.ui.line_FirstName.text()} {self.ui.line_MiddleName.text()}",
            'Date': str(date.today()),
            'Take': take,
            "Give": give,
        }
        doc.render(context)
        doc.save("temp.docx")

    def remove_books(self, object):
        print(object)
        index = object.selectedIndexes()[0].row()
        print(index)
        object.setItem(index, 2, QTableWidgetItem(
            str(int(object.item(index, 2).text()) - 1)))
        if object.item(index, 2).text() == '0':
            object.removeRow(index)

    def operationGiveBook(self, src: QtWidgets.QTableWidget, target: QtWidgets.QTableWidget) -> None:
        try:
            index = src.selectedIndexes()[0].row()
        except:
            return QMessageBox.information(self, "Information", "Firstly you need to click on book")
        _ = True

        if target == self.ui.table_OperationsLibrary:
            txt = "take"
        else:
            txt = "give"
        index_book = self.cur.execute(
            f"SELECT book_id FROM Journal WHERE operation_id={int(src.item(index, 0).text())}").fetchone()[0]
        name_book = self.cur.execute(
            f"SELECT Name FROM Book WHERE book_id={index_book}").fetchone()[0]

        for row in range(target.rowCount()):
            if target.item(row, 1).text() == name_book and target.item(row, 3).text() == txt.capitalize():
                if int(target.item(row, 2).text()) + int(src.item(row, 6).text()) >= int(src.item(index, 4).text()):
                    return QMessageBox.information(self, "Information", f"You cant {txt} more books")
                target.setItem(row, 2, QTableWidgetItem(
                    str(int(target.item(row, 2).text()) + 1)))
                _ = False
        if _:
            target.setRowCount(target.rowCount() + 1)
            row = target.rowCount()
            target.setItem(row-1, 0, QTableWidgetItem(str(index_book)))
            target.setItem(row-1, 1, QTableWidgetItem(str(name_book)))
            target.setItem(row-1, 2, QTableWidgetItem(str(1)))
            target.setItem(row-1, 3, QTableWidgetItem(txt.capitalize()))

        target.horizontalHeader().setStretchLastSection(False)
        target.resizeColumnsToContents()
        target.horizontalHeader().setStretchLastSection(True)

    def update_table_UserBooks(self, object: QtWidgets.QTableWidget) -> None:
        if object == self.ui.table_UserBooksLibrary:
            fn = self.ui.line_FirstNameLib.text()
            ln = self.ui.line_LastNameLib.text()
            mn = self.ui.line_MiddleNameLib.text()
        elif object == self.ui.table_UserYour:
            fn = self.ui.line_FirstName.text()
            ln = self.ui.line_LastName.text()
            mn = self.ui.line_MiddleName.text()
        index_User = self.cur.execute(
            f'SELECT user_id FROM User WHERE FirstName="{fn}" AND LastName="{ln}" AND MiddleName="{mn}"').fetchall()[0][0]

        res = self.cur.execute(
            f'SELECT * FROM Journal WHERE user_id={index_User} AND Time_giveback IS NULL').fetchall()
        print(res)
        hor_lab = ["operation_id",
                   "User",
                   "Book",
                   "Librarian",
                   "Amount",
                   "Time taked",
                   "Amount give back"
                   ]

        object.clear()
        object.setColumnCount(len(hor_lab))
        object.setRowCount(len(res))
        object.setHorizontalHeaderLabels(hor_lab)

        for i, row in enumerate(res):
            for j, val in enumerate(row[:-1]):
                if j == 1:
                    val = list(self.cur.execute(
                        f"SELECT LastName, FirstName, MiddleName FROM User WHERE user_id={val}").fetchall()[0])
                    val[1] = f"{val[1][0]}."
                    val[2] = f"{val[2][0]}."
                    val = ' '.join(val)
                if j == 2:
                    val = self.cur.execute(
                        f"SELECT Name FROM Book WHERE book_id={val}").fetchall()[0][0]
                if j == 3:
                    val = list(self.cur.execute(
                        f"SELECT LastName, FirstName, MiddleName FROM Librarian WHERE librarian_id={val}").fetchall()[0])
                    val[1] = f"{val[1][0]}."
                    val[2] = f"{val[2][0]}."
                    val = ' '.join(val)
                object.setItem(i, j, QTableWidgetItem(str(val)))

        object.horizontalHeader().setStretchLastSection(False)
        object.resizeColumnsToContents()
        object.horizontalHeader().setStretchLastSection(True)

    def passLibrarian(self):
        login = self.ui.line_Login.text()
        passwd = self.ui.line_Password.text()
        res = self.cur.execute(
            f'SELECT * FROM Librarian WHERE Login="{login}"').fetchall()
        if res != []:
            if res[0][2] == passwd:
                self.passLibrarianWindow = True
                self.indexLibrarian = res[0][0]
                self.setting(self.ui.WindowLibrarianMain.parent())
            else:
                return QMessageBox.information(self, "Information", "Incorrect login or password")
        else:
            return QMessageBox.information(self, "Information", "Incorrect login or password")

    def onClicked(self, object):
        operation = object.text()
        query_text = self.ui.line_Query.text()
        if query_text == "" and operation != "Show all":
            return QMessageBox.information(self, "Information", "Firstly you need to write query")
        if operation == "Show all":
            res = self.cur.execute("SELECT * FROM Book").fetchall()
        else:
            res = self.cur.execute(
                f'SELECT * FROM Book WHERE {operation}="{query_text}"').fetchall()
        self.update_table_Library(res, self.ui.table_Library)

    def operationTakeBook(self, src: QtWidgets.QTableWidget, target: QtWidgets.QTableWidget) -> None:
        try:
            index = src.selectedIndexes()[0].row()
        except:
            return QMessageBox.information(self, "Information", "Firstly you need to click on book")
        
        item_data = self.cur.execute(
            f"SELECT * FROM Book WHERE book_id={index+1}").fetchall()[0]
        _ = True
        if target == self.ui.table_OperationsLibrary:
            txt = "give"
        else:
            txt = "take"

        for row in range(target.rowCount()):
            if target.item(row, 1).text() == item_data[1] and target.item(row, 3).text() == txt.capitalize():
                if int(target.item(row, 2).text()) >= int(src.item(index, 4).text()):
                    return QMessageBox.information(self, "Information", f"You cant {txt} more books")
                target.setItem(row, 2, QTableWidgetItem(
                    str(int(target.item(row, 2).text()) + 1)))
                _ = False
        if _:
            target.setRowCount(target.rowCount() + 1)
            row = target.rowCount()
            for col in range(target.columnCount() - 1):
                target.setItem(
                    row-1, col, QTableWidgetItem(str(item_data[col])))
            target.setItem(row-1, 2, QTableWidgetItem(str(1)))
            target.setItem(row-1, 3, QTableWidgetItem(txt.capitalize()))

        target.horizontalHeader().setStretchLastSection(False)
        target.resizeColumnsToContents()
        target.horizontalHeader().setStretchLastSection(True)

    def showDescription(self):
        index = self.ui.table_Library.selectedIndexes()[0].row()
        name = self.ui.table_Library.item(index, 0).text()
        record = self.cur.execute(
            f'SELECT * FROM Book WHERE Name="{name}"').fetchall()[0]
        self.ui.Label.setText(record[1])
        self.ui.Description.setText(record[-2])
        img = QPixmap(f'{os.path.join(self.MEDIA_DIR, record[-1])}')
        img = img.scaled(self.REZ)
        self.ui.Photo.setPixmap(img)

    @staticmethod
    def createDataBaseTables(cursor: sqlite3.Cursor,
                             connection: sqlite3.Connection) -> NoneType:
        cursor.execute("""CREATE TABLE IF NOT EXISTS User(
                    user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    FirstName VARCHAR(255) NOT NULL,
                    LastName VARCHAR(255) NOT NULL,
                    MiddleName VARCHAR(255) NOT NULL,
                    Email VARCHAR(255) NOT NULL,
                    PhoneNumber VARCHAR(255) NOT NULL,
                    AddressCity TEXT NOT NULL,
                    AddressStreet TEXT NOT NULL,
                    AddressZipCode TEXT NOT NULL,
                    DateOfBirth DATE NOT NULL,
                    TimeJoined DATE NOT NULL,
                    StatusMemberClub BOOLEAN DEFAULT 0,
                    StatusBlackList BOOLEAN DEFAULT 0,
                    Reputation INT DEFAULT 0);
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Book(
                    book_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Name VARCHAR(255) NOT NULL,
                    Genre VARCHAR(255) NOT NULL,
                    Author VARCHAR(255) NOT NULL,
                    DatePublished DATE NOT NULL,
                    Amount INTEGER NOT NULL,
                    StatusLuxery BOOLEAN DEFAULT 0,
                    Description TEXT NOT NULL,
                    Image TEXT NOT NULL DEFAULT "noimage.jpg");
        """)

        cursor.execute("""CREATE TABLE IF NOT EXISTS Librarian(
                    librarian_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    Login VARCHAR(255) NOT NULL,
                    Passwd VARCHAR(255) NOT NULL,
                    FirstName VARCHAR(255) NOT NULL,
                    LastName VARCHAR(255) NOT NULL,
                    MiddleName VARCHAR(255) NOT NULL);
        """)
        cursor.execute("""CREATE TABLE IF NOT EXISTS Journal(
                    operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    librarian_id INTEGER NOT NULL,
                    book_id INTEGER NOT NULL,
                    user_id INTEGER NOT NULL,
                    Amount INTEGER NOT NULL,
                    Time_taked DATE NOT NULL DEFAULT CURRENT_TIMESTAMP,
                    Amount_giveback INTEGER DEFAULT 0,
                    Time_giveback DATE,
                    FOREIGN KEY(user_id) REFERENCES User(user_id),
                    FOREIGN KEY(book_id) REFERENCES Book(book_id),
                    FOREIGN KEY(librarian_id) REFERENCES Librarian(librarian_id));
        """)
        connection.commit()

    def addUserDataBase(self):
        # Create tables if not exists
        self.createDataBaseTables(
            cursor=self.cur, connection=self.connectionDB)
        self.cur.execute(
            f'SELECT * FROM User WHERE FirstName="{self.ui.line_FirstName.text()}" AND LastName="{self.ui.line_LastName.text()}" AND MiddleName="{self.ui.line_MiddleName.text()}"')

        if len(self.cur.fetchall()) == 0:
            user = User()

            if self.ui.line_Email.text() == "" or self.ui.line_PhoneNumber.text() == "" or self.ui.line_AddressCity.text() == "" or self.ui.line_AddressStreet.text() == "" or self.ui.line_Address_ZipCode.text() == "":
                return QMessageBox.information(self, "Information", "You are not in DataBase")

            if user.verifyData(f"{user._FirstName} {user._LastName} {user._MiddleName}",
                               user._AddressZipCode,
                               user._PhoneNumber) == 0:
                return QMessageBox.information(window, "Information", "Check validality of writed text")

            self.cur.execute(f"""INSERT INTO User(
                        FirstName,
                        LastName,
                        MiddleName,
                        Email,
                        PhoneNumber,
                        AddressCity,
                        AddressStreet,
                        AddressZipCode,
                        DateOfBirth,
                        TimeJoined
                    )
                    VALUES(
                        "{user._FirstName}",
                        "{user._LastName}",
                        "{user._MiddleName}",
                        "{user._Email}",
                        "{user._PhoneNumber}",
                        "{user._AddressCity}",
                        "{user._AddressStreet}",
                        "{user._AddressZipCode}",
                        "{user._DateOfBirth}",
                        CURRENT_TIMESTAMP
                    );      
            """)
            self.connectionDB.commit()
        self.passUserWindow = True
        self.update_table_UserBooks(object=self.ui.table_UserYour)
        self.setting(self.ui.WindowUserMain.parent())

    def update_table_Library(self, res, object):
        hor_lab = [i[1] for i in self.cur.execute(
            "PRAGMA table_info(Book);").fetchall()[1:6]]

        object.clear()
        object.setColumnCount(len(hor_lab))
        object.setRowCount(len(res))
        object.setHorizontalHeaderLabels(hor_lab)

        for i, row in enumerate(res):
            for j, val in enumerate(row[1:6]):
                object.setItem(i, j, QTableWidgetItem(str(val)))

        object.horizontalHeader().setStretchLastSection(False)
        object.resizeColumnsToContents()
        object.horizontalHeader().setStretchLastSection(True)

    def setting(self, grid_layout: QWidget) -> NoneType:
        # Main algorithm
        try:
            self.CURRENT_GRID_LAYOUT.close()
            self.CURRENT_GRID_LAYOUT.setParent(None)
        except AttributeError:
            pass
        self.CURRENT_GRID_LAYOUT = grid_layout
        grid_layout.setParent(self.ui.centralwidget)
        grid_layout.setGeometry(10, 10, self.geometry().getRect()[2] - 20,
                                self.geometry().getRect()[3] - 55)
        grid_layout.show()

        # Setting Options of Window
        if grid_layout == self.ui.WindowUserMain.parent():

            self.resize(1560, 900)
            self.ui.line_Query.setPlaceholderText("Query")
            self.ui.radBut_ShowAll.click()

            hor_lab_User = [i[1] for i in self.cur.execute(
                "PRAGMA table_info(Book);").fetchall()[:2]] + ["Amount", "Operation"]
            self.ui.table_UserTake.setColumnCount(len(hor_lab_User))
            self.ui.table_UserTake.setHorizontalHeaderLabels(hor_lab_User)
            self.ui.table_UserTake.resizeColumnsToContents()
            self.ui.table_UserTake.horizontalHeader().setStretchLastSection(True)

        elif grid_layout == self.ui.WindowLibrarianMain.parent():
            self.resize(1560, 900)
            self.update_table_Library(self.cur.execute(
                "SELECT * FROM Book").fetchall(), self.ui.tableLibLibrary)

        else:
            self.resize(960, 680)

    def resizeEvent(self, event):
        self.CURRENT_GRID_LAYOUT.setGeometry(10, 10, self.geometry().getRect()[2] - 20,
                                             self.geometry().getRect()[3] - 55)


class User():
    """User of DataBase"""

    def __init__(self) -> None:
        self._FirstName = window.ui.line_FirstName.text()
        self._LastName = window.ui.line_LastName.text()
        self._MiddleName = window.ui.line_MiddleName.text()
        self._Email = window.ui.line_Email.text()
        self._PhoneNumber = window.ui.line_PhoneNumber.text()
        self._AddressCity = window.ui.line_AddressCity.text()
        self._AddressStreet = window.ui.line_AddressStreet.text()
        self._AddressZipCode = window.ui.line_Address_ZipCode.text()
        self._DateOfBirth = f"{window.ui.line_Year.text()}-{window.ui.line_Month.text()}-{window.ui.line_Day.text()}"

    # Verify

    @staticmethod
    def verifyData(Names: str,
                   AddrZipCode: int,
                   Phone: str):

        # Name
        if type(Names) != str:
            return 0
        arr_names = Names.split()
        if len(arr_names) != 3:
            return 0
        for name in arr_names:
            if len(name) < 1:
                return 0
            if len(name.strip(ascii_letters)) != 0:
                return 0

        # ZipCode
        if not AddrZipCode.isnumeric():
            return 0
        if len(AddrZipCode) != 6:
            return 0

        # Phone
        if Phone[0] != '+':
            return 0
        if not Phone[1:].isnumeric():
            return 0


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.resize(960, 680)
    window.show()

    sys.exit(app.exec())
