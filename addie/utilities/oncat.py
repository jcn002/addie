import pyoncat

try:
    from PyQt4.QtGui import QDialog
    from PyQt4 import QtGui, QtCore
except:
    try:
        from PyQt5.QtWidgets import QDialog
        from PyQt5 import QtGui, QtCore
    except:
        raise ImportError("Requires PyQt4 or PyQt5")

from addie.ui_oncat_error_message import Ui_Dialog as UiDialog


# Create token store
class InMemoryTokenStore(object):
    def __init__(self):
        self._token = None

    def set_token(self, token):
        pass

    def get_token(self):
        return self._token


def pyoncatGetRuns(oncat=None, instrument='', runs=-1, facility='SNS'):
    datafiles = oncat.Datafile.list(
        facility=facility,
        instrument=instrument,
        projection=['location'],
        tags=['type/raw'],
        exts=['.nxs.h5'],
        ranges_q='indexed.run_number:%s' % runs
    )
    return datafiles

def pyoncatGetIptsList(oncat=None, instrument='', facility='SNS'):
    ipts_list = oncat.Experiment.list(
        facility=facility,
        instrument=instrument,
        projection=['id']
    )
    return [ipts.name for ipts in ipts_list]


if __name__ == "__main__":
    useRcFile = True
    dashes = 35
    oncat = pyoncatForADDIE(useRcFile=useRcFile)

    print("-" * dashes)
    print("NOMAD file 11000")
    print("-" * dashes)
    datafiles = pyoncatGetRuns(oncat, 'NOM', 111000)
    for datafile in datafiles:
        print(datafile.location)

    print("-" * dashes)
    print("ARCS file 11000")
    print("-" * dashes)
    datafiles = pyoncatGetRuns(oncat, 'ARCS', 11000)
    for datafile in datafiles:
        print(datafile.location)

    print("-" * dashes)
    print("NOMAD IPTSs")
    print("-" * dashes)
    print(pyoncatGetIptsList(oncat, 'NOM'))

    print("-" * dashes)
    print("VISION IPTSs")
    print("-" * dashes)
    print(pyoncatGetIptsList(oncat, 'VIS'))


class OncatErrorMessageWindow(QDialog):

    def __init__(self, parent=None, list_of_runs=[]):
        QDialog.__init__(self, parent=parent)
        self.ui = UiDialog()
        self.ui.setupUi(self)

        self.init_widgets(list_of_runs=list_of_runs)

    def init_widgets(self, list_of_runs=[]):
        str_list_of_runs = "\n".join(list_of_runs)
        self.ui.list_of_runs.setText(str_list_of_runs)




