from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QAction,QMainWindow,QApplication,qApp
import sqlite3
import sys
import os



class Window(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.con()
        self.init_ui()

    def init_ui(self):

        #WH
        self.setFixedWidth(1360)
        self.setFixedHeight(1000)

        #Widgets
        #Btn
        self.btn_add = QtWidgets.QPushButton(self)
        self.btn_del = QtWidgets.QPushButton(self)
        self.btn_read = QtWidgets.QPushButton(self)

        #Label
        self.lbl_dn = QtWidgets.QLabel(self)
        self.lbl_sn = QtWidgets.QLabel(self)
        self.lbl_q = QtWidgets.QLabel(self)

        #Linedit
        self.le_dn = QtWidgets.QLineEdit(self)
        self.le_sn = QtWidgets.QLineEdit(self)
        self.le_q = QtWidgets.QLineEdit(self)

        #others

        #LE Sent
        self.lbl_dn.setText("Device Name:")
        self.lbl_sn.setText("Serial No:")
        self.lbl_q.setText("Quantity:")

        #BTN Sent
        self.btn_add.setText("Add")
        self.btn_del.setText("Delete")
        self.btn_read.setText("Read")


        #Pos

        self.btn_add.move(105,300)
        self.btn_del.move(225,300)
        self.btn_read.move(345,300)

        self.lbl_dn.move(100,50)
        self.lbl_sn.move(100,100)
        self.lbl_q.move(100,150)

        self.le_dn.move(300,50)
        self.le_sn.move(300,100)
        self.le_q.move(300,150)


        #Btns
        self.btn_add.clicked.connect(lambda: self.add())
        self.btn_del.clicked.connect(lambda: self.dell())
        self.btn_read.clicked.connect(lambda: self.read())


        self.setWindowTitle("Inventory")
        self.show()


    def con(self):
        self.con = sqlite3.connect("database.db")
        self.cursor = self.con.cursor()


        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (device TEXT,model TEXT,q INT)")
        self.con.commit()

    def add(self):
        try:
            dn = self.le_dn.text()
            sn = self.le_sn.text()
            q = int(self.le_q.text())

            #Testing
            self.cursor.execute("SELECT * FROM data where device = ? and model = ?",(dn,sn,))
            cihaz = self.cursor.fetchall()

            if(len(cihaz) == 0):
                #Adding
                self.cursor.execute("Insert Into data Values(?,?,?)",(dn,sn,q,))
                self.con.commit()
            else:
                self.multipl_q()

        except TypeError:
            print("TE")
        except ValueError:
            print("VE")
        except NameError:
            print("NE")
        except SyntaxError:
            print("SE")

    def multipl_q(self):
        try:
            dn = self.le_dn.text()
            sn = self.le_sn.text()
            q = int(self.le_q.text())


            self.cursor.execute("SELECT * FROM data where device = ? and model = ?",(dn,sn,))

            self.num =self.cursor.fetchall()
            self.qq = self.num[0][2]
            print(self.qq)
            self.up()
        except:
            print("Hata")
    def up(self):
        dn = self.le_dn.text()
        sn = self.le_sn.text()
        q = int(self.le_q.text())
        nu = q + self.qq
        self.cursor.execute("UPDATE data SET q = ? WHERE model = ? and device = ?", (nu,sn,dn,))
        self.con.commit()








    def dell(self):

        try:
            dn = self.le_dn.text()
            sn = self.le_sn.text()
            q = int(self.le_q.text())

            self.cursor.execute("SELECT * FROM data where device = ? and model = ?", (dn, sn,))

            self.numm = self.cursor.fetchall()
            self.qqq = self.numm[0][2]
            print(self.qqq)
            self.down()
        except:
            print("Hata")


    def down(self):
        dn = self.le_dn.text()
        sn = self.le_sn.text()
        q = int(self.le_q.text())
        nu =  self.qqq - q
        if(nu < self.qqq):
            self.cursor.execute("UPDATE data SET q = ? WHERE model = ? and device = ?", (nu,sn,dn,))
            self.con.commit()
        elif(nu == self.qqq):
            self.cursor.execute("Delete From data Where device = ? and model = ?",(dn,sn,))
            self.con.commit()

        elif(nu > self.qqq):



    def read(self):
        print("Read func called")


#Others

q = QApplication(sys.argv)

w = Window()

x = sys.exit(q.exec())
