# Form implementation generated from reading ui file 'f:\Code\projects\python_projects\GeneticAlgorithmUniversityClassScheduler\qt_ui\instructor.ui'
#
# Created by: PyQt6 UI code generator 6.7.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(605, 320))
        Dialog.setMaximumSize(QtCore.QSize(605, 320))
        Dialog.setFocusPolicy(QtCore.Qt.FocusPolicy.NoFocus)
        Dialog.setModal(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetMinimumSize
        )
        self.gridLayout.setObjectName("gridLayout")
        self.lblName = QtWidgets.QLabel(parent=Dialog)
        self.lblName.setObjectName("lblName")
        self.gridLayout.addWidget(self.lblName, 0, 0, 1, 1)
        self.lineEditName = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditName.setObjectName("lineEditName")
        self.gridLayout.addWidget(self.lineEditName, 0, 1, 1, 1)
        self.lblHours = QtWidgets.QLabel(parent=Dialog)
        self.lblHours.setObjectName("lblHours")
        self.gridLayout.addWidget(self.lblHours, 0, 2, 1, 1)
        self.lineEditHours = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEditHours.setObjectName("lineEditHours")
        self.gridLayout.addWidget(self.lineEditHours, 0, 3, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.tableSchedule = QtWidgets.QTableView(parent=Dialog)
        self.tableSchedule.setObjectName("tableSchedule")
        self.verticalLayout.addWidget(self.tableSchedule)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnFinish = QtWidgets.QPushButton(parent=Dialog)
        self.btnFinish.setObjectName("btnFinish")
        self.horizontalLayout.addWidget(self.btnFinish)
        self.btnCancel = QtWidgets.QPushButton(parent=Dialog)
        self.btnCancel.setObjectName("btnCancel")
        self.horizontalLayout.addWidget(self.btnCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Instructor"))
        self.lblName.setText(_translate("Dialog", "Name"))
        self.lblHours.setText(_translate("Dialog", "Available Hours"))
        self.btnFinish.setText(_translate("Dialog", "Finish"))
        self.btnCancel.setText(_translate("Dialog", "Cancel"))
