# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/allan/PycharmProjects/pyqt/config/ui/themeConfig_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_themeDialog(object):
    def setupUi(self, themeDialog):
        themeDialog.setObjectName("themeDialog")
        themeDialog.resize(468, 418)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(themeDialog.sizePolicy().hasHeightForWidth())
        themeDialog.setSizePolicy(sizePolicy)
        themeDialog.setMinimumSize(QtCore.QSize(0, 0))
        themeDialog.setMaximumSize(QtCore.QSize(1000, 1000))
        themeDialog.setLayoutDirection(QtCore.Qt.LeftToRight)
        themeDialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(themeDialog)
        self.verticalLayout.setContentsMargins(4, 0, 4, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(themeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setContentsMargins(100, -1, 100, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setMidLineWidth(0)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.themeBox = QtWidgets.QComboBox(self.frame_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.themeBox.sizePolicy().hasHeightForWidth())
        self.themeBox.setSizePolicy(sizePolicy)
        self.themeBox.setMinimumSize(QtCore.QSize(10, 0))
        self.themeBox.setMaximumSize(QtCore.QSize(120, 16777215))
        self.themeBox.setObjectName("themeBox")
        self.horizontalLayout_2.addWidget(self.themeBox)
        self.verticalLayout.addWidget(self.frame_2)
        self.preview_label = QtWidgets.QLabel(themeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.preview_label.sizePolicy().hasHeightForWidth())
        self.preview_label.setSizePolicy(sizePolicy)
        self.preview_label.setMinimumSize(QtCore.QSize(20, 20))
        self.preview_label.setFrameShape(QtWidgets.QFrame.Box)
        self.preview_label.setText("")
        self.preview_label.setObjectName("preview_label")
        self.verticalLayout.addWidget(self.preview_label)
        self.link_label = QtWidgets.QLabel(themeDialog)
        self.link_label.setMaximumSize(QtCore.QSize(1000, 16))
        self.link_label.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.link_label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.link_label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.link_label.setWordWrap(False)
        self.link_label.setIndent(6)
        self.link_label.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.link_label.setObjectName("link_label")
        self.verticalLayout.addWidget(self.link_label)
        self.frame_3 = QtWidgets.QFrame(themeDialog)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.frame_3.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btCancel = QtWidgets.QPushButton(self.frame_3)
        self.btCancel.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btCancel.setCheckable(False)
        self.btCancel.setChecked(False)
        self.btCancel.setAutoDefault(True)
        self.btCancel.setDefault(False)
        self.btCancel.setFlat(False)
        self.btCancel.setObjectName("btCancel")
        self.horizontalLayout.addWidget(self.btCancel)
        self.btApply = QtWidgets.QPushButton(self.frame_3)
        self.btApply.setMaximumSize(QtCore.QSize(100, 16777215))
        self.btApply.setObjectName("btApply")
        self.horizontalLayout.addWidget(self.btApply)
        self.verticalLayout.addWidget(self.frame_3)

        self.retranslateUi(themeDialog)
        QtCore.QMetaObject.connectSlotsByName(themeDialog)

    def retranslateUi(self, themeDialog):
        _translate = QtCore.QCoreApplication.translate
        themeDialog.setWindowTitle(_translate("themeDialog", "Theme configuration"))
        self.label.setText(_translate("themeDialog", "Theme:"))
        self.link_label.setText(_translate("themeDialog", "Source: Lorem"))
        self.btCancel.setText(_translate("themeDialog", "Cancel"))
        self.btApply.setText(_translate("themeDialog", "Apply"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    themeDialog = QtWidgets.QDialog()
    ui = Ui_themeDialog()
    ui.setupUi(themeDialog)
    themeDialog.show()
    sys.exit(app.exec_())

