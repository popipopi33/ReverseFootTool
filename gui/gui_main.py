# coding: utf-8

# ------------------------------
__version__ = "0.1"
__author__ = "Kei Ueda"
# ------------------------------

Debug = True
TOOLNAME = "ReverseFootTool"

# if Debug:
#     TOOLNAME = TOOLNAME + "_dev"
import os,sys

import PySide2
import PySide2.QtGui as QtGui
import PySide2.QtCore as QtCore
import PySide2.QtWidgets as QtWidgets

from PySide2.QtGui import *
from PySide2.QtCore import *
from PySide2.QtUiTools import QUiLoader
from PySide2.QtWidgets import *

from maya.app.general.mayaMixin import MayaQWidgetBaseMixin

toolpath = "Y:/tool/ND_Tools/DCC/{}".format(TOOLNAME)
sys.path.append(toolpath)

from importlib import import_module
import maya.cmds as cmds


class GUI(MayaQWidgetBaseMixin, QMainWindow):
    
    WINDOW = TOOLNAME

    def __init__(self, parent=None):
        super(GUI, self).__init__(parent)

        self.ui_path = '{}/gui/ReverseFoot_gui.ui'.format(toolpath)
        self.ui = QUiLoader().load(self.ui_path)
        self.setCentralWidget(self.ui)
        self.setGeometry(500, 200, 500, 180)

        self.setWindowTitle('%s %s' % (self.WINDOW, __version__))

        self.ui.create_locator_button.clicked.connect(self.create_locator_button_clicked)
        self.ui.create_joint_button.clicked.connect(self.create_joint_button_clicked)
        self.ui.setup_button.clicked.connect(self.setup_button_clicked)

    def create_locator_button_clicked(self):
        import setup.create_tg_locator as create_tg_locator
        reload(create_tg_locator)
        create_tg_locator.create_tg_locator_main()
        cmds.inViewMessage(assistMessage="Create Locators finished.", pos='midCenter', fade=True, fst=3500, fts=26)    

    def create_joint_button_clicked(self):        
        import setup.bind_joint as bind_joint
        reload(bind_joint)
        bind_joint.bind_joint_main()
        cmds.inViewMessage(assistMessage="Create joint finished.", pos='midCenter', fade=True, fst=3500, fts=26)    
    
    def setup_button_clicked(self):
        import setup.reverse_foot_setup as reverse_foot_setup
        reload(reverse_foot_setup)
        reverse_foot_setup.reverse_foot_setup_main()
        import setup.ctrlshape_cc as ctrlshape_cc
        reload(ctrlshape_cc)
        ctrlshape_cc.ctrlshape_cc_main()
        cmds.inViewMessage(assistMessage="Setup finished.", pos='midCenter', fade=True, fst=3500, fts=26)    


def runs(*argv):
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    global Debug
    if argv[0]==True:
        Debug=True
    else:
        Debug=False
    print "Debug :{}".format(Debug)
    print toolpath
    ui = GUI()
    ui.show()
    # app.exec_()

    return True

if __name__ == '__main__':
    # runs(sys.argv[1:])
    sys.path.append(r'Y:\tool\ND_Tools\DCC\ReverseFootTool\gui')
    import gui_main
    gui_main.runs('')