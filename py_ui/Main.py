# Form implementation generated from reading ui file 'qt_ui\main.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setWindowModality(QtCore.Qt.WindowModality.NonModal)
        MainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Maximum, QtWidgets.QSizePolicy.Policy.Maximum
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setMinimumSize(QtCore.QSize(711, 526))
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(parent=self.centralwidget)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("")
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.TabPosition.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.TabShape.Rounded)
        self.tabWidget.setObjectName("tabWidget")
        self.tabInstructors = QtWidgets.QWidget()
        self.tabInstructors.setObjectName("tabInstructors")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.tabInstructors)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(parent=self.tabInstructors)
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnInstrAdd = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnInstrAdd.setObjectName("btnInstrAdd")
        self.horizontalLayout.addWidget(self.btnInstrAdd)
        self.btnInstrImport = QtWidgets.QPushButton(parent=self.groupBox)
        self.btnInstrImport.setObjectName("btnInstrImport")
        self.horizontalLayout.addWidget(self.btnInstrImport)
        self.verticalLayout_2.addWidget(self.groupBox)
        self.treeInstr = QtWidgets.QTreeView(parent=self.tabInstructors)
        self.treeInstr.setObjectName("treeInstr")
        self.verticalLayout_2.addWidget(self.treeInstr)
        self.tabWidget.addTab(self.tabInstructors, "")
        self.tabRooms = QtWidgets.QWidget()
        self.tabRooms.setObjectName("tabRooms")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.tabRooms)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.groupBox_2 = QtWidgets.QGroupBox(parent=self.tabRooms)
        self.groupBox_2.setObjectName("groupBox_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.groupBox_2)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.btnRoomAdd = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnRoomAdd.setObjectName("btnRoomAdd")
        self.horizontalLayout_7.addWidget(self.btnRoomAdd)
        self.btnRoomImport = QtWidgets.QPushButton(parent=self.groupBox_2)
        self.btnRoomImport.setObjectName("btnRoomImport")
        self.horizontalLayout_7.addWidget(self.btnRoomImport)
        self.verticalLayout_3.addWidget(self.groupBox_2)
        self.treeRoom = QtWidgets.QTreeView(parent=self.tabRooms)
        self.treeRoom.setObjectName("treeRoom")
        self.verticalLayout_3.addWidget(self.treeRoom)
        self.tabWidget.addTab(self.tabRooms, "")
        self.tabSubjects = QtWidgets.QWidget()
        self.tabSubjects.setObjectName("tabSubjects")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tabSubjects)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.groupBox_3 = QtWidgets.QGroupBox(parent=self.tabSubjects)
        self.groupBox_3.setObjectName("groupBox_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btnSubjAdd = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnSubjAdd.setObjectName("btnSubjAdd")
        self.horizontalLayout_2.addWidget(self.btnSubjAdd)
        self.btnSubjImport = QtWidgets.QPushButton(parent=self.groupBox_3)
        self.btnSubjImport.setObjectName("btnSubjImport")
        self.horizontalLayout_2.addWidget(self.btnSubjImport)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.treeSubj = QtWidgets.QTreeView(parent=self.tabSubjects)
        self.treeSubj.setObjectName("treeSubj")
        self.verticalLayout_4.addWidget(self.treeSubj)
        self.tabWidget.addTab(self.tabSubjects, "")
        self.tabSections = QtWidgets.QWidget()
        self.tabSections.setObjectName("tabSections")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tabSections)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.groupBox_4 = QtWidgets.QGroupBox(parent=self.tabSections)
        self.groupBox_4.setObjectName("groupBox_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.groupBox_4)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.btnSecAdd = QtWidgets.QPushButton(parent=self.groupBox_4)
        self.btnSecAdd.setObjectName("btnSecAdd")
        self.horizontalLayout_3.addWidget(self.btnSecAdd)
        self.verticalLayout_5.addWidget(self.groupBox_4)
        self.treeSec = QtWidgets.QTreeView(parent=self.tabSections)
        self.treeSec.setObjectName("treeSec")
        self.verticalLayout_5.addWidget(self.treeSec)
        self.tabWidget.addTab(self.tabSections, "")
        self.tabScenario = QtWidgets.QWidget()
        sizePolicy = QtWidgets.QSizePolicy(
            QtWidgets.QSizePolicy.Policy.Preferred,
            QtWidgets.QSizePolicy.Policy.Preferred,
        )
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabScenario.sizePolicy().hasHeightForWidth())
        self.tabScenario.setSizePolicy(sizePolicy)
        self.tabScenario.setObjectName("tabScenario")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tabScenario)
        self.verticalLayout_6.setSizeConstraint(
            QtWidgets.QLayout.SizeConstraint.SetDefaultConstraint
        )
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox_5 = QtWidgets.QGroupBox(parent=self.tabScenario)
        self.groupBox_5.setObjectName("groupBox_5")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.groupBox_5)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.btnScenGenerate = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnScenGenerate.setObjectName("btnScenGenerate")
        self.horizontalLayout_4.addWidget(self.btnScenGenerate)
        self.btnScenResult = QtWidgets.QPushButton(parent=self.groupBox_5)
        self.btnScenResult.setObjectName("btnScenResult")
        self.horizontalLayout_4.addWidget(self.btnScenResult)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.groupBox_6 = QtWidgets.QGroupBox(parent=self.tabScenario)
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.groupBox_7 = QtWidgets.QGroupBox(parent=self.groupBox_6)
        self.groupBox_7.setStyleSheet("border: none")
        self.groupBox_7.setTitle("")
        self.groupBox_7.setFlat(False)
        self.groupBox_7.setCheckable(False)
        self.groupBox_7.setChecked(False)
        self.groupBox_7.setObjectName("groupBox_7")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.groupBox_7)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setSpacing(10)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.radioLunchYes = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioLunchYes.setChecked(True)
        self.radioLunchYes.setObjectName("radioLunchYes")
        self.horizontalLayout_5.addWidget(self.radioLunchYes)
        self.radioLunchNo = QtWidgets.QRadioButton(parent=self.groupBox_7)
        self.radioLunchNo.setObjectName("radioLunchNo")
        self.horizontalLayout_5.addWidget(self.radioLunchNo)
        self.gridLayout_2.addWidget(self.groupBox_7, 2, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 2, 0, 1, 1)
        self.label_4 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.timeStarting = QtWidgets.QTimeEdit(parent=self.groupBox_6)
        self.timeStarting.setCurrentSection(QtWidgets.QDateTimeEdit.Section.HourSection)
        self.timeStarting.setTime(QtCore.QTime(8, 0, 0))
        self.timeStarting.setObjectName("timeStarting")
        self.gridLayout_2.addWidget(self.timeStarting, 0, 1, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_2.addItem(spacerItem, 0, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(parent=self.groupBox_6)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 1, 0, 1, 1)
        self.timeEnding = QtWidgets.QTimeEdit(parent=self.groupBox_6)
        self.timeEnding.setCalendarPopup(True)
        self.timeEnding.setTime(QtCore.QTime(18, 0, 0))
        self.timeEnding.setObjectName("timeEnding")
        self.gridLayout_2.addWidget(self.timeEnding, 1, 1, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_6)
        self.groupBox_8 = QtWidgets.QGroupBox(parent=self.tabScenario)
        self.groupBox_8.setObjectName("groupBox_8")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_8)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_20 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_20.setObjectName("label_20")
        self.gridLayout_3.addWidget(self.label_20, 2, 3, 1, 1)
        self.label_21 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_21.setObjectName("label_21")
        self.gridLayout_3.addWidget(self.label_21, 3, 3, 1, 1)
        self.editDev = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editDev.setMaximum(100)
        self.editDev.setProperty("value", 55)
        self.editDev.setObjectName("editDev")
        self.gridLayout_3.addWidget(self.editDev, 3, 5, 1, 1)
        self.editMaxPop = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editMaxPop.setMinimum(50)
        self.editMaxPop.setMaximum(10000)
        self.editMaxPop.setProperty("value", 100)
        self.editMaxPop.setObjectName("editMaxPop")
        self.gridLayout_3.addWidget(self.editMaxPop, 1, 1, 1, 1)
        self.label_12 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 3, 1, 1)
        self.editElite = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editElite.setMaximum(100)
        self.editElite.setProperty("value", 5)
        self.editElite.setObjectName("editElite")
        self.gridLayout_3.addWidget(self.editElite, 2, 5, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_3.addItem(spacerItem1, 0, 7, 1, 1)
        self.editMaxGen = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editMaxGen.setMinimum(50)
        self.editMaxGen.setMaximum(10000)
        self.editMaxGen.setObjectName("editMaxGen")
        self.gridLayout_3.addWidget(self.editMaxGen, 2, 1, 1, 1)
        self.editMaxFit = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editMaxFit.setMaximum(100)
        self.editMaxFit.setProperty("value", 90)
        self.editMaxFit.setObjectName("editMaxFit")
        self.gridLayout_3.addWidget(self.editMaxFit, 1, 5, 1, 1)
        self.label_11 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 3, 1, 1)
        self.label_10 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 3, 0, 1, 1)
        self.label_9 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_9.setObjectName("label_9")
        self.gridLayout_3.addWidget(self.label_9, 2, 0, 1, 1)
        self.editMaxCreation = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editMaxCreation.setMinimum(1500)
        self.editMaxCreation.setMaximum(30000)
        self.editMaxCreation.setObjectName("editMaxCreation")
        self.gridLayout_3.addWidget(self.editMaxCreation, 3, 1, 1, 1)
        self.label_7 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 0, 1, 1)
        self.label_8 = QtWidgets.QLabel(parent=self.groupBox_8)
        self.label_8.setObjectName("label_8")
        self.gridLayout_3.addWidget(self.label_8, 1, 0, 1, 1)
        self.editMinPop = QtWidgets.QSpinBox(parent=self.groupBox_8)
        self.editMinPop.setMinimum(50)
        self.editMinPop.setMaximum(10000)
        self.editMinPop.setObjectName("editMinPop")
        self.gridLayout_3.addWidget(self.editMinPop, 0, 1, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_3.addItem(spacerItem2, 0, 11, 1, 1)
        spacerItem3 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_3.addItem(spacerItem3, 0, 10, 1, 1)
        spacerItem4 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_3.addItem(spacerItem4, 0, 2, 1, 1)
        spacerItem5 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_3.addItem(spacerItem5, 0, 9, 1, 1)
        spacerItem6 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_3.addItem(spacerItem6, 0, 8, 1, 1)
        self.editMut = QtWidgets.QDoubleSpinBox(parent=self.groupBox_8)
        self.editMut.setMaximum(100.0)
        self.editMut.setSingleStep(0.01)
        self.editMut.setProperty("value", 0.08)
        self.editMut.setObjectName("editMut")
        self.gridLayout_3.addWidget(self.editMut, 0, 5, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_8)
        self.groupBox_9 = QtWidgets.QGroupBox(parent=self.tabScenario)
        self.groupBox_9.setObjectName("groupBox_9")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox_9)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_15 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_15.setObjectName("label_15")
        self.gridLayout_4.addWidget(self.label_15, 2, 0, 1, 1)
        self.label_18 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_18.setObjectName("label_18")
        self.gridLayout_4.addWidget(self.label_18, 3, 0, 1, 1)
        self.label_19 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_19.setObjectName("label_19")
        self.gridLayout_4.addWidget(self.label_19, 5, 0, 1, 1)
        self.label_17 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_17.setObjectName("label_17")
        self.gridLayout_4.addWidget(self.label_17, 7, 0, 1, 1)
        self.label_16 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_16.setObjectName("label_16")
        self.gridLayout_4.addWidget(self.label_16, 4, 0, 1, 1)
        self.editSbj = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editSbj.setMaximum(100)
        self.editSbj.setProperty("value", 70)
        self.editSbj.setObjectName("editSbj")
        self.gridLayout_4.addWidget(self.editSbj, 0, 1, 1, 1)
        self.label_13 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_13.setObjectName("label_13")
        self.gridLayout_4.addWidget(self.label_13, 0, 0, 1, 1)
        self.label_14 = QtWidgets.QLabel(parent=self.groupBox_9)
        self.label_14.setObjectName("label_14")
        self.gridLayout_4.addWidget(self.label_14, 1, 0, 1, 1)
        spacerItem7 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Minimum,
        )
        self.gridLayout_4.addItem(spacerItem7, 0, 2, 1, 1)
        self.editLun = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editLun.setMaximum(100)
        self.editLun.setProperty("value", 5)
        self.editLun.setObjectName("editLun")
        self.gridLayout_4.addWidget(self.editLun, 1, 1, 1, 1)
        self.editSec = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editSec.setMaximum(100)
        self.editSec.setProperty("value", 5)
        self.editSec.setObjectName("editSec")
        self.gridLayout_4.addWidget(self.editSec, 2, 1, 1, 1)
        self.editInstrRest = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editInstrRest.setMaximum(100)
        self.editInstrRest.setProperty("value", 5)
        self.editInstrRest.setObjectName("editInstrRest")
        self.gridLayout_4.addWidget(self.editInstrRest, 4, 1, 1, 1)
        self.editInstrLoad = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editInstrLoad.setMaximum(100)
        self.editInstrLoad.setProperty("value", 5)
        self.editInstrLoad.setObjectName("editInstrLoad")
        self.gridLayout_4.addWidget(self.editInstrLoad, 5, 1, 1, 1)
        self.editIdle = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editIdle.setMaximum(100)
        self.editIdle.setProperty("value", 5)
        self.editIdle.setObjectName("editIdle")
        self.gridLayout_4.addWidget(self.editIdle, 3, 1, 1, 1)
        self.editMeet = QtWidgets.QSpinBox(parent=self.groupBox_9)
        self.editMeet.setMaximum(100)
        self.editMeet.setProperty("value", 5)
        self.editMeet.setObjectName("editMeet")
        self.gridLayout_4.addWidget(self.editMeet, 7, 1, 1, 1)
        self.lblTotal = QtWidgets.QLabel(parent=self.groupBox_9)
        self.lblTotal.setObjectName("lblTotal")
        self.gridLayout_4.addWidget(self.lblTotal, 8, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_9)
        spacerItem8 = QtWidgets.QSpacerItem(
            20,
            40,
            QtWidgets.QSizePolicy.Policy.Minimum,
            QtWidgets.QSizePolicy.Policy.Expanding,
        )
        self.verticalLayout_6.addItem(spacerItem8)
        self.tabWidget.addTab(self.tabScenario, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(parent=self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuHelp = QtWidgets.QMenu(parent=self.menubar)
        self.menuHelp.setObjectName("menuHelp")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(parent=MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionOpen = QtGui.QAction(parent=MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionSave = QtGui.QAction(parent=MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionSave_As = QtGui.QAction(parent=MainWindow)
        self.actionSave_As.setObjectName("actionSave_As")
        self.actionSettings = QtGui.QAction(parent=MainWindow)
        self.actionSettings.setObjectName("actionSettings")
        self.actionExit = QtGui.QAction(parent=MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.actionAdd_Instructor = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Instructor.setObjectName("actionAdd_Instructor")
        self.actionView_Instructors = QtGui.QAction(parent=MainWindow)
        self.actionView_Instructors.setObjectName("actionView_Instructors")
        self.actionAdd_Room = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Room.setObjectName("actionAdd_Room")
        self.actionView_Rooms = QtGui.QAction(parent=MainWindow)
        self.actionView_Rooms.setObjectName("actionView_Rooms")
        self.actionAdd_Subject = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Subject.setObjectName("actionAdd_Subject")
        self.actionView_Subjects = QtGui.QAction(parent=MainWindow)
        self.actionView_Subjects.setObjectName("actionView_Subjects")
        self.actionAdd_Sections = QtGui.QAction(parent=MainWindow)
        self.actionAdd_Sections.setObjectName("actionAdd_Sections")
        self.actionView_Sections = QtGui.QAction(parent=MainWindow)
        self.actionView_Sections.setObjectName("actionView_Sections")
        self.actionImport = QtGui.QAction(parent=MainWindow)
        self.actionImport.setObjectName("actionImport")
        self.actionExport = QtGui.QAction(parent=MainWindow)
        self.actionExport.setObjectName("actionExport")
        self.actionView_Results = QtGui.QAction(parent=MainWindow)
        self.actionView_Results.setObjectName("actionView_Results")
        self.actionGenerate = QtGui.QAction(parent=MainWindow)
        self.actionGenerate.setObjectName("actionGenerate")
        self.actionImport_2 = QtGui.QAction(parent=MainWindow)
        self.actionImport_2.setObjectName("actionImport_2")
        self.actionExport_2 = QtGui.QAction(parent=MainWindow)
        self.actionExport_2.setObjectName("actionExport_2")
        self.actionScenario_Summary = QtGui.QAction(parent=MainWindow)
        self.actionScenario_Summary.setObjectName("actionScenario_Summary")
        self.actionGenerate_2 = QtGui.QAction(parent=MainWindow)
        self.actionGenerate_2.setObjectName("actionGenerate_2")
        self.actionView_Results_2 = QtGui.QAction(parent=MainWindow)
        self.actionView_Results_2.setObjectName("actionView_Results_2")
        self.actionInstructions = QtGui.QAction(parent=MainWindow)
        self.actionInstructions.setObjectName("actionInstructions")
        self.actionAbout = QtGui.QAction(parent=MainWindow)
        self.actionAbout.setObjectName("actionAbout")
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_As)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSettings)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menuHelp.addAction(self.actionInstructions)
        self.menuHelp.addAction(self.actionAbout)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(4)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Timetable Scheduler"))
        self.tabInstructors.setWhatsThis(
            _translate("MainWindow", "<html><head/><body><p><br/></p></body></html>")
        )
        self.groupBox.setTitle(_translate("MainWindow", "Operation"))
        self.btnInstrAdd.setText(_translate("MainWindow", "Add Instructor"))
        self.btnInstrImport.setText(_translate("MainWindow", "Import from CSV"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabInstructors),
            _translate("MainWindow", "Instructors"),
        )
        self.groupBox_2.setTitle(_translate("MainWindow", "Operation"))
        self.btnRoomAdd.setText(_translate("MainWindow", "Add Room"))
        self.btnRoomImport.setText(_translate("MainWindow", "Import from CSV"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabRooms), _translate("MainWindow", "Rooms")
        )
        self.groupBox_3.setTitle(_translate("MainWindow", "Operation"))
        self.btnSubjAdd.setText(_translate("MainWindow", "Add Subject"))
        self.btnSubjImport.setText(_translate("MainWindow", "Import from CSV"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabSubjects),
            _translate("MainWindow", "Subjects"),
        )
        self.groupBox_4.setTitle(_translate("MainWindow", "Operation"))
        self.btnSecAdd.setText(_translate("MainWindow", "Add Section"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabSections),
            _translate("MainWindow", "Sections"),
        )
        self.groupBox_5.setTitle(_translate("MainWindow", "Operation"))
        self.btnScenGenerate.setText(_translate("MainWindow", "Generate"))
        self.btnScenResult.setText(_translate("MainWindow", "View Results"))
        self.groupBox_6.setTitle(_translate("MainWindow", "School Operation Settings"))
        self.radioLunchYes.setText(_translate("MainWindow", "Yes"))
        self.radioLunchNo.setText(_translate("MainWindow", "No"))
        self.label_6.setToolTip(
            _translate("MainWindow", "Assess for lunch break for sections.")
        )
        self.label_6.setText(_translate("MainWindow", "Lunchbreak"))
        self.label_4.setToolTip(
            _translate("MainWindow", "The opening time of the school.")
        )
        self.label_4.setText(_translate("MainWindow", "Operation Starting Time"))
        self.timeStarting.setDisplayFormat(_translate("MainWindow", "h AP"))
        self.label_5.setToolTip(
            _translate("MainWindow", "The closing time of the school.")
        )
        self.label_5.setText(_translate("MainWindow", "Operation Ending Time"))
        self.timeEnding.setDisplayFormat(_translate("MainWindow", "h AP"))
        self.groupBox_8.setTitle(_translate("MainWindow", "Genetic Algorithm Settings"))
        self.label_20.setToolTip(
            _translate(
                "MainWindow", "The percent of population that would belong to elite."
            )
        )
        self.label_20.setText(_translate("MainWindow", "Elite Population"))
        self.label_21.setToolTip(
            _translate("MainWindow", "The maximum control of a sigma.")
        )
        self.label_21.setText(_translate("MainWindow", "Deviation Tolerance"))
        self.label_12.setToolTip(
            _translate(
                "MainWindow", "Stops the generation when a chromosome meets this."
            )
        )
        self.label_12.setText(_translate("MainWindow", "Maximum Fitness"))
        self.label_11.setToolTip(
            _translate(
                "MainWindow",
                "<html><head/><body><p>Triggers mutation rate change when the difference of average fitness falls to the specificied level.</p></body></html>",
            )
        )
        self.label_11.setText(
            _translate("MainWindow", "Mutation Rate Adjustment Trigger")
        )
        self.label_10.setToolTip(
            _translate(
                "MainWindow", "Maximum attempts for creating a valid chromosome."
            )
        )
        self.label_10.setText(_translate("MainWindow", "Maximum Creation Attempts"))
        self.label_9.setToolTip(
            _translate(
                "MainWindow",
                "Maximum amount of generations to be performed on solution generation.",
            )
        )
        self.label_9.setText(_translate("MainWindow", "Maximum Generations"))
        self.label_7.setToolTip(
            _translate(
                "MainWindow",
                "Starting point and lowest population count of the genetic algorithm.",
            )
        )
        self.label_7.setText(_translate("MainWindow", "Minimum Population Count"))
        self.label_8.setToolTip(
            _translate(
                "MainWindow", "Highest population count of the genetic algorithm."
            )
        )
        self.label_8.setText(_translate("MainWindow", "Maximum Population Count"))
        self.groupBox_9.setTitle(_translate("MainWindow", "Evaluation Matrix"))
        self.label_15.setToolTip(
            _translate(
                "MainWindow",
                "The weight of section rest (There must be a rest for every consecutive 3 hours of session)",
            )
        )
        self.label_15.setText(_translate("MainWindow", "Section Rest"))
        self.label_18.setToolTip(
            _translate("MainWindow", "The weight of sections having less idle time.")
        )
        self.label_18.setText(_translate("MainWindow", "Section Idle Time"))
        self.label_19.setToolTip(
            _translate(
                "MainWindow",
                "The weight of having all instructors have normalized teaching load.",
            )
        )
        self.label_19.setText(_translate("MainWindow", "Instructor Load Balance"))
        self.label_17.setToolTip(
            _translate(
                "MainWindow",
                "The weight of having correct meeting patterns for subject placement.",
            )
        )
        self.label_17.setText(_translate("MainWindow", "Meeting Pattern"))
        self.label_16.setToolTip(
            _translate(
                "MainWindow",
                "The weight of instructor rest (There must be a rest for every consecutive 3 hours of session)",
            )
        )
        self.label_16.setText(_translate("MainWindow", "Instructor Rest"))
        self.label_13.setToolTip(
            _translate("MainWindow", "The weight of having all subjects placed.")
        )
        self.label_13.setText(_translate("MainWindow", "Subject Placement"))
        self.label_14.setToolTip(
            _translate("MainWindow", "The weight of having a lunch break.")
        )
        self.label_14.setText(_translate("MainWindow", "Lunch Break"))
        self.lblTotal.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(
            self.tabWidget.indexOf(self.tabScenario),
            _translate("MainWindow", "Settings"),
        )
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuHelp.setTitle(_translate("MainWindow", "Help"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionSave_As.setText(_translate("MainWindow", "Save As"))
        self.actionSettings.setText(_translate("MainWindow", "Settings"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionAdd_Instructor.setText(_translate("MainWindow", "Add Instructor"))
        self.actionView_Instructors.setText(
            _translate("MainWindow", "View Instructors")
        )
        self.actionAdd_Room.setText(_translate("MainWindow", "Add Room"))
        self.actionView_Rooms.setText(_translate("MainWindow", "View Rooms"))
        self.actionAdd_Subject.setText(_translate("MainWindow", "Add Subject"))
        self.actionView_Subjects.setText(_translate("MainWindow", "View Subjects"))
        self.actionAdd_Sections.setText(_translate("MainWindow", "Add Sections"))
        self.actionView_Sections.setText(_translate("MainWindow", "View Sections"))
        self.actionImport.setText(_translate("MainWindow", "Import"))
        self.actionExport.setText(_translate("MainWindow", "Export"))
        self.actionView_Results.setText(_translate("MainWindow", "View Results"))
        self.actionGenerate.setText(_translate("MainWindow", "Generate"))
        self.actionImport_2.setText(_translate("MainWindow", "Import"))
        self.actionExport_2.setText(_translate("MainWindow", "Export"))
        self.actionScenario_Summary.setText(
            _translate("MainWindow", "Scenario Summary")
        )
        self.actionGenerate_2.setText(_translate("MainWindow", "Generate"))
        self.actionView_Results_2.setText(_translate("MainWindow", "View Results"))
        self.actionInstructions.setText(_translate("MainWindow", "Instructions"))
        self.actionAbout.setText(_translate("MainWindow", "About"))
