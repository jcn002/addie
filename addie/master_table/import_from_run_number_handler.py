try:
    from PyQt4.QtGui import QDialog
except:
    try:
        from PyQt5.QtWidgets import QDialog
    except:
        raise ImportError("Requires PyQt4 or PyQt5")

from addie.master_table.oncat_authentication_handler import OncatAuthenticationHandler

from addie.ui_import_from_run_number import Ui_Dialog as UiDialog


class ImportFromRunNumberHandler:

    def __init__(self, parent=None):
        if parent.import_from_run_number_ui is None:
            o_import = ImportFromRunNumberWindow(parent=parent)
            o_import.show()
            parent.import_from_run_number_ui = o_import
            if parent.import_from_run_number_ui_position:
                parent.import_from_run_number_ui.move(parent.import_from_run_number_ui_position)
        else:
            parent.import_from_run_number_ui.setFocus()
            parent.import_from_run_number_ui.activateWindow()


class ImportFromRunNumberWindow(QDialog):

    def __init__(self, parent=None):
        self.parent = parent

        QDialog.__init__(self, parent=parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)

        self.init_widgets()

    def init_widgets(self):
        pass

    def change_user_clicked(self):
        OncatAuthenticationHandler(parent=self.parent)

    def run_number_return_pressed(self):
        pass

    def run_number_text_changed(self, run_number_string):
        self.check_widgets(run_number_string=run_number_string)

    def run_number_format_is_correct(self, run_number_string):
        #FIXME
        # make sure the format of the string is correct and that we can retrieve a correct list of runs
        return True

    def check_widgets(self, run_number_string=""):
        enabled_import_button = True
        if run_number_string.strip() == "":
            if not self.run_number_format_is_correct(run_number_string.strip()):
                enabled_import_button = False
        self.ui.import_button.setEnabled(enabled_import_button)

    def import_button_clicked(self):
        pass

    def cancel_button_clicked(self):
        self.close()

    def closeEvent(self, c):
        self.parent.import_from_run_number_ui = None
        self.parent.import_from_run_number_ui_position = self.pos()