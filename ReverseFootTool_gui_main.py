# coding:utf-8

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
sys.path.append("Y:/tool/ND_Tools/DCC/{}/setup".format(TOOLNAME))

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
        self.set_window_pos()

        self.setWindowTitle('%s %s' % (self.WINDOW, __version__))

        self.ui.create_locator_button.clicked.connect(self.create_locator_button_clicked)
        self.ui.create_joint_button.clicked.connect(self.create_joint_button_clicked)
        self.ui.setup_button.clicked.connect(self.setup_button_clicked)
        self.ui.ik_const_button.clicked.connect(self.ik_const_button_clicked)
        self.ui.import_leg_rig_button.clicked.connect(self.import_leg_rig_button_clicked)
        self.ui.adjust_radius_button.clicked.connect(self.adjust_radius_button_clicked)

    def set_window_pos(self):
        desktop = QtWidgets.qApp.desktop()
        activeScreen  = desktop.screenNumber(desktop.cursor().pos())
        desktopCenter = desktop.screenGeometry(activeScreen).center()
        w_w = desktopCenter.x()
        w_h = desktopCenter.y()
        u_w = self.ui.width()
        u_h = self.ui.height()
        
        self.move(w_w-u_w/2, w_h-u_h/2)

    def create_locator_button_clicked(self):
        import create_reversefoot_locator
        reload(create_reversefoot_locator)
        create_reversefoot_locator.create_reversefoot_locator_main()
        cmds.inViewMessage(assistMessage="Create Locators finished.", pos='midCenter', fade=True, fst=3500, fts=26)    

    def create_joint_button_clicked(self):
        self.adjust_scale = cmds.getAttr("adjustRootAnkle.scaleX")  
        import bind_joint
        reload(bind_joint)
        bind_joint.bind_joint_main()
        cmds.inViewMessage(assistMessage="Create joint finished.", pos='midCenter', fade=True, fst=3500, fts=26)    
    
    def setup_button_clicked(self):
        import reverse_foot_setup
        reload(reverse_foot_setup)
        reverse_foot_setup.reverse_foot_setup_main(self.adjust_scale)
        cmds.inViewMessage(assistMessage="Setup finished.", pos='midCenter', fade=True, fst=3500, fts=26)    

    def ik_const_button_clicked(self):
        cmds.pointConstraint('ancleConstrain_LOC', self.ui.tg_ik_text.text())

        cmds.parentConstraint('Leg_Rig_v001:kneeA_ctrl', 'ankle_ctrloffC', mo=True)
        cmds.parentConstraint('Leg_Rig_v001:ankle_ik_JNT', 'ankle_root_ik_JNT_to_ankle_ik', mo=True)
        # cmds.pointConstraint('kneeA_ctrl', 'kneeA_bindJNT', mo=True)
        # cmds.orientConstraint('kneeA_ctrl', 'kneeA_bindJNT', mo=True)
        
        # cmds.parentConstraint('thighLOC', 'secLegPV_ctrloffB', mo=True)

    def import_leg_rig_button_clicked(self):
        leg_rig_ma = 'Y:\\tool\\ND_Tools\\DCC\\ReverseFootTool\\sample\\0301\\Leg_Rig_v001.mb'
        leg_rig_ns = leg_rig_ma.split('\\')[-1].rstrip('.ma').rstrip('.mb')
        cmds.file(leg_rig_ma, i=True, ns=leg_rig_ns)

    def adjust_radius_button_clicked(self):
        if not cmds.objExists('adjustRootAnkle'):
            cmds.inViewMessage(assistMessage="Target Joint not found.", pos='midCenter', fade=True, fst=3500, fts=26)   
            return
        self.adjust_scale = cmds.getAttr("adjustRootAnkle.scaleX")
        for jnt in cmds.ls("*", type="joint"[:]):
            n_rad = cmds.getAttr("{}.radiusOrigin".format(jnt))
            cmds.setAttr("{}.radius".format(jnt), self.adjust_scale*n_rad)
            
def runs(*argv):
    app = QApplication.instance()
    if app is None:
        app = QApplication(sys.argv)
    global Debug
    if argv[0]==True:
        Debug=True
    else:
        Debug=False
    print("Debug :{}".format(Debug))
    print(toolpath)
    ui = GUI()
    ui.show()
    # app.exec_()

    return True

# if __name__ == '__main__':
#     leg_ma = r'Y:\tool\ND_Tools\DCC\ReverseFootTool\sample\0301\Leg_Rig_v001.mb'
#     print(os.path.exists(leg_ma))
#     cmds.file(leg_ma, o=True, force=True)
#     # runs(sys.argv[1:])
#     sys.path.append(r'Y:\tool\ND_Tools\DCC')
#     import ReverseFootTool.gui.gui_main as gui_main
#     reload(gui_main)
#     gui_main.runs('')

'''
cmds.parentConstraint('kneeA_ctrl', 'ankle_ctrloffC', mo=True)
cmds.parentConstraint('ankle_root_ik_JNT_to_ankle_ik', 'ankle_ik_JNT', mo=True)


Y:\tool\ND_Tools\DCC\ReverseFootTool\sample\0301
'''