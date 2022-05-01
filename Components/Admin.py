import json

import pandas as pd
from PyQt5 import QtCore, QtGui, QtWidgets

from Components import Login, StatMenu
from utils import routes
from utils.Helpers.AdminHelper import *
from utils.Helpers.GeneralHelpers import fillTableData


class Ui_AdminPage(object):
    def retranslateUi(self, AdminPage):
        _translate = QtCore.QCoreApplication.translate
        AdminPage.setWindowTitle(_translate("AdminPage", "Admins Page"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.rawData), _translate("AdminPage", "Raw Data"))
        self.bakeBtn.setText(_translate("AdminPage", "Bake Rules"))
        self.includeLbl.setText(_translate("AdminPage", "Include special keywords:"))
        self.excludeLbl_2.setText(_translate("AdminPage", "Exclude special keywords:"))
        self.impactLabel.setText(_translate("AdminPage", "Potential Impact values:"))
        self.integrity.setText(_translate("AdminPage", "Integrity"))
        self.confidentiality.setText(_translate("AdminPage", "Confidentiality"))
        self.availability.setText(_translate("AdminPage", "Availability"))
        self.sortByDate.setText(_translate("AdminPage", "Sort by date"))
        self.wsmSort.setText(_translate("AdminPage", "WSM rating"))

        self.label.setText(_translate("AdminPage", "0%"))
        self.label_2.setText(_translate("AdminPage", "0%"))
        self.label_3.setText(_translate("AdminPage", "0%"))
        self.label_4.setText(_translate("AdminPage", "0%"))

        self.label_5.setText(_translate("AdminPage", "Severity"))
        self.label_6.setText(_translate("AdminPage", "Security Grade"))
        self.label_7.setText(_translate("AdminPage", "Security Score"))
        self.label_8.setText(_translate("AdminPage", "Discoverability"))
        self.mostImpact.setText(_translate("AdminPage", "Most issues impact"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.analyst1), _translate("AdminPage", "Yaniv"))
        self.excludeLbl_3.setText(_translate("AdminPage", "Exclude special keywords:"))
        self.wsmSort_2.setText(_translate("AdminPage", "WSM rating"))

        self.label_25.setText(_translate("AdminPage", "0%"))
        self.label_26.setText(_translate("AdminPage", "0%"))
        self.label_27.setText(_translate("AdminPage", "0%"))
        self.label_28.setText(_translate("AdminPage", "0%"))

        self.label_29.setText(_translate("AdminPage", "Severity"))
        self.label_30.setText(_translate("AdminPage", "Security Grade"))
        self.label_31.setText(_translate("AdminPage", "Security Score"))
        self.label_32.setText(_translate("AdminPage", "Discoverability"))
        self.impactLabel_4.setText(_translate("AdminPage", "Potential Impact values:"))
        self.integrity_2.setText(_translate("AdminPage", "Integrity"))
        self.confidentiality_2.setText(_translate("AdminPage", "Confidentiality"))
        self.availability_2.setText(_translate("AdminPage", "Availability"))
        self.sortByDate_2.setText(_translate("AdminPage", "Sort by date"))
        self.bakeBtn_2.setText(_translate("AdminPage", "Bake Rules"))
        self.mostImpact_2.setText(_translate("AdminPage", "Most issues impact"))
        self.includeLbl_2.setText(_translate("AdminPage", "Include special keywords:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.analyst2), _translate("AdminPage", "Itay"))
        self.excludeLbl_4.setText(_translate("AdminPage", "Exclude special keywords:"))
        self.wsmSort_3.setText(_translate("AdminPage", "WSM rating"))

        self.label_33.setText(_translate("AdminPage", "0%"))
        self.label_34.setText(_translate("AdminPage", "0%"))
        self.label_35.setText(_translate("AdminPage", "0%"))
        self.label_36.setText(_translate("AdminPage", "0%"))

        self.label_37.setText(_translate("AdminPage", "Severity"))
        self.label_38.setText(_translate("AdminPage", "Security Grade"))
        self.label_39.setText(_translate("AdminPage", "Security Score"))
        self.label_40.setText(_translate("AdminPage", "Discoverability"))
        self.impactLabel_5.setText(_translate("AdminPage", "Potential Impact values:"))
        self.integrity_3.setText(_translate("AdminPage", "Integrity"))
        self.confidentiality_3.setText(_translate("AdminPage", "Confidentiality"))
        self.availability_3.setText(_translate("AdminPage", "Availability"))
        self.sortByDate_3.setText(_translate("AdminPage", "Sort by date"))
        self.bakeBtn_3.setText(_translate("AdminPage", "Bake Rules"))
        self.mostImpact_3.setText(_translate("AdminPage", "Most issues impact"))
        self.includeLbl_3.setText(_translate("AdminPage", "Include special keywords:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.analyst3), _translate("AdminPage", "Ben"))
        self.excludeLbl_5.setText(_translate("AdminPage", "Exclude special keywords:"))
        self.wsmSort_4.setText(_translate("AdminPage", "WSM rating"))

        self.label_41.setText(_translate("AdminPage", "0%"))
        self.label_42.setText(_translate("AdminPage", "0%"))
        self.label_43.setText(_translate("AdminPage", "0%"))
        self.label_44.setText(_translate("AdminPage", "0%"))

        self.label_45.setText(_translate("AdminPage", "Severity"))
        self.label_46.setText(_translate("AdminPage", "Security Grade"))
        self.label_47.setText(_translate("AdminPage", "Security Score"))
        self.label_48.setText(_translate("AdminPage", "Discoverability"))
        self.impactLabel_6.setText(_translate("AdminPage", "Potential Impact values:"))
        self.integrity_4.setText(_translate("AdminPage", "Integrity"))
        self.confidentiality_4.setText(_translate("AdminPage", "Confidentiality"))
        self.availability_4.setText(_translate("AdminPage", "Availability"))
        self.sortByDate_4.setText(_translate("AdminPage", "Sort by date"))
        self.bakeBtn_4.setText(_translate("AdminPage", "Bake Rules"))
        self.mostImpact_4.setText(_translate("AdminPage", "Most issues impact"))
        self.includeLbl_4.setText(_translate("AdminPage", "Include special keywords:"))
        self.toolBox.setItemText(self.toolBox.indexOf(self.analyst4), _translate("AdminPage", "Roni"))
        self.ExitBtn.setText(_translate("AdminPage", "Exit"))
        self.importCsvBtn.setText(_translate("AdminPage", "  Import CSV"))
        self.statisticsBtn.setText(_translate("AdminPage", "Statistics"))

    def fileDialog(self):
        self.csvTuple = QtWidgets.QFileDialog.getOpenFileName(None, "File Explorer", "",
                                                              "All Files (*);;Python Files (*.py);;Text Files (*.txt)",
                                                              )
        if not self.csvTuple[0]:
            return

        self.CSV = self.csvTuple[0]
        with open(routes.latestCsvFile) as latestCsv:
            uploadedCsv = json.load(latestCsv)

        uploadedCsv["latest_upload"] = self.CSV
        uploadedCsv["previous_uploads"].append(self.CSV)
        with open(routes.latestCsvFile, 'w') as latestCsv:
            json.dump(uploadedCsv, latestCsv, indent=2)

        relevant_columns = {
            1: 'Severity',
            2: 'Asset Security Grade',
            3: 'Asset Security Score',
            4: 'Asset Discoverability',
            5: 'Asset Attractiveness',
            6: 'Asset Type',
            7: 'Potential Impact',
            8: 'Asset First Seen',
            9: 'Description'
        }

        raw_df = pd.read_csv(self.CSV, low_memory=False)
        filtered_df = raw_df[relevant_columns.values()]
        fillTableData(filtered_df, self.rawDataTableWidget)

    def initAllRules(self):
        with open(routes.rulesFile) as file:
            rulesDB = json.load(file)

        self.sortByDate.setChecked(rulesDB['analyst_1']['date'])
        self.wsmSort.setChecked(rulesDB['analyst_1']['wsm']['state'])
        self.mostImpact.setChecked(rulesDB['analyst_1']['most_impact'])
        self.confidentiality.setChecked(rulesDB['analyst_1']['confidentiality'])
        self.integrity.setChecked(rulesDB['analyst_1']['integrity'])
        self.availability.setChecked(rulesDB['analyst_1']['availability'])
        self.includeKeywords.setText(rulesDB['analyst_1']['include'])
        self.excludeKeywords.setText(rulesDB['analyst_1']['exclude'])

        self.sortByDate_2.setChecked(rulesDB['analyst_2']['date'])
        self.mostImpact_2.setChecked(rulesDB['analyst_2']['most_impact'])
        self.wsmSort_2.setChecked(rulesDB['analyst_2']['wsm']['state'])
        self.confidentiality_2.setChecked(rulesDB['analyst_2']['confidentiality'])
        self.integrity_2.setChecked(rulesDB['analyst_2']['integrity'])
        self.availability_2.setChecked(rulesDB['analyst_2']['availability'])
        self.includeKeywords_2.setText(rulesDB['analyst_2']['include'])
        self.excludeKeywords_2.setText(rulesDB['analyst_2']['exclude'])

        self.sortByDate_3.setChecked(rulesDB['analyst_3']['date'])
        self.mostImpact_3.setChecked(rulesDB['analyst_4']['most_impact'])
        self.wsmSort_3.setChecked(rulesDB['analyst_3']['wsm']['state'])
        self.confidentiality_3.setChecked(rulesDB['analyst_3']['confidentiality'])
        self.integrity_3.setChecked(rulesDB['analyst_3']['integrity'])
        self.availability_3.setChecked(rulesDB['analyst_3']['availability'])
        self.includeKeywords_3.setText(rulesDB['analyst_3']['include'])
        self.excludeKeywords_3.setText(rulesDB['analyst_3']['exclude'])

        self.sortByDate_4.setChecked(rulesDB['analyst_4']['date'])
        self.mostImpact_4.setChecked(rulesDB['analyst_4']['most_impact'])
        self.wsmSort_4.setChecked(rulesDB['analyst_4']['wsm']['state'])
        self.confidentiality_4.setChecked(rulesDB['analyst_4']['confidentiality'])
        self.integrity_4.setChecked(rulesDB['analyst_4']['integrity'])
        self.availability_4.setChecked(rulesDB['analyst_4']['availability'])
        self.includeKeywords_4.setText(rulesDB['analyst_4']['include'])
        self.excludeKeywords_4.setText(rulesDB['analyst_4']['exclude'])

        # -----------Init Vertical bars-------------------------
        self.vSlider1_Analyst1.setEnabled(rulesDB['analyst_1']['wsm']['state'])
        self.vSlider2_Analyst1.setEnabled(rulesDB['analyst_1']['wsm']['state'])
        self.vSlider3_Analyst1.setEnabled(rulesDB['analyst_1']['wsm']['state'])
        self.vSlider4_Analyst1.setEnabled(rulesDB['analyst_1']['wsm']['state'])
        self.vSlider1_Analyst1.setValue(rulesDB['analyst_1']['wsm']['slider1'])
        self.vSlider2_Analyst1.setValue(rulesDB['analyst_1']['wsm']['slider2'])
        self.vSlider3_Analyst1.setValue(rulesDB['analyst_1']['wsm']['slider3'])
        self.vSlider4_Analyst1.setValue(rulesDB['analyst_1']['wsm']['slider4'])

        self.vSlider1_Analyst2.setEnabled(rulesDB['analyst_2']['wsm']['state'])
        self.vSlider2_Analyst2.setEnabled(rulesDB['analyst_2']['wsm']['state'])
        self.vSlider3_Analyst2.setEnabled(rulesDB['analyst_2']['wsm']['state'])
        self.vSlider4_Analyst2.setEnabled(rulesDB['analyst_2']['wsm']['state'])
        self.vSlider1_Analyst2.setValue(rulesDB['analyst_2']['wsm']['slider1'])
        self.vSlider2_Analyst2.setValue(rulesDB['analyst_2']['wsm']['slider2'])
        self.vSlider3_Analyst2.setValue(rulesDB['analyst_2']['wsm']['slider3'])
        self.vSlider4_Analyst2.setValue(rulesDB['analyst_2']['wsm']['slider4'])

        self.vSlider1_Analyst3.setEnabled(rulesDB['analyst_3']['wsm']['state'])
        self.vSlider2_Analyst3.setEnabled(rulesDB['analyst_3']['wsm']['state'])
        self.vSlider3_Analyst3.setEnabled(rulesDB['analyst_3']['wsm']['state'])
        self.vSlider4_Analyst3.setEnabled(rulesDB['analyst_3']['wsm']['state'])
        self.vSlider1_Analyst3.setValue(rulesDB['analyst_3']['wsm']['slider1'])
        self.vSlider2_Analyst3.setValue(rulesDB['analyst_3']['wsm']['slider2'])
        self.vSlider3_Analyst3.setValue(rulesDB['analyst_3']['wsm']['slider3'])
        self.vSlider4_Analyst3.setValue(rulesDB['analyst_3']['wsm']['slider4'])

        self.vSlider1_Analyst4.setEnabled(rulesDB['analyst_4']['wsm']['state'])
        self.vSlider2_Analyst4.setEnabled(rulesDB['analyst_4']['wsm']['state'])
        self.vSlider3_Analyst4.setEnabled(rulesDB['analyst_4']['wsm']['state'])
        self.vSlider4_Analyst4.setEnabled(rulesDB['analyst_4']['wsm']['state'])
        self.vSlider1_Analyst4.setValue(rulesDB['analyst_4']['wsm']['slider1'])
        self.vSlider2_Analyst4.setValue(rulesDB['analyst_4']['wsm']['slider2'])
        self.vSlider3_Analyst4.setValue(rulesDB['analyst_4']['wsm']['slider3'])
        self.vSlider4_Analyst4.setValue(rulesDB['analyst_4']['wsm']['slider4'])

    def openLogin(self, AdminPage):
        self.LoginWindow = QtWidgets.QMainWindow()
        self.ui = Login.UiLogIn()
        self.ui.setupUi(self.LoginWindow)
        self.LoginWindow.show()
        AdminPage.close()

    def openStatisticsMenu(self):
        self.statisticsMenu = QtWidgets.QMainWindow()
        self.ui = StatMenu.Ui_StatisticsMenu()
        self.ui.setupUi(self.statisticsMenu)
        self.statisticsMenu.show()

    def setupUi(self, AdminPage):
        AdminPage.setObjectName("AdminPage")
        AdminPage.setEnabled(True)
        AdminPage.resize(1024, 715)
        AdminPage.setWindowIcon(QtGui.QIcon(routes.sceLogo))
        self.centralwidget = QtWidgets.QWidget(AdminPage)
        self.centralwidget.setObjectName("centralwidget")

        # -------------- Fonts ---------------------
        self.font = QtGui.QFont()
        self.font.setPointSize(10)
        self.font.setBold(True)
        self.font.setItalic(False)
        self.font.setUnderline(False)
        self.font.setWeight(75)
        self.font.setStrikeOut(False)
        self.font.setKerning(True)
        self.font.setStyleStrategy(QtGui.QFont.PreferDefault)

        self.precentFont = QtGui.QFont()
        self.precentFont.setBold(True)
        self.precentFont.setWeight(75)

        # ------- The tool box that gathers all analysts and raw data ----------
        self.toolBox = QtWidgets.QToolBox(self.centralwidget)
        self.toolBox.setGeometry(QtCore.QRect(10, 90, 1001, 561))
        self.toolBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.toolBox.setFrameShape(QtWidgets.QFrame.Box)
        self.toolBox.setFrameShadow(QtWidgets.QFrame.Raised)
        self.toolBox.setLineWidth(1)
        self.toolBox.setMidLineWidth(1)
        self.toolBox.setObjectName("toolBox")

        # --------- Raw Data Table-------------------
        self.rawData = QtWidgets.QWidget()
        self.rawData.setGeometry(QtCore.QRect(0, 0, 995, 400))
        self.rawData.setObjectName("rawData")
        self.rawDataTableWidget = QtWidgets.QTableWidget(self.rawData)
        self.rawDataTableWidget.setGeometry(QtCore.QRect(0, 0, 1001, 401))
        self.rawDataTableWidget.setObjectName("rawDataTableWidget")
        self.rawDataTableWidget.setColumnCount(0)
        self.rawDataTableWidget.setRowCount(0)
        self.toolBox.addItem(self.rawData, "")

        # ----------- Buttons ------------------------
        self.ExitBtn = QtWidgets.QPushButton(self.centralwidget)
        self.ExitBtn.setGeometry(QtCore.QRect(890, 660, 121, 31))
        self.ExitBtn.setObjectName("ExitBtn")
        self.ExitBtn.clicked.connect(lambda: self.openLogin(AdminPage))

        self.importCsvBtn = QtWidgets.QCommandLinkButton(self.centralwidget)
        self.importCsvBtn.setGeometry(QtCore.QRect(420, 10, 191, 71))
        self.importCsvBtn.setIcon(QtGui.QIcon(routes.importCsvIcon))
        self.importCsvBtn.setIconSize(QtCore.QSize(45, 80))
        self.importCsvBtn.setCheckable(False)
        self.importCsvBtn.setObjectName("importCsvBtn")
        self.importCsvBtn.clicked.connect(self.fileDialog)

        self.statisticsBtn = QtWidgets.QPushButton(self.centralwidget)
        self.statisticsBtn.setGeometry(QtCore.QRect(10, 660, 121, 31))
        self.statisticsBtn.setObjectName("statisticsBtn")
        self.statisticsBtn.clicked.connect(self.openStatisticsMenu)

        # -----------------Analyst1-------------------
        self.analyst1 = QtWidgets.QWidget()
        self.analyst1.setGeometry(QtCore.QRect(0, 0, 995, 400))
        self.analyst1.setObjectName("analyst1")

        self.excludeKeywords = QtWidgets.QLineEdit(self.analyst1)
        self.excludeKeywords.setGeometry(QtCore.QRect(10, 310, 421, 22))
        self.excludeKeywords.setObjectName("excludeKeywords")

        self.includeKeywords = QtWidgets.QLineEdit(self.analyst1)
        self.includeKeywords.setGeometry(QtCore.QRect(10, 260, 421, 22))
        self.includeKeywords.setObjectName("includeKeywords")

        self.includeLbl = QtWidgets.QLabel(self.analyst1)
        self.includeLbl.setGeometry(QtCore.QRect(10, 240, 201, 20))
        self.includeLbl.setObjectName("includeLbl")

        self.excludeLbl_2 = QtWidgets.QLabel(self.analyst1)
        self.excludeLbl_2.setGeometry(QtCore.QRect(10, 290, 181, 16))
        self.excludeLbl_2.setObjectName("excludeLbl_2")

        self.potentialImpactFrame = QtWidgets.QFrame(self.analyst1)
        self.potentialImpactFrame.setGeometry(QtCore.QRect(10, 10, 180, 81))
        self.potentialImpactFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.potentialImpactFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.potentialImpactFrame.setLineWidth(1)
        self.potentialImpactFrame.setObjectName("potentialImpactFrame")

        self.impactLabel = QtWidgets.QLabel(self.potentialImpactFrame)
        self.impactLabel.setGeometry(QtCore.QRect(10, 0, 161, 21))
        self.impactLabel.setStyleSheet("text-decoration: underline;\n"
                                       "font: 75 9pt \"MS Shell Dlg 2\";")
        self.impactLabel.setObjectName("impactLabel")

        self.integrity = QtWidgets.QCheckBox(self.potentialImpactFrame)
        self.integrity.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.integrity.setObjectName("integrity")

        self.confidentiality = QtWidgets.QCheckBox(self.potentialImpactFrame)
        self.confidentiality.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.confidentiality.setObjectName("confitendiality")

        self.availability = QtWidgets.QCheckBox(self.potentialImpactFrame)
        self.availability.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.availability.setObjectName("availability")

        self.sortByDate = QtWidgets.QCheckBox(self.analyst1)
        self.sortByDate.setGeometry(QtCore.QRect(230, 20, 111, 20))
        self.sortByDate.setObjectName("sortByDate")

        self.wsmFrame = QtWidgets.QFrame(self.analyst1)
        self.wsmFrame.setGeometry(QtCore.QRect(440, 10, 541, 321))
        self.wsmFrame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.wsmFrame.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wsmFrame.setLineWidth(1)
        self.wsmFrame.setObjectName("wsmFrame")

        self.wsmSort = QtWidgets.QCheckBox(self.wsmFrame)
        self.wsmSort.setGeometry(QtCore.QRect(220, 10, 111, 21))
        self.wsmSort.setObjectName("wsmSort")
        self.wsmSort.clicked.connect(
            lambda: changeVerticalStatus(self.wsmSort.isChecked(), self.vSlider1_Analyst1, self.vSlider2_Analyst1,
                                         self.vSlider3_Analyst1, self.vSlider4_Analyst1, self.label, self.label_2,
                                         self.label_3, self.label_4))

        self.vSlider1_Analyst1 = QtWidgets.QSlider(self.wsmFrame)
        self.vSlider1_Analyst1.setGeometry(QtCore.QRect(60, 80, 21, 221))
        self.vSlider1_Analyst1.setAutoFillBackground(True)
        self.vSlider1_Analyst1.setMaximum(4)
        self.vSlider1_Analyst1.setPageStep(1)
        self.vSlider1_Analyst1.setTracking(True)
        self.vSlider1_Analyst1.setOrientation(QtCore.Qt.Vertical)
        self.vSlider1_Analyst1.setInvertedControls(False)
        self.vSlider1_Analyst1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider1_Analyst1.setTickInterval(1)
        self.vSlider1_Analyst1.setObjectName("verticalSlider")
        self.vSlider1_Analyst1.valueChanged.connect(lambda: slide_it(self.label, self.vSlider1_Analyst1.value()))

        self.vSlider2_Analyst1 = QtWidgets.QSlider(self.wsmFrame)
        self.vSlider2_Analyst1.setGeometry(QtCore.QRect(190, 80, 21, 221))
        self.vSlider2_Analyst1.setAutoFillBackground(True)
        self.vSlider2_Analyst1.setMaximum(4)
        self.vSlider2_Analyst1.setPageStep(1)
        self.vSlider2_Analyst1.setTracking(True)
        self.vSlider2_Analyst1.setOrientation(QtCore.Qt.Vertical)
        self.vSlider2_Analyst1.setInvertedControls(False)
        self.vSlider2_Analyst1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider2_Analyst1.setTickInterval(1)
        self.vSlider2_Analyst1.setObjectName("verticalSlider_2")
        self.vSlider2_Analyst1.valueChanged.connect(lambda: slide_it(self.label_2, self.vSlider2_Analyst1.value()))

        self.vSlider3_Analyst1 = QtWidgets.QSlider(self.wsmFrame)
        self.vSlider3_Analyst1.setGeometry(QtCore.QRect(320, 80, 21, 221))
        self.vSlider3_Analyst1.setAutoFillBackground(True)
        self.vSlider3_Analyst1.setMaximum(4)
        self.vSlider3_Analyst1.setPageStep(1)
        self.vSlider3_Analyst1.setTracking(True)
        self.vSlider3_Analyst1.setOrientation(QtCore.Qt.Vertical)
        self.vSlider3_Analyst1.setInvertedControls(False)
        self.vSlider3_Analyst1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider3_Analyst1.setTickInterval(1)
        self.vSlider3_Analyst1.setObjectName("verticalSlider_3")
        self.vSlider3_Analyst1.valueChanged.connect(lambda: slide_it(self.label_3, self.vSlider3_Analyst1.value()))

        self.vSlider4_Analyst1 = QtWidgets.QSlider(self.wsmFrame)
        self.vSlider4_Analyst1.setGeometry(QtCore.QRect(450, 80, 21, 221))
        self.vSlider4_Analyst1.setAutoFillBackground(True)
        self.vSlider4_Analyst1.setMaximum(4)
        self.vSlider4_Analyst1.setPageStep(1)
        self.vSlider4_Analyst1.setTracking(True)
        self.vSlider4_Analyst1.setOrientation(QtCore.Qt.Vertical)
        self.vSlider4_Analyst1.setInvertedControls(False)
        self.vSlider4_Analyst1.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider4_Analyst1.setTickInterval(1)
        self.vSlider4_Analyst1.setObjectName("verticalSlider_4")
        self.vSlider4_Analyst1.valueChanged.connect(lambda: slide_it(self.label_4, self.vSlider4_Analyst1.value()))

        self.label = QtWidgets.QLabel(self.wsmFrame)
        self.label.setGeometry(QtCore.QRect(100, 170, 53, 21))
        self.label.setFont(self.font)
        self.label.setObjectName("label")

        self.label_2 = QtWidgets.QLabel(self.wsmFrame)
        self.label_2.setGeometry(QtCore.QRect(230, 170, 53, 21))
        self.label_2.setFont(self.font)
        self.label_2.setObjectName("label_2")

        self.label_3 = QtWidgets.QLabel(self.wsmFrame)
        self.label_3.setGeometry(QtCore.QRect(360, 170, 61, 21))
        self.label_3.setFont(self.font)
        self.label_3.setObjectName("label_3")

        self.label_4 = QtWidgets.QLabel(self.wsmFrame)
        self.label_4.setGeometry(QtCore.QRect(480, 170, 61, 21))
        self.label_4.setFont(self.font)
        self.label_4.setObjectName("label_4")

        self.label_5 = QtWidgets.QLabel(self.wsmFrame)
        self.label_5.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.label_5.setFont(self.precentFont)
        self.label_5.setObjectName("label_5")

        self.label_6 = QtWidgets.QLabel(self.wsmFrame)
        self.label_6.setGeometry(QtCore.QRect(150, 50, 101, 21))
        self.label_6.setFont(self.precentFont)
        self.label_6.setObjectName("label_6")

        self.label_7 = QtWidgets.QLabel(self.wsmFrame)
        self.label_7.setGeometry(QtCore.QRect(280, 50, 101, 21))
        self.label_7.setFont(self.precentFont)
        self.label_7.setObjectName("label_7")

        self.label_8 = QtWidgets.QLabel(self.wsmFrame)
        self.label_8.setGeometry(QtCore.QRect(410, 50, 101, 21))
        self.label_8.setFont(self.precentFont)
        self.label_8.setObjectName("label_8")

        self.mostImpact = QtWidgets.QCheckBox(self.analyst1)
        self.mostImpact.setGeometry(QtCore.QRect(230, 50, 141, 20))
        self.mostImpact.setObjectName("mostImpact")

        self.bakeBtn = QtWidgets.QPushButton(self.analyst1)
        self.bakeBtn.setGeometry(QtCore.QRect(440, 350, 111, 41))
        self.bakeBtn.setObjectName("bakeBtn")
        self.bakeBtn.clicked.connect(
            lambda: writeAnalystRules('analyst_1', self.sortByDate, self.wsmSort, self.vSlider1_Analyst1,
                                      self.vSlider2_Analyst1, self.vSlider3_Analyst1, self.vSlider4_Analyst1,
                                      self.confidentiality,
                                      self.integrity,
                                      self.availability, self.mostImpact, self.includeKeywords, self.excludeKeywords))

        self.toolBox.addItem(self.analyst1, "")

        # ------------------- Analyst2 -----------------------------
        self.analyst2 = QtWidgets.QWidget()
        self.analyst2.setGeometry(QtCore.QRect(0, 0, 995, 400))
        self.analyst2.setObjectName("analyst2")

        self.excludeLbl_3 = QtWidgets.QLabel(self.analyst2)
        self.excludeLbl_3.setGeometry(QtCore.QRect(10, 290, 181, 16))
        self.excludeLbl_3.setObjectName("excludeLbl_3")

        self.includeKeywords_2 = QtWidgets.QLineEdit(self.analyst2)
        self.includeKeywords_2.setGeometry(QtCore.QRect(10, 260, 421, 22))
        self.includeKeywords_2.setObjectName("includeKeywords_2")

        self.wsmFrame_2 = QtWidgets.QFrame(self.analyst2)
        self.wsmFrame_2.setGeometry(QtCore.QRect(440, 10, 541, 321))
        self.wsmFrame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.wsmFrame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wsmFrame_2.setLineWidth(1)
        self.wsmFrame_2.setObjectName("wsmFrame_2")

        self.wsmSort_2 = QtWidgets.QCheckBox(self.wsmFrame_2)
        self.wsmSort_2.setGeometry(QtCore.QRect(220, 10, 111, 21))
        self.wsmSort_2.setObjectName("wsmSort_4")
        self.wsmSort_2.clicked.connect(
            lambda: changeVerticalStatus(self.wsmSort_2.isChecked(), self.vSlider1_Analyst2, self.vSlider2_Analyst2,
                                         self.vSlider4_Analyst2, self.vSlider3_Analyst2, self.label_25, self.label_26,
                                         self.label_27, self.label_28))

        self.vSlider1_Analyst2 = QtWidgets.QSlider(self.wsmFrame_2)
        self.vSlider1_Analyst2.setGeometry(QtCore.QRect(60, 80, 21, 221))
        self.vSlider1_Analyst2.setAutoFillBackground(True)
        self.vSlider1_Analyst2.setMaximum(4)
        self.vSlider1_Analyst2.setPageStep(1)
        self.vSlider1_Analyst2.setTracking(True)
        self.vSlider1_Analyst2.setOrientation(QtCore.Qt.Vertical)
        self.vSlider1_Analyst2.setInvertedControls(False)
        self.vSlider1_Analyst2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider1_Analyst2.setTickInterval(1)
        self.vSlider1_Analyst2.setObjectName("verticalSlider_13")
        self.vSlider1_Analyst2.valueChanged.connect(lambda: slide_it(self.label_25, self.vSlider1_Analyst2.value()))

        self.vSlider2_Analyst2 = QtWidgets.QSlider(self.wsmFrame_2)
        self.vSlider2_Analyst2.setGeometry(QtCore.QRect(190, 80, 21, 221))
        self.vSlider2_Analyst2.setAutoFillBackground(True)
        self.vSlider2_Analyst2.setMaximum(4)
        self.vSlider2_Analyst2.setPageStep(1)
        self.vSlider2_Analyst2.setTracking(True)
        self.vSlider2_Analyst2.setOrientation(QtCore.Qt.Vertical)
        self.vSlider2_Analyst2.setInvertedControls(False)
        self.vSlider2_Analyst2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider2_Analyst2.setTickInterval(1)
        self.vSlider2_Analyst2.setObjectName("verticalSlider_16")
        self.vSlider2_Analyst2.valueChanged.connect(lambda: slide_it(self.label_26, self.vSlider2_Analyst2.value()))

        self.vSlider3_Analyst2 = QtWidgets.QSlider(self.wsmFrame_2)
        self.vSlider3_Analyst2.setGeometry(QtCore.QRect(320, 80, 21, 221))
        self.vSlider3_Analyst2.setAutoFillBackground(True)
        self.vSlider3_Analyst2.setMaximum(4)
        self.vSlider3_Analyst2.setPageStep(1)
        self.vSlider3_Analyst2.setTracking(True)
        self.vSlider3_Analyst2.setOrientation(QtCore.Qt.Vertical)
        self.vSlider3_Analyst2.setInvertedControls(False)
        self.vSlider3_Analyst2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider3_Analyst2.setTickInterval(1)
        self.vSlider3_Analyst2.setObjectName("verticalSlider_16")
        self.vSlider3_Analyst2.valueChanged.connect(lambda: slide_it(self.label_27, self.vSlider3_Analyst2.value()))

        self.vSlider4_Analyst2 = QtWidgets.QSlider(self.wsmFrame_2)
        self.vSlider4_Analyst2.setGeometry(QtCore.QRect(450, 80, 21, 221))
        self.vSlider4_Analyst2.setAutoFillBackground(True)
        self.vSlider4_Analyst2.setMaximum(4)
        self.vSlider4_Analyst2.setPageStep(1)
        self.vSlider4_Analyst2.setTracking(True)
        self.vSlider4_Analyst2.setOrientation(QtCore.Qt.Vertical)
        self.vSlider4_Analyst2.setInvertedControls(False)
        self.vSlider4_Analyst2.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider4_Analyst2.setTickInterval(1)
        self.vSlider4_Analyst2.setObjectName("verticalSlider_15")
        self.vSlider4_Analyst2.valueChanged.connect(lambda: slide_it(self.label_28, self.vSlider4_Analyst2.value()))

        self.label_25 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_25.setGeometry(QtCore.QRect(100, 170, 53, 21))
        self.label_25.setFont(self.font)
        self.label_25.setObjectName("label_25")

        self.label_26 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_26.setGeometry(QtCore.QRect(230, 170, 53, 21))
        self.label_26.setFont(self.font)
        self.label_26.setObjectName("label_26")

        self.label_27 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_27.setGeometry(QtCore.QRect(360, 170, 61, 21))
        self.label_27.setFont(self.font)
        self.label_27.setObjectName("label_27")

        self.label_28 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_28.setGeometry(QtCore.QRect(480, 170, 61, 21))
        self.label_28.setFont(self.font)
        self.label_28.setObjectName("label_28")

        self.label_29 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_29.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.label_29.setFont(self.precentFont)
        self.label_29.setObjectName("label_29")

        self.label_30 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_30.setGeometry(QtCore.QRect(150, 50, 101, 21))
        self.label_30.setFont(self.precentFont)
        self.label_30.setObjectName("label_30")

        self.label_31 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_31.setGeometry(QtCore.QRect(280, 50, 101, 21))
        self.label_31.setFont(self.precentFont)
        self.label_31.setObjectName("label_31")

        self.label_32 = QtWidgets.QLabel(self.wsmFrame_2)
        self.label_32.setGeometry(QtCore.QRect(410, 50, 101, 21))
        self.label_32.setFont(self.precentFont)
        self.label_32.setObjectName("label_32")

        self.potentialImpactFrame_2 = QtWidgets.QFrame(self.analyst2)
        self.potentialImpactFrame_2.setGeometry(QtCore.QRect(10, 10, 180, 81))
        self.potentialImpactFrame_2.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.potentialImpactFrame_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.potentialImpactFrame_2.setLineWidth(1)
        self.potentialImpactFrame_2.setObjectName("potentialImpactFrame_2")

        self.impactLabel_4 = QtWidgets.QLabel(self.potentialImpactFrame_2)
        self.impactLabel_4.setGeometry(QtCore.QRect(10, 0, 161, 21))
        self.impactLabel_4.setStyleSheet("text-decoration: underline;\n"
                                         "font: 75 9pt \"MS Shell Dlg 2\";")
        self.impactLabel_4.setObjectName("impactLabel_4")

        self.integrity_2 = QtWidgets.QCheckBox(self.potentialImpactFrame_2)
        self.integrity_2.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.integrity_2.setObjectName("integrity_4")

        self.confidentiality_2 = QtWidgets.QCheckBox(self.potentialImpactFrame_2)
        self.confidentiality_2.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.confidentiality_2.setObjectName("confidentiality_2")

        self.availability_2 = QtWidgets.QCheckBox(self.potentialImpactFrame_2)
        self.availability_2.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.availability_2.setObjectName("availability_4")

        self.sortByDate_2 = QtWidgets.QCheckBox(self.analyst2)
        self.sortByDate_2.setGeometry(QtCore.QRect(230, 20, 111, 20))
        self.sortByDate_2.setObjectName("sortByDate_2")

        self.excludeKeywords_2 = QtWidgets.QLineEdit(self.analyst2)
        self.excludeKeywords_2.setGeometry(QtCore.QRect(10, 310, 421, 22))
        self.excludeKeywords_2.setObjectName("excludeKeywords_2")

        self.mostImpact_2 = QtWidgets.QCheckBox(self.analyst2)
        self.mostImpact_2.setGeometry(QtCore.QRect(230, 50, 141, 20))
        self.mostImpact_2.setObjectName("mostImpact_2")

        self.bakeBtn_2 = QtWidgets.QPushButton(self.analyst2)
        self.bakeBtn_2.setGeometry(QtCore.QRect(440, 350, 111, 41))
        self.bakeBtn_2.setObjectName("bakeBtn_2")
        self.bakeBtn_2.clicked.connect(
            lambda: writeAnalystRules('analyst_2', self.sortByDate_2, self.wsmSort_2, self.vSlider1_Analyst2,
                                      self.vSlider2_Analyst2, self.vSlider3_Analyst2, self.vSlider4_Analyst2,
                                      self.confidentiality_2,
                                      self.integrity_2,
                                      self.availability_2, self.mostImpact_2, self.includeKeywords_2,
                                      self.excludeKeywords_2))

        self.includeLbl_2 = QtWidgets.QLabel(self.analyst2)
        self.includeLbl_2.setGeometry(QtCore.QRect(10, 240, 201, 20))
        self.includeLbl_2.setObjectName("includeLbl_2")
        self.toolBox.addItem(self.analyst2, "")

        # ------------------- Analyst3 -----------------------------
        self.analyst3 = QtWidgets.QWidget()
        self.analyst3.setGeometry(QtCore.QRect(0, 0, 995, 400))
        self.analyst3.setObjectName("analyst3")

        self.excludeLbl_4 = QtWidgets.QLabel(self.analyst3)
        self.excludeLbl_4.setGeometry(QtCore.QRect(10, 290, 181, 16))
        self.excludeLbl_4.setObjectName("excludeLbl_4")

        self.includeKeywords_3 = QtWidgets.QLineEdit(self.analyst3)
        self.includeKeywords_3.setGeometry(QtCore.QRect(10, 260, 421, 22))
        self.includeKeywords_3.setObjectName("includeKeywords_3")

        self.wsmFrame_3 = QtWidgets.QFrame(self.analyst3)
        self.wsmFrame_3.setGeometry(QtCore.QRect(440, 10, 541, 321))
        self.wsmFrame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.wsmFrame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wsmFrame_3.setLineWidth(1)
        self.wsmFrame_3.setObjectName("wsmFrame_3")

        self.wsmSort_3 = QtWidgets.QCheckBox(self.wsmFrame_3)
        self.wsmSort_3.setGeometry(QtCore.QRect(220, 10, 111, 21))
        self.wsmSort_3.setObjectName("wsmSort_3")
        self.wsmSort_3.clicked.connect(
            lambda: changeVerticalStatus(self.wsmSort_3.isChecked(), self.vSlider1_Analyst3, self.vSlider2_Analyst3,
                                         self.vSlider3_Analyst3, self.vSlider4_Analyst3, self.label_33, self.label_34,
                                         self.label_35, self.label_36))

        self.vSlider1_Analyst3 = QtWidgets.QSlider(self.wsmFrame_3)
        self.vSlider1_Analyst3.setGeometry(QtCore.QRect(60, 80, 21, 221))
        self.vSlider1_Analyst3.setAutoFillBackground(True)
        self.vSlider1_Analyst3.setMaximum(4)
        self.vSlider1_Analyst3.setPageStep(1)
        self.vSlider1_Analyst3.setTracking(True)
        self.vSlider1_Analyst3.setOrientation(QtCore.Qt.Vertical)
        self.vSlider1_Analyst3.setInvertedControls(False)
        self.vSlider1_Analyst3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider1_Analyst3.setTickInterval(1)
        self.vSlider1_Analyst3.setObjectName("verticalSlider_17")
        self.vSlider1_Analyst3.valueChanged.connect(lambda: slide_it(self.label_33, self.vSlider1_Analyst3.value()))

        self.vSlider2_Analyst3 = QtWidgets.QSlider(self.wsmFrame_3)
        self.vSlider2_Analyst3.setGeometry(QtCore.QRect(190, 80, 21, 221))
        self.vSlider2_Analyst3.setAutoFillBackground(True)
        self.vSlider2_Analyst3.setMaximum(4)
        self.vSlider2_Analyst3.setPageStep(1)
        self.vSlider2_Analyst3.setTracking(True)
        self.vSlider2_Analyst3.setOrientation(QtCore.Qt.Vertical)
        self.vSlider2_Analyst3.setInvertedControls(False)
        self.vSlider2_Analyst3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider2_Analyst3.setTickInterval(1)
        self.vSlider2_Analyst3.setObjectName("verticalSlider_19")
        self.vSlider2_Analyst3.valueChanged.connect(lambda: slide_it(self.label_34, self.vSlider2_Analyst3.value()))

        self.vSlider3_Analyst3 = QtWidgets.QSlider(self.wsmFrame_3)
        self.vSlider3_Analyst3.setGeometry(QtCore.QRect(320, 80, 21, 221))
        self.vSlider3_Analyst3.setAutoFillBackground(True)
        self.vSlider3_Analyst3.setMaximum(4)
        self.vSlider3_Analyst3.setPageStep(1)
        self.vSlider3_Analyst3.setTracking(True)
        self.vSlider3_Analyst3.setOrientation(QtCore.Qt.Vertical)
        self.vSlider3_Analyst3.setInvertedControls(False)
        self.vSlider3_Analyst3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider3_Analyst3.setTickInterval(1)
        self.vSlider3_Analyst3.setObjectName("verticalSlider_20")
        self.vSlider3_Analyst3.valueChanged.connect(lambda: slide_it(self.label_35, self.vSlider3_Analyst3.value()))

        self.vSlider4_Analyst3 = QtWidgets.QSlider(self.wsmFrame_3)
        self.vSlider4_Analyst3.setGeometry(QtCore.QRect(450, 80, 21, 221))
        self.vSlider4_Analyst3.setAutoFillBackground(True)
        self.vSlider4_Analyst3.setMaximum(4)
        self.vSlider4_Analyst3.setPageStep(1)
        self.vSlider4_Analyst3.setTracking(True)
        self.vSlider4_Analyst3.setOrientation(QtCore.Qt.Vertical)
        self.vSlider4_Analyst3.setInvertedControls(False)
        self.vSlider4_Analyst3.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider4_Analyst3.setTickInterval(1)
        self.vSlider4_Analyst3.setObjectName("verticalSlider_18")
        self.vSlider4_Analyst3.valueChanged.connect(lambda: slide_it(self.label_36, self.vSlider4_Analyst3.value()))

        self.label_33 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_33.setGeometry(QtCore.QRect(100, 170, 53, 21))
        self.label_33.setFont(self.font)
        self.label_33.setObjectName("label_33")

        self.label_34 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_34.setGeometry(QtCore.QRect(230, 170, 53, 21))
        self.label_34.setFont(self.font)
        self.label_34.setObjectName("label_34")

        self.label_35 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_35.setGeometry(QtCore.QRect(360, 170, 61, 21))
        self.label_35.setFont(self.font)
        self.label_35.setObjectName("label_35")

        self.label_36 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_36.setGeometry(QtCore.QRect(480, 170, 61, 21))
        self.label_36.setFont(self.font)
        self.label_36.setObjectName("label_36")

        self.label_37 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_37.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.label_37.setFont(self.precentFont)
        self.label_37.setObjectName("label_37")

        self.label_38 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_38.setGeometry(QtCore.QRect(150, 50, 101, 21))
        self.label_38.setFont(self.precentFont)
        self.label_38.setObjectName("label_38")

        self.label_39 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_39.setGeometry(QtCore.QRect(280, 50, 101, 21))
        self.label_39.setFont(self.precentFont)
        self.label_39.setObjectName("label_39")

        self.label_40 = QtWidgets.QLabel(self.wsmFrame_3)
        self.label_40.setGeometry(QtCore.QRect(410, 50, 101, 21))
        self.label_40.setFont(self.precentFont)
        self.label_40.setObjectName("label_40")

        self.potentialImpactFrame_3 = QtWidgets.QFrame(self.analyst3)
        self.potentialImpactFrame_3.setGeometry(QtCore.QRect(10, 10, 180, 81))
        self.potentialImpactFrame_3.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.potentialImpactFrame_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.potentialImpactFrame_3.setLineWidth(1)
        self.potentialImpactFrame_3.setObjectName("potentialImpactFrame_3")

        self.impactLabel_5 = QtWidgets.QLabel(self.potentialImpactFrame_3)
        self.impactLabel_5.setGeometry(QtCore.QRect(10, 0, 161, 21))
        self.impactLabel_5.setStyleSheet("text-decoration: underline;\n"
                                         "font: 75 9pt \"MS Shell Dlg 2\";")
        self.impactLabel_5.setObjectName("impactLabel_5")

        self.integrity_3 = QtWidgets.QCheckBox(self.potentialImpactFrame_3)
        self.integrity_3.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.integrity_3.setObjectName("integrity_5")

        self.confidentiality_3 = QtWidgets.QCheckBox(self.potentialImpactFrame_3)
        self.confidentiality_3.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.confidentiality_3.setObjectName("confidentiality_3")

        self.availability_3 = QtWidgets.QCheckBox(self.potentialImpactFrame_3)
        self.availability_3.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.availability_3.setObjectName("availability_3")

        self.sortByDate_3 = QtWidgets.QCheckBox(self.analyst3)
        self.sortByDate_3.setGeometry(QtCore.QRect(230, 20, 111, 20))
        self.sortByDate_3.setObjectName("sortByDate_3")

        self.excludeKeywords_3 = QtWidgets.QLineEdit(self.analyst3)
        self.excludeKeywords_3.setGeometry(QtCore.QRect(10, 310, 421, 22))
        self.excludeKeywords_3.setObjectName("excludeKeywords_3")

        self.mostImpact_3 = QtWidgets.QCheckBox(self.analyst3)
        self.mostImpact_3.setGeometry(QtCore.QRect(230, 50, 141, 20))
        self.mostImpact_3.setObjectName("mostImpact_3")

        self.bakeBtn_3 = QtWidgets.QPushButton(self.analyst3)
        self.bakeBtn_3.setGeometry(QtCore.QRect(440, 350, 111, 41))
        self.bakeBtn_3.setObjectName("bakeBtn_3")
        self.bakeBtn_3.clicked.connect(
            lambda: writeAnalystRules('analyst_3', self.sortByDate_3, self.wsmSort_3, self.vSlider1_Analyst3,
                                      self.vSlider2_Analyst3, self.vSlider3_Analyst3, self.vSlider4_Analyst3,
                                      self.confidentiality_3,
                                      self.integrity_3,
                                      self.availability_3, self.mostImpact_3, self.includeKeywords_3,
                                      self.excludeKeywords_3))

        self.includeLbl_3 = QtWidgets.QLabel(self.analyst3)
        self.includeLbl_3.setGeometry(QtCore.QRect(10, 240, 201, 20))
        self.includeLbl_3.setObjectName("includeLbl_3")
        self.toolBox.addItem(self.analyst3, "")

        # ------------------- Analyst4 -----------------------------
        self.analyst4 = QtWidgets.QWidget()
        self.analyst4.setGeometry(QtCore.QRect(0, 0, 995, 400))
        self.analyst4.setObjectName("analyst4")

        self.excludeLbl_5 = QtWidgets.QLabel(self.analyst4)
        self.excludeLbl_5.setGeometry(QtCore.QRect(10, 290, 181, 16))
        self.excludeLbl_5.setObjectName("excludeLbl_5")

        self.wsmFrame_4 = QtWidgets.QFrame(self.analyst4)
        self.wsmFrame_4.setGeometry(QtCore.QRect(440, 10, 541, 321))
        self.wsmFrame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.wsmFrame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.wsmFrame_4.setLineWidth(1)
        self.wsmFrame_4.setObjectName("wsmFrame_4")

        self.wsmSort_4 = QtWidgets.QCheckBox(self.wsmFrame_4)
        self.wsmSort_4.setGeometry(QtCore.QRect(220, 10, 111, 21))
        self.wsmSort_4.setObjectName("wsmSort_4")
        self.wsmSort_4.clicked.connect(
            lambda: changeVerticalStatus(self.wsmSort_4.isChecked(), self.vSlider1_Analyst4, self.vSlider2_Analyst4,
                                         self.vSlider3_Analyst4, self.vSlider4_Analyst4, self.label_41, self.label_42,
                                         self.label_43, self.label_44))

        self.vSlider1_Analyst4 = QtWidgets.QSlider(self.wsmFrame_4)
        self.vSlider1_Analyst4.setGeometry(QtCore.QRect(60, 80, 21, 221))
        self.vSlider1_Analyst4.setAutoFillBackground(True)
        self.vSlider1_Analyst4.setMaximum(4)
        self.vSlider1_Analyst4.setPageStep(1)
        self.vSlider1_Analyst4.setTracking(True)
        self.vSlider1_Analyst4.setOrientation(QtCore.Qt.Vertical)
        self.vSlider1_Analyst4.setInvertedControls(False)
        self.vSlider1_Analyst4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider1_Analyst4.setTickInterval(1)
        self.vSlider1_Analyst4.setObjectName("verticalSlider_21")
        self.vSlider1_Analyst4.valueChanged.connect(lambda: slide_it(self.label_41, self.vSlider1_Analyst4.value()))

        self.vSlider2_Analyst4 = QtWidgets.QSlider(self.wsmFrame_4)
        self.vSlider2_Analyst4.setGeometry(QtCore.QRect(190, 80, 21, 221))
        self.vSlider2_Analyst4.setAutoFillBackground(True)
        self.vSlider2_Analyst4.setMaximum(4)
        self.vSlider2_Analyst4.setPageStep(1)
        self.vSlider2_Analyst4.setTracking(True)
        self.vSlider2_Analyst4.setOrientation(QtCore.Qt.Vertical)
        self.vSlider2_Analyst4.setInvertedControls(False)
        self.vSlider2_Analyst4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider2_Analyst4.setTickInterval(1)
        self.vSlider2_Analyst4.setObjectName("verticalSlider_24")
        self.vSlider2_Analyst4.valueChanged.connect(lambda: slide_it(self.label_42, self.vSlider2_Analyst4.value()))

        self.vSlider3_Analyst4 = QtWidgets.QSlider(self.wsmFrame_4)
        self.vSlider3_Analyst4.setGeometry(QtCore.QRect(320, 80, 21, 221))
        self.vSlider3_Analyst4.setAutoFillBackground(True)
        self.vSlider3_Analyst4.setMaximum(4)
        self.vSlider3_Analyst4.setPageStep(1)
        self.vSlider3_Analyst4.setTracking(True)
        self.vSlider3_Analyst4.setOrientation(QtCore.Qt.Vertical)
        self.vSlider3_Analyst4.setInvertedControls(False)
        self.vSlider3_Analyst4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider3_Analyst4.setTickInterval(1)
        self.vSlider3_Analyst4.setObjectName("verticalSlider_22")
        self.vSlider3_Analyst4.valueChanged.connect(lambda: slide_it(self.label_43, self.vSlider3_Analyst4.value()))

        self.vSlider4_Analyst4 = QtWidgets.QSlider(self.wsmFrame_4)
        self.vSlider4_Analyst4.setGeometry(QtCore.QRect(450, 80, 21, 221))
        self.vSlider4_Analyst4.setAutoFillBackground(True)
        self.vSlider4_Analyst4.setMaximum(4)
        self.vSlider4_Analyst4.setPageStep(1)
        self.vSlider4_Analyst4.setTracking(True)
        self.vSlider4_Analyst4.setOrientation(QtCore.Qt.Vertical)
        self.vSlider4_Analyst4.setInvertedControls(False)
        self.vSlider4_Analyst4.setTickPosition(QtWidgets.QSlider.TicksBelow)
        self.vSlider4_Analyst4.setTickInterval(1)
        self.vSlider4_Analyst4.setObjectName("verticalSlider_23")
        self.vSlider4_Analyst4.valueChanged.connect(lambda: slide_it(self.label_44, self.vSlider4_Analyst4.value()))

        self.label_41 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_41.setGeometry(QtCore.QRect(100, 170, 53, 21))
        self.label_41.setFont(self.font)
        self.label_41.setObjectName("label_41")

        self.label_42 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_42.setGeometry(QtCore.QRect(230, 170, 53, 21))
        self.label_42.setFont(self.font)
        self.label_42.setObjectName("label_42")

        self.label_43 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_43.setGeometry(QtCore.QRect(360, 170, 61, 21))
        self.label_43.setFont(self.font)
        self.label_43.setObjectName("label_43")

        self.label_44 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_44.setGeometry(QtCore.QRect(480, 170, 61, 21))
        self.label_44.setFont(self.font)
        self.label_44.setObjectName("label_44")

        self.label_45 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_45.setGeometry(QtCore.QRect(40, 50, 61, 21))
        self.label_45.setFont(self.precentFont)
        self.label_45.setObjectName("label_45")

        self.label_46 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_46.setGeometry(QtCore.QRect(150, 50, 101, 21))
        self.label_46.setFont(self.precentFont)
        self.label_46.setObjectName("label_46")

        self.label_47 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_47.setGeometry(QtCore.QRect(280, 50, 101, 21))
        self.label_47.setFont(self.precentFont)
        self.label_47.setObjectName("label_47")

        self.label_48 = QtWidgets.QLabel(self.wsmFrame_4)
        self.label_48.setGeometry(QtCore.QRect(410, 50, 101, 21))
        self.label_48.setFont(self.precentFont)
        self.label_48.setObjectName("label_48")

        self.potentialImpactFrame_4 = QtWidgets.QFrame(self.analyst4)
        self.potentialImpactFrame_4.setGeometry(QtCore.QRect(10, 10, 180, 81))
        self.potentialImpactFrame_4.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.potentialImpactFrame_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.potentialImpactFrame_4.setLineWidth(1)
        self.potentialImpactFrame_4.setObjectName("potentialImpactFrame_4")

        self.impactLabel_6 = QtWidgets.QLabel(self.potentialImpactFrame_4)
        self.impactLabel_6.setGeometry(QtCore.QRect(10, 0, 161, 21))
        self.impactLabel_6.setStyleSheet("text-decoration: underline;\n"
                                         "font: 75 9pt \"MS Shell Dlg 2\";")
        self.impactLabel_6.setObjectName("impactLabel_6")

        self.integrity_4 = QtWidgets.QCheckBox(self.potentialImpactFrame_4)
        self.integrity_4.setGeometry(QtCore.QRect(10, 40, 81, 20))
        self.integrity_4.setObjectName("integrity_4")

        self.confidentiality_4 = QtWidgets.QCheckBox(self.potentialImpactFrame_4)
        self.confidentiality_4.setGeometry(QtCore.QRect(10, 20, 111, 20))
        self.confidentiality_4.setObjectName("confidentiality_4")

        self.availability_4 = QtWidgets.QCheckBox(self.potentialImpactFrame_4)
        self.availability_4.setGeometry(QtCore.QRect(10, 60, 111, 20))
        self.availability_4.setObjectName("availability_4")

        self.sortByDate_4 = QtWidgets.QCheckBox(self.analyst4)
        self.sortByDate_4.setGeometry(QtCore.QRect(230, 20, 111, 20))
        self.sortByDate_4.setObjectName("sortByDate_4")

        self.includeKeywords_4 = QtWidgets.QLineEdit(self.analyst4)
        self.includeKeywords_4.setGeometry(QtCore.QRect(10, 260, 421, 22))
        self.includeKeywords_4.setObjectName("includeKeywords_4")

        self.excludeKeywords_4 = QtWidgets.QLineEdit(self.analyst4)
        self.excludeKeywords_4.setGeometry(QtCore.QRect(10, 310, 421, 22))
        self.excludeKeywords_4.setObjectName("excludeKeywords_4")

        self.mostImpact_4 = QtWidgets.QCheckBox(self.analyst4)
        self.mostImpact_4.setGeometry(QtCore.QRect(230, 50, 141, 20))
        self.mostImpact_4.setObjectName("mostImpact_4")

        self.bakeBtn_4 = QtWidgets.QPushButton(self.analyst4)
        self.bakeBtn_4.setGeometry(QtCore.QRect(440, 350, 111, 41))
        self.bakeBtn_4.setObjectName("bakeBtn_4")
        self.bakeBtn_4.clicked.connect(
            lambda: writeAnalystRules('analyst_4', self.sortByDate_4, self.wsmSort_4, self.vSlider1_Analyst4,
                                      self.vSlider2_Analyst4, self.vSlider3_Analyst4, self.vSlider4_Analyst4,
                                      self.confidentiality_4,
                                      self.integrity_4,
                                      self.availability_4, self.mostImpact_4, self.includeKeywords_4,
                                      self.excludeKeywords_4))

        self.includeLbl_4 = QtWidgets.QLabel(self.analyst4)
        self.includeLbl_4.setGeometry(QtCore.QRect(10, 240, 201, 20))
        self.includeLbl_4.setObjectName("includeLbl_4")
        self.toolBox.addItem(self.analyst4, "")

        AdminPage.setCentralWidget(self.centralwidget)
        self.retranslateUi(AdminPage)

        # ---Start all additional funcs --
        self.initAllRules()

        QtCore.QMetaObject.connectSlotsByName(AdminPage)
