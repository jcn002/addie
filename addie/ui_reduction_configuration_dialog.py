# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'designer/ui_reduction_configuration_dialog.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(813, 575)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.horizontalLayout_26 = QtGui.QHBoxLayout()
        self.horizontalLayout_26.setObjectName(_fromUtf8("horizontalLayout_26"))
        self.label_26 = QtGui.QLabel(self.groupBox_3)
        self.label_26.setMinimumSize(QtCore.QSize(80, 0))
        self.label_26.setMaximumSize(QtCore.QSize(80, 16777215))
        self.label_26.setObjectName(_fromUtf8("label_26"))
        self.horizontalLayout_26.addWidget(self.label_26)
        self.browse_calibration_button = QtGui.QPushButton(self.groupBox_3)
        self.browse_calibration_button.setMinimumSize(QtCore.QSize(100, 0))
        self.browse_calibration_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.browse_calibration_button.setObjectName(_fromUtf8("browse_calibration_button"))
        self.horizontalLayout_26.addWidget(self.browse_calibration_button)
        self.label_27 = QtGui.QLabel(self.groupBox_3)
        self.label_27.setMinimumSize(QtCore.QSize(20, 0))
        self.label_27.setMaximumSize(QtCore.QSize(20, 16777215))
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.horizontalLayout_26.addWidget(self.label_27)
        self.make_calibration_button = QtGui.QPushButton(self.groupBox_3)
        self.make_calibration_button.setMinimumSize(QtCore.QSize(100, 0))
        self.make_calibration_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.make_calibration_button.setObjectName(_fromUtf8("make_calibration_button"))
        self.horizontalLayout_26.addWidget(self.make_calibration_button)
        self.calibration_file = QtGui.QLabel(self.groupBox_3)
        self.calibration_file.setObjectName(_fromUtf8("calibration_file"))
        self.horizontalLayout_26.addWidget(self.calibration_file)
        self.verticalLayout_4.addLayout(self.horizontalLayout_26)
        spacerItem = QtGui.QSpacerItem(20, 53, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem)
        self.verticalLayout_5.addWidget(self.groupBox_3)
        self.toolBox = QtGui.QToolBox(self.tab)
        self.toolBox.setAutoFillBackground(False)
        self.toolBox.setFrameShape(QtGui.QFrame.Panel)
        self.toolBox.setFrameShadow(QtGui.QFrame.Plain)
        self.toolBox.setLineWidth(1)
        self.toolBox.setObjectName(_fromUtf8("toolBox"))
        self.page = QtGui.QWidget()
        self.page.setGeometry(QtCore.QRect(0, 0, 757, 288))
        self.page.setObjectName(_fromUtf8("page"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.page)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        self.pdf_browse_characterization_button = QtGui.QPushButton(self.page)
        self.pdf_browse_characterization_button.setMinimumSize(QtCore.QSize(200, 0))
        self.pdf_browse_characterization_button.setObjectName(_fromUtf8("pdf_browse_characterization_button"))
        self.horizontalLayout_40.addWidget(self.pdf_browse_characterization_button)
        self.pdf_characterization_file = QtGui.QLabel(self.page)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdf_characterization_file.sizePolicy().hasHeightForWidth())
        self.pdf_characterization_file.setSizePolicy(sizePolicy)
        self.pdf_characterization_file.setObjectName(_fromUtf8("pdf_characterization_file"))
        self.horizontalLayout_40.addWidget(self.pdf_characterization_file)
        self.verticalLayout_3.addLayout(self.horizontalLayout_40)
        self.q_range_group_box_2 = QtGui.QGroupBox(self.page)
        self.q_range_group_box_2.setObjectName(_fromUtf8("q_range_group_box_2"))
        self.horizontalLayout_29 = QtGui.QHBoxLayout(self.q_range_group_box_2)
        self.horizontalLayout_29.setObjectName(_fromUtf8("horizontalLayout_29"))
        self.label_43 = QtGui.QLabel(self.q_range_group_box_2)
        self.label_43.setMinimumSize(QtCore.QSize(35, 0))
        self.label_43.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_43.setObjectName(_fromUtf8("label_43"))
        self.horizontalLayout_29.addWidget(self.label_43)
        self.pdf_q_range_min = QtGui.QLineEdit(self.q_range_group_box_2)
        self.pdf_q_range_min.setMinimumSize(QtCore.QSize(80, 0))
        self.pdf_q_range_min.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pdf_q_range_min.setObjectName(_fromUtf8("pdf_q_range_min"))
        self.horizontalLayout_29.addWidget(self.pdf_q_range_min)
        self.label_67 = QtGui.QLabel(self.q_range_group_box_2)
        self.label_67.setMinimumSize(QtCore.QSize(30, 0))
        self.label_67.setObjectName(_fromUtf8("label_67"))
        self.horizontalLayout_29.addWidget(self.label_67)
        self.label_44 = QtGui.QLabel(self.q_range_group_box_2)
        self.label_44.setMinimumSize(QtCore.QSize(40, 0))
        self.label_44.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_44.setObjectName(_fromUtf8("label_44"))
        self.horizontalLayout_29.addWidget(self.label_44)
        self.pdf_q_range_max = QtGui.QLineEdit(self.q_range_group_box_2)
        self.pdf_q_range_max.setMinimumSize(QtCore.QSize(80, 0))
        self.pdf_q_range_max.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pdf_q_range_max.setObjectName(_fromUtf8("pdf_q_range_max"))
        self.horizontalLayout_29.addWidget(self.pdf_q_range_max)
        self.label_68 = QtGui.QLabel(self.q_range_group_box_2)
        self.label_68.setMinimumSize(QtCore.QSize(30, 0))
        self.label_68.setObjectName(_fromUtf8("label_68"))
        self.horizontalLayout_29.addWidget(self.label_68)
        self.label_45 = QtGui.QLabel(self.q_range_group_box_2)
        self.label_45.setMinimumSize(QtCore.QSize(35, 0))
        self.label_45.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_45.setTextFormat(QtCore.Qt.RichText)
        self.label_45.setObjectName(_fromUtf8("label_45"))
        self.horizontalLayout_29.addWidget(self.label_45)
        self.pdf_q_range_delta = QtGui.QLineEdit(self.q_range_group_box_2)
        self.pdf_q_range_delta.setMinimumSize(QtCore.QSize(80, 0))
        self.pdf_q_range_delta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pdf_q_range_delta.setObjectName(_fromUtf8("pdf_q_range_delta"))
        self.horizontalLayout_29.addWidget(self.pdf_q_range_delta)
        self.label_69 = QtGui.QLabel(self.q_range_group_box_2)
        self.label_69.setMinimumSize(QtCore.QSize(30, 0))
        self.label_69.setObjectName(_fromUtf8("label_69"))
        self.horizontalLayout_29.addWidget(self.label_69)
        self.reset_pdf_q_range_button = QtGui.QPushButton(self.q_range_group_box_2)
        self.reset_pdf_q_range_button.setMinimumSize(QtCore.QSize(30, 30))
        self.reset_pdf_q_range_button.setMaximumSize(QtCore.QSize(30, 30))
        self.reset_pdf_q_range_button.setText(_fromUtf8(""))
        self.reset_pdf_q_range_button.setObjectName(_fromUtf8("reset_pdf_q_range_button"))
        self.horizontalLayout_29.addWidget(self.reset_pdf_q_range_button)
        self.verticalLayout_3.addWidget(self.q_range_group_box_2)
        self.q_range_group_box_3 = QtGui.QGroupBox(self.page)
        self.q_range_group_box_3.setObjectName(_fromUtf8("q_range_group_box_3"))
        self.horizontalLayout_32 = QtGui.QHBoxLayout(self.q_range_group_box_3)
        self.horizontalLayout_32.setObjectName(_fromUtf8("horizontalLayout_32"))
        self.label_46 = QtGui.QLabel(self.q_range_group_box_3)
        self.label_46.setMinimumSize(QtCore.QSize(35, 0))
        self.label_46.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_46.setObjectName(_fromUtf8("label_46"))
        self.horizontalLayout_32.addWidget(self.label_46)
        self.pdf_r_range_min = QtGui.QLineEdit(self.q_range_group_box_3)
        self.pdf_r_range_min.setMinimumSize(QtCore.QSize(80, 0))
        self.pdf_r_range_min.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pdf_r_range_min.setObjectName(_fromUtf8("pdf_r_range_min"))
        self.horizontalLayout_32.addWidget(self.pdf_r_range_min)
        self.label_70 = QtGui.QLabel(self.q_range_group_box_3)
        self.label_70.setMinimumSize(QtCore.QSize(30, 0))
        self.label_70.setObjectName(_fromUtf8("label_70"))
        self.horizontalLayout_32.addWidget(self.label_70)
        self.label_47 = QtGui.QLabel(self.q_range_group_box_3)
        self.label_47.setMinimumSize(QtCore.QSize(40, 0))
        self.label_47.setMaximumSize(QtCore.QSize(40, 16777215))
        self.label_47.setObjectName(_fromUtf8("label_47"))
        self.horizontalLayout_32.addWidget(self.label_47)
        self.pdf_r_range_max = QtGui.QLineEdit(self.q_range_group_box_3)
        self.pdf_r_range_max.setMinimumSize(QtCore.QSize(80, 0))
        self.pdf_r_range_max.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pdf_r_range_max.setObjectName(_fromUtf8("pdf_r_range_max"))
        self.horizontalLayout_32.addWidget(self.pdf_r_range_max)
        self.label_73 = QtGui.QLabel(self.q_range_group_box_3)
        self.label_73.setMinimumSize(QtCore.QSize(30, 0))
        self.label_73.setObjectName(_fromUtf8("label_73"))
        self.horizontalLayout_32.addWidget(self.label_73)
        self.label_74 = QtGui.QLabel(self.q_range_group_box_3)
        self.label_74.setMinimumSize(QtCore.QSize(35, 0))
        self.label_74.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_74.setTextFormat(QtCore.Qt.RichText)
        self.label_74.setObjectName(_fromUtf8("label_74"))
        self.horizontalLayout_32.addWidget(self.label_74)
        self.pdf_r_range_delta = QtGui.QLineEdit(self.q_range_group_box_3)
        self.pdf_r_range_delta.setMinimumSize(QtCore.QSize(80, 0))
        self.pdf_r_range_delta.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pdf_r_range_delta.setObjectName(_fromUtf8("pdf_r_range_delta"))
        self.horizontalLayout_32.addWidget(self.pdf_r_range_delta)
        self.label_79 = QtGui.QLabel(self.q_range_group_box_3)
        self.label_79.setMinimumSize(QtCore.QSize(25, 0))
        self.label_79.setObjectName(_fromUtf8("label_79"))
        self.horizontalLayout_32.addWidget(self.label_79)
        self.reset_pdf_r_range_button = QtGui.QPushButton(self.q_range_group_box_3)
        self.reset_pdf_r_range_button.setMinimumSize(QtCore.QSize(30, 30))
        self.reset_pdf_r_range_button.setMaximumSize(QtCore.QSize(30, 30))
        self.reset_pdf_r_range_button.setText(_fromUtf8(""))
        self.reset_pdf_r_range_button.setObjectName(_fromUtf8("reset_pdf_r_range_button"))
        self.horizontalLayout_32.addWidget(self.reset_pdf_r_range_button)
        self.verticalLayout_3.addWidget(self.q_range_group_box_3)
        self.groupBox_6 = QtGui.QGroupBox(self.page)
        self.groupBox_6.setObjectName(_fromUtf8("groupBox_6"))
        self.verticalLayout_10 = QtGui.QVBoxLayout(self.groupBox_6)
        self.verticalLayout_10.setObjectName(_fromUtf8("verticalLayout_10"))
        self.horizontalLayout_31 = QtGui.QHBoxLayout()
        self.horizontalLayout_31.setObjectName(_fromUtf8("horizontalLayout_31"))
        self.label_48 = QtGui.QLabel(self.groupBox_6)
        self.label_48.setMinimumSize(QtCore.QSize(50, 0))
        self.label_48.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_48.setObjectName(_fromUtf8("label_48"))
        self.horizontalLayout_31.addWidget(self.label_48)
        self.pdf_reduction_configuration_file = QtGui.QLineEdit(self.groupBox_6)
        self.pdf_reduction_configuration_file.setObjectName(_fromUtf8("pdf_reduction_configuration_file"))
        self.horizontalLayout_31.addWidget(self.pdf_reduction_configuration_file)
        self.label_49 = QtGui.QLabel(self.groupBox_6)
        self.label_49.setObjectName(_fromUtf8("label_49"))
        self.horizontalLayout_31.addWidget(self.label_49)
        self.verticalLayout_10.addLayout(self.horizontalLayout_31)
        self.verticalLayout_3.addWidget(self.groupBox_6)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.toolBox.addItem(self.page, _fromUtf8(""))
        self.page_2 = QtGui.QWidget()
        self.page_2.setGeometry(QtCore.QRect(0, 0, 771, 204))
        self.page_2.setObjectName(_fromUtf8("page_2"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_2)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.mantid_browse_characterization_button_2 = QtGui.QPushButton(self.page_2)
        self.mantid_browse_characterization_button_2.setMinimumSize(QtCore.QSize(200, 0))
        self.mantid_browse_characterization_button_2.setObjectName(_fromUtf8("mantid_browse_characterization_button_2"))
        self.horizontalLayout_38.addWidget(self.mantid_browse_characterization_button_2)
        self.bragg_characterization_file = QtGui.QLabel(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bragg_characterization_file.sizePolicy().hasHeightForWidth())
        self.bragg_characterization_file.setSizePolicy(sizePolicy)
        self.bragg_characterization_file.setObjectName(_fromUtf8("bragg_characterization_file"))
        self.horizontalLayout_38.addWidget(self.bragg_characterization_file)
        self.verticalLayout_2.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        self.label_56 = QtGui.QLabel(self.page_2)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.horizontalLayout_39.addWidget(self.label_56)
        self.bragg_number_of_bins = QtGui.QLineEdit(self.page_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bragg_number_of_bins.sizePolicy().hasHeightForWidth())
        self.bragg_number_of_bins.setSizePolicy(sizePolicy)
        self.bragg_number_of_bins.setMinimumSize(QtCore.QSize(80, 0))
        self.bragg_number_of_bins.setMaximumSize(QtCore.QSize(80, 16777215))
        self.bragg_number_of_bins.setObjectName(_fromUtf8("bragg_number_of_bins"))
        self.horizontalLayout_39.addWidget(self.bragg_number_of_bins)
        self.label_57 = QtGui.QLabel(self.page_2)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.horizontalLayout_39.addWidget(self.label_57)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem2)
        self.verticalLayout_2.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName(_fromUtf8("horizontalLayout_41"))
        self.groupBox_8 = QtGui.QGroupBox(self.page_2)
        self.groupBox_8.setObjectName(_fromUtf8("groupBox_8"))
        self.horizontalLayout_42 = QtGui.QHBoxLayout(self.groupBox_8)
        self.horizontalLayout_42.setObjectName(_fromUtf8("horizontalLayout_42"))
        self.label_58 = QtGui.QLabel(self.groupBox_8)
        self.label_58.setObjectName(_fromUtf8("label_58"))
        self.horizontalLayout_42.addWidget(self.label_58)
        self.bragg_wavelength_min = QtGui.QLineEdit(self.groupBox_8)
        self.bragg_wavelength_min.setMinimumSize(QtCore.QSize(50, 0))
        self.bragg_wavelength_min.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bragg_wavelength_min.setObjectName(_fromUtf8("bragg_wavelength_min"))
        self.horizontalLayout_42.addWidget(self.bragg_wavelength_min)
        self.label_59 = QtGui.QLabel(self.groupBox_8)
        self.label_59.setObjectName(_fromUtf8("label_59"))
        self.horizontalLayout_42.addWidget(self.label_59)
        self.label_60 = QtGui.QLabel(self.groupBox_8)
        self.label_60.setObjectName(_fromUtf8("label_60"))
        self.horizontalLayout_42.addWidget(self.label_60)
        self.bragg_wavelength_max = QtGui.QLineEdit(self.groupBox_8)
        self.bragg_wavelength_max.setMinimumSize(QtCore.QSize(50, 0))
        self.bragg_wavelength_max.setMaximumSize(QtCore.QSize(50, 16777215))
        self.bragg_wavelength_max.setObjectName(_fromUtf8("bragg_wavelength_max"))
        self.horizontalLayout_42.addWidget(self.bragg_wavelength_max)
        self.label_61 = QtGui.QLabel(self.groupBox_8)
        self.label_61.setObjectName(_fromUtf8("label_61"))
        self.horizontalLayout_42.addWidget(self.label_61)
        self.horizontalLayout_41.addWidget(self.groupBox_8)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_41)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem4)
        self.toolBox.addItem(self.page_2, _fromUtf8(""))
        self.verticalLayout_5.addWidget(self.toolBox)
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(_fromUtf8("verticalLayout_6"))
        self.groupBox_4 = QtGui.QGroupBox(self.tab_2)
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.groupBox_4)
        self.verticalLayout_7.setObjectName(_fromUtf8("verticalLayout_7"))
        self.push_data_positive = QtGui.QCheckBox(self.groupBox_4)
        self.push_data_positive.setObjectName(_fromUtf8("push_data_positive"))
        self.verticalLayout_7.addWidget(self.push_data_positive)
        self.verticalLayout_6.addWidget(self.groupBox_4)
        spacerItem5 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem5)
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.verticalLayout.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)
        QtCore.QObject.connect(self.make_calibration_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.make_calibration_clicked)
        QtCore.QObject.connect(self.reset_pdf_q_range_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pdf_reset_q_range_button)
        QtCore.QObject.connect(self.reset_pdf_r_range_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pdf_reset_r_range_button)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close_button)
        QtCore.QObject.connect(self.browse_calibration_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.browse_calibration_clicked)
        QtCore.QObject.connect(self.pdf_browse_characterization_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pdf_browse_characterization_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Reduction Configuration", None))
        self.groupBox_3.setTitle(_translate("Dialog", "PDF and Bragg", None))
        self.label_26.setText(_translate("Dialog", "Calibration:", None))
        self.browse_calibration_button.setText(_translate("Dialog", "Browse ...", None))
        self.label_27.setText(_translate("Dialog", "or", None))
        self.make_calibration_button.setText(_translate("Dialog", "Make ...", None))
        self.calibration_file.setText(_translate("Dialog", "N/A", None))
        self.pdf_browse_characterization_button.setText(_translate("Dialog", "Browse Characterization ...", None))
        self.pdf_characterization_file.setText(_translate("Dialog", "N/A", None))
        self.q_range_group_box_2.setTitle(_translate("Dialog", "Q range", None))
        self.label_43.setText(_translate("Dialog", "Qmin", None))
        self.pdf_q_range_min.setText(_translate("Dialog", "0", None))
        self.label_67.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Å<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.label_44.setText(_translate("Dialog", "Qmax", None))
        self.pdf_q_range_max.setText(_translate("Dialog", "40", None))
        self.label_68.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Å<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.label_45.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">∆Q</span></p></body></html>", None))
        self.pdf_q_range_delta.setText(_translate("Dialog", "0.02", None))
        self.label_69.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Å<span style=\" vertical-align:super;\">-1</span></p></body></html>", None))
        self.q_range_group_box_3.setTitle(_translate("Dialog", "R range", None))
        self.label_46.setText(_translate("Dialog", "Rmin", None))
        self.pdf_r_range_min.setText(_translate("Dialog", "0", None))
        self.label_70.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Å</p></body></html>", None))
        self.label_47.setText(_translate("Dialog", "Rmax", None))
        self.pdf_r_range_max.setText(_translate("Dialog", "40", None))
        self.label_73.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Å</p></body></html>", None))
        self.label_74.setText(_translate("Dialog", "<html><head/><body><p><span style=\" font-size:11pt;\">∆R</span></p></body></html>", None))
        self.pdf_r_range_delta.setText(_translate("Dialog", "0.02", None))
        self.label_79.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Å</p></body></html>", None))
        self.groupBox_6.setTitle(_translate("Dialog", "Reduction Config. File", None))
        self.label_48.setText(_translate("Dialog", "Name:", None))
        self.label_49.setText(_translate("Dialog", ".json", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), _translate("Dialog", "PDF", None))
        self.mantid_browse_characterization_button_2.setText(_translate("Dialog", "Browse Characterization ...", None))
        self.bragg_characterization_file.setText(_translate("Dialog", "N/A", None))
        self.label_56.setText(_translate("Dialog", "Number of Bins:", None))
        self.bragg_number_of_bins.setText(_translate("Dialog", "-6000", None))
        self.label_57.setText(_translate("Dialog", "(\"-\" for log binning)", None))
        self.groupBox_8.setTitle(_translate("Dialog", "Crop Wavelength", None))
        self.label_58.setText(_translate("Dialog", "Min", None))
        self.bragg_wavelength_min.setText(_translate("Dialog", ".1", None))
        self.label_59.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&#8491;</p></body></html>", None))
        self.label_60.setText(_translate("Dialog", "         Max", None))
        self.bragg_wavelength_max.setText(_translate("Dialog", "2.9", None))
        self.label_61.setText(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">&#8491;</p></body></html>", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), _translate("Dialog", "Bragg", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Bragg", None))
        self.push_data_positive.setText(_translate("Dialog", "Push Data Positive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Advanced", None))
        self.pushButton.setText(_translate("Dialog", "Save and Close", None))

