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
        Dialog.resize(734, 878)
        self.verticalLayout_2 = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.tabWidget = QtGui.QTabWidget(Dialog)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.tab)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.groupBox_3 = QtGui.QGroupBox(self.tab)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.verticalLayout_9 = QtGui.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_9.setObjectName(_fromUtf8("verticalLayout_9"))
        self.groupBox_5 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox_5)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.intermediate_from_calibration_radioButton = QtGui.QRadioButton(self.groupBox_5)
        self.intermediate_from_calibration_radioButton.setChecked(True)
        self.intermediate_from_calibration_radioButton.setObjectName(_fromUtf8("intermediate_from_calibration_radioButton"))
        self.horizontalLayout_2.addWidget(self.intermediate_from_calibration_radioButton)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.intermediate_from_calibration_groups_value = QtGui.QLabel(self.groupBox_5)
        self.intermediate_from_calibration_groups_value.setMinimumSize(QtCore.QSize(20, 0))
        self.intermediate_from_calibration_groups_value.setMaximumSize(QtCore.QSize(20, 16777215))
        self.intermediate_from_calibration_groups_value.setObjectName(_fromUtf8("intermediate_from_calibration_groups_value"))
        self.horizontalLayout_4.addWidget(self.intermediate_from_calibration_groups_value)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setMinimumSize(QtCore.QSize(50, 0))
        self.label_7.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.horizontalLayout_4.addWidget(self.label_7)
        self.horizontalLayout_2.addLayout(self.horizontalLayout_4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.radioButton_2 = QtGui.QRadioButton(self.groupBox_5)
        self.radioButton_2.setMinimumSize(QtCore.QSize(15, 0))
        self.radioButton_2.setMaximumSize(QtCore.QSize(15, 16777215))
        self.radioButton_2.setText(_fromUtf8(""))
        self.radioButton_2.setObjectName(_fromUtf8("radioButton_2"))
        self.horizontalLayout_3.addWidget(self.radioButton_2)
        self.intermediate_browse_button = QtGui.QPushButton(self.groupBox_5)
        self.intermediate_browse_button.setEnabled(False)
        self.intermediate_browse_button.setMinimumSize(QtCore.QSize(100, 0))
        self.intermediate_browse_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.intermediate_browse_button.setObjectName(_fromUtf8("intermediate_browse_button"))
        self.horizontalLayout_3.addWidget(self.intermediate_browse_button)
        self.intermediate_browse_value = QtGui.QLabel(self.groupBox_5)
        self.intermediate_browse_value.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.intermediate_browse_value.sizePolicy().hasHeightForWidth())
        self.intermediate_browse_value.setSizePolicy(sizePolicy)
        self.intermediate_browse_value.setObjectName(_fromUtf8("intermediate_browse_value"))
        self.horizontalLayout_3.addWidget(self.intermediate_browse_value)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.intermediate_browse_groupe_value = QtGui.QLabel(self.groupBox_5)
        self.intermediate_browse_groupe_value.setEnabled(False)
        self.intermediate_browse_groupe_value.setMinimumSize(QtCore.QSize(20, 0))
        self.intermediate_browse_groupe_value.setMaximumSize(QtCore.QSize(20, 16777215))
        self.intermediate_browse_groupe_value.setObjectName(_fromUtf8("intermediate_browse_groupe_value"))
        self.horizontalLayout_5.addWidget(self.intermediate_browse_groupe_value)
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setEnabled(False)
        self.label_5.setMinimumSize(QtCore.QSize(50, 0))
        self.label_5.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.horizontalLayout_5.addWidget(self.label_5)
        self.horizontalLayout_3.addLayout(self.horizontalLayout_5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_3)
        self.verticalLayout_9.addWidget(self.groupBox_5)
        self.groupBox_7 = QtGui.QGroupBox(self.groupBox_3)
        self.groupBox_7.setObjectName(_fromUtf8("groupBox_7"))
        self.verticalLayout_8 = QtGui.QVBoxLayout(self.groupBox_7)
        self.verticalLayout_8.setObjectName(_fromUtf8("verticalLayout_8"))
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName(_fromUtf8("horizontalLayout_6"))
        self.output_from_calibration_radioButton = QtGui.QRadioButton(self.groupBox_7)
        self.output_from_calibration_radioButton.setChecked(True)
        self.output_from_calibration_radioButton.setObjectName(_fromUtf8("output_from_calibration_radioButton"))
        self.horizontalLayout_6.addWidget(self.output_from_calibration_radioButton)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.output_from_calibration_groups_value = QtGui.QLabel(self.groupBox_7)
        self.output_from_calibration_groups_value.setMinimumSize(QtCore.QSize(20, 0))
        self.output_from_calibration_groups_value.setMaximumSize(QtCore.QSize(20, 16777215))
        self.output_from_calibration_groups_value.setObjectName(_fromUtf8("output_from_calibration_groups_value"))
        self.horizontalLayout_7.addWidget(self.output_from_calibration_groups_value)
        self.label_9 = QtGui.QLabel(self.groupBox_7)
        self.label_9.setMinimumSize(QtCore.QSize(50, 0))
        self.label_9.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.horizontalLayout_7.addWidget(self.label_9)
        self.horizontalLayout_6.addLayout(self.horizontalLayout_7)
        self.verticalLayout_8.addLayout(self.horizontalLayout_6)
        self.horizontalLayout_8 = QtGui.QHBoxLayout()
        self.horizontalLayout_8.setObjectName(_fromUtf8("horizontalLayout_8"))
        self.radioButton_4 = QtGui.QRadioButton(self.groupBox_7)
        self.radioButton_4.setMinimumSize(QtCore.QSize(15, 0))
        self.radioButton_4.setMaximumSize(QtCore.QSize(15, 16777215))
        self.radioButton_4.setText(_fromUtf8(""))
        self.radioButton_4.setObjectName(_fromUtf8("radioButton_4"))
        self.horizontalLayout_8.addWidget(self.radioButton_4)
        self.output_browse_button = QtGui.QPushButton(self.groupBox_7)
        self.output_browse_button.setEnabled(False)
        self.output_browse_button.setMinimumSize(QtCore.QSize(100, 0))
        self.output_browse_button.setMaximumSize(QtCore.QSize(100, 16777215))
        self.output_browse_button.setObjectName(_fromUtf8("output_browse_button"))
        self.horizontalLayout_8.addWidget(self.output_browse_button)
        self.output_browse_value = QtGui.QLabel(self.groupBox_7)
        self.output_browse_value.setEnabled(False)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.output_browse_value.sizePolicy().hasHeightForWidth())
        self.output_browse_value.setSizePolicy(sizePolicy)
        self.output_browse_value.setObjectName(_fromUtf8("output_browse_value"))
        self.horizontalLayout_8.addWidget(self.output_browse_value)
        self.horizontalLayout_9 = QtGui.QHBoxLayout()
        self.horizontalLayout_9.setObjectName(_fromUtf8("horizontalLayout_9"))
        self.output_browse_groups_value = QtGui.QLabel(self.groupBox_7)
        self.output_browse_groups_value.setEnabled(False)
        self.output_browse_groups_value.setMinimumSize(QtCore.QSize(20, 0))
        self.output_browse_groups_value.setMaximumSize(QtCore.QSize(20, 16777215))
        self.output_browse_groups_value.setObjectName(_fromUtf8("output_browse_groups_value"))
        self.horizontalLayout_9.addWidget(self.output_browse_groups_value)
        self.label_11 = QtGui.QLabel(self.groupBox_7)
        self.label_11.setEnabled(False)
        self.label_11.setMinimumSize(QtCore.QSize(50, 0))
        self.label_11.setMaximumSize(QtCore.QSize(50, 16777215))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.horizontalLayout_9.addWidget(self.label_11)
        self.horizontalLayout_8.addLayout(self.horizontalLayout_9)
        self.verticalLayout_8.addLayout(self.horizontalLayout_8)
        self.verticalLayout_9.addWidget(self.groupBox_7)
        self.verticalLayout_4.addWidget(self.groupBox_3)
        self.groupBox = QtGui.QGroupBox(self.tab)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.horizontalLayout_40 = QtGui.QHBoxLayout()
        self.horizontalLayout_40.setObjectName(_fromUtf8("horizontalLayout_40"))
        self.pdf_browse_characterization_button = QtGui.QPushButton(self.groupBox)
        self.pdf_browse_characterization_button.setMinimumSize(QtCore.QSize(200, 0))
        self.pdf_browse_characterization_button.setObjectName(_fromUtf8("pdf_browse_characterization_button"))
        self.horizontalLayout_40.addWidget(self.pdf_browse_characterization_button)
        self.pdf_characterization_file = QtGui.QLabel(self.groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pdf_characterization_file.sizePolicy().hasHeightForWidth())
        self.pdf_characterization_file.setSizePolicy(sizePolicy)
        self.pdf_characterization_file.setObjectName(_fromUtf8("pdf_characterization_file"))
        self.horizontalLayout_40.addWidget(self.pdf_characterization_file)
        self.verticalLayout.addLayout(self.horizontalLayout_40)
        self.q_range_group_box_2 = QtGui.QGroupBox(self.groupBox)
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
        self.verticalLayout.addWidget(self.q_range_group_box_2)
        self.q_range_group_box_3 = QtGui.QGroupBox(self.groupBox)
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
        self.verticalLayout.addWidget(self.q_range_group_box_3)
        self.groupBox_6 = QtGui.QGroupBox(self.groupBox)
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
        self.verticalLayout.addWidget(self.groupBox_6)
        self.verticalLayout_4.addWidget(self.groupBox)
        self.groupBox_2 = QtGui.QGroupBox(self.tab)
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.horizontalLayout_38 = QtGui.QHBoxLayout()
        self.horizontalLayout_38.setObjectName(_fromUtf8("horizontalLayout_38"))
        self.mantid_browse_characterization_button_2 = QtGui.QPushButton(self.groupBox_2)
        self.mantid_browse_characterization_button_2.setMinimumSize(QtCore.QSize(200, 0))
        self.mantid_browse_characterization_button_2.setObjectName(_fromUtf8("mantid_browse_characterization_button_2"))
        self.horizontalLayout_38.addWidget(self.mantid_browse_characterization_button_2)
        self.bragg_characterization_file = QtGui.QLabel(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bragg_characterization_file.sizePolicy().hasHeightForWidth())
        self.bragg_characterization_file.setSizePolicy(sizePolicy)
        self.bragg_characterization_file.setObjectName(_fromUtf8("bragg_characterization_file"))
        self.horizontalLayout_38.addWidget(self.bragg_characterization_file)
        self.verticalLayout_3.addLayout(self.horizontalLayout_38)
        self.horizontalLayout_39 = QtGui.QHBoxLayout()
        self.horizontalLayout_39.setObjectName(_fromUtf8("horizontalLayout_39"))
        self.label_56 = QtGui.QLabel(self.groupBox_2)
        self.label_56.setObjectName(_fromUtf8("label_56"))
        self.horizontalLayout_39.addWidget(self.label_56)
        self.bragg_number_of_bins = QtGui.QLineEdit(self.groupBox_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.bragg_number_of_bins.sizePolicy().hasHeightForWidth())
        self.bragg_number_of_bins.setSizePolicy(sizePolicy)
        self.bragg_number_of_bins.setMinimumSize(QtCore.QSize(80, 0))
        self.bragg_number_of_bins.setMaximumSize(QtCore.QSize(80, 16777215))
        self.bragg_number_of_bins.setObjectName(_fromUtf8("bragg_number_of_bins"))
        self.horizontalLayout_39.addWidget(self.bragg_number_of_bins)
        self.label_57 = QtGui.QLabel(self.groupBox_2)
        self.label_57.setObjectName(_fromUtf8("label_57"))
        self.horizontalLayout_39.addWidget(self.label_57)
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_39.addItem(spacerItem2)
        self.verticalLayout_3.addLayout(self.horizontalLayout_39)
        self.horizontalLayout_41 = QtGui.QHBoxLayout()
        self.horizontalLayout_41.setObjectName(_fromUtf8("horizontalLayout_41"))
        self.groupBox_8 = QtGui.QGroupBox(self.groupBox_2)
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
        spacerItem3 = QtGui.QSpacerItem(546, 17, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_41.addItem(spacerItem3)
        self.verticalLayout_3.addLayout(self.horizontalLayout_41)
        self.verticalLayout_4.addWidget(self.groupBox_2)
        spacerItem4 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_4.addItem(spacerItem4)
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
        self.verticalLayout_2.addWidget(self.tabWidget)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.pushButton = QtGui.QPushButton(Dialog)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.horizontalLayout.addWidget(self.pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QObject.connect(self.reset_pdf_q_range_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pdf_reset_q_range_button)
        QtCore.QObject.connect(self.reset_pdf_r_range_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pdf_reset_r_range_button)
        QtCore.QObject.connect(self.pushButton, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.close_button)
        QtCore.QObject.connect(self.pdf_browse_characterization_button, QtCore.SIGNAL(_fromUtf8("clicked()")), Dialog.pdf_browse_characterization_clicked)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Reduction Configuration", None))
        self.groupBox_3.setTitle(_translate("Dialog", "Grouping", None))
        self.groupBox_5.setTitle(_translate("Dialog", "Intermediate", None))
        self.intermediate_from_calibration_radioButton.setText(_translate("Dialog", "From Calibration File", None))
        self.intermediate_from_calibration_groups_value.setText(_translate("Dialog", "N/A", None))
        self.label_7.setText(_translate("Dialog", "groups", None))
        self.intermediate_browse_button.setText(_translate("Dialog", "Browse ...", None))
        self.intermediate_browse_value.setText(_translate("Dialog", "N/A", None))
        self.intermediate_browse_groupe_value.setText(_translate("Dialog", "N/A", None))
        self.label_5.setText(_translate("Dialog", "groups", None))
        self.groupBox_7.setTitle(_translate("Dialog", "Output", None))
        self.output_from_calibration_radioButton.setText(_translate("Dialog", "From Calibration File", None))
        self.output_from_calibration_groups_value.setText(_translate("Dialog", "N/A", None))
        self.label_9.setText(_translate("Dialog", "groups", None))
        self.output_browse_button.setText(_translate("Dialog", "Browse ...", None))
        self.output_browse_value.setText(_translate("Dialog", "N/A", None))
        self.output_browse_groups_value.setText(_translate("Dialog", "N/A", None))
        self.label_11.setText(_translate("Dialog", "groups", None))
        self.groupBox.setTitle(_translate("Dialog", "PDF", None))
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
        self.groupBox_2.setTitle(_translate("Dialog", "Bragg", None))
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
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "General", None))
        self.groupBox_4.setTitle(_translate("Dialog", "Bragg", None))
        self.push_data_positive.setText(_translate("Dialog", "Push Data Positive", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Advanced", None))
        self.pushButton.setText(_translate("Dialog", "Save and Close", None))

