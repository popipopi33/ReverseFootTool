#coding:utf-8
import maya.cmds as cmds

def create_node_tree(node, parent=None):
    s = node[0]
    print s, parent
    if cmds.objExists(s):
        pass
    elif s.split('_')[-1] in ['bindJNT', 'JNT']:
        if parent is not None:
            cmds.select(parent)
            cmds.joint(n=s)
    elif s.split('_')[-1] == 'ctrl':
        cmds.curve(n=s, p=[0,0,0])
        cmds.rename('curveShape1', '{}Shape'.format(s))
        cmds.parent(s, parent)
    elif s.split('_')[-1] in ['pointConstraint1', 'orientConstraint1', 'parentConstraint1']:
        pass
    elif s.split('_')[-1]=='loc':
        cmds.spaceLocator(n=s)
        cmds.parent(s, parent)
    else:
        if parent is not None:
            cmds.createNode('transform', n=s, p=parent)
        else:
            cmds.createNode('transform', n=s)

    for c in node[1]: # 子ノードでループ
        create_node_tree(c, s)
        pass
    return s

def adjust_tr(tar, obj):
    if tar == "zero":
        pos = tuple([0, 0, 0])
    else:
        pos = cmds.xform(tar, q=True, t=True, ws=True)
    cmds.xform(obj, t=pos, ws=True)

def adjust_ro(tar, obj):
    ro = cmds.xform(tar, q=True, ro=True, ws=True)
    cmds.xform(obj, ro=ro, ws=True)


def reverse_foot_setup_main():
    node_tree = [
        ['reverseFoot_Setup_GRP', [
            ['reverseFoot_ctrl_GRP', [
                ['reverseFoot_ctrloffB', [
                    ['reverseFoot_ctrloffA', [
                        ['reverseFoot_ctrl', [
                            ['reverseHeel_ctrloffB', [
                                ['reverseHeel_ctrloffA', [
                                    ['reverseHeel_ctrl', [
                                        ['reverseToe_ctrloffB', [
                                            ['reverseToe_ctrloffA', [
                                                ['reverseToe_ctrl', [
                                                    ['reverseBall_ctrloffB', [
                                                        ['reverseBall_ctrloffA', [
                                                            ['reverseBall_ctrl', []],
                                                        ]],
                                                    ]],
                                                ]],
                                            ]],
                                        ]],
                                    ]],
                                ]],
                            ]],
                        ]],
                    ]],
                ]],
            ]],
            ['ankleFk_ctrl_GRP', [
                ['ankle_ctrloffC', [
                    ['ankle_ctrloffB', [
                        ['ankle_ctrloffA', [
                            ['ankle_ctrl', [
                                ['toe_ctrloffC', [
                                    ['toe_ctrloffB', [
                                        ['toe_ctrloffA', [
                                            ['toe_ctrl', []],
                                        ]],
                                    ]],
                                ]],
                            ]],
                        ]],
                    ]],
                ]],
            ]],
            ['Ik_to_ancleConstrain_LOC', [
                ['ancleConstrain_LOC_OFF', [
                    ['ancleConstrain_LOC', [
                        ['ancleConstrain_LOC_parentConstraint1', []],
                    ]],
                ]],
            ]],
            ['reverseFoot_JNT_GRP', [
                ['ankle_bindJNT_OFF', [
                    ['ankle_bindJNT', [
                        ['heel_sub_bindJNT', []],
                        ['ball_bindJNT', [
                            ['toe_bindJNT', []],
                            ['ball_bindJNT_pointConstraint1', []],
                            ['ball_bindJNT_orientConstraint1', []],
                        ]],
                        ['ankleTop_bindJNT', []],
                        ['ankle_bindJNT_pointConstraint1', []],
                        ['ankle_bindJNT_orientConstraint1', []],
                    ]],
                ]],
                ['ankle_root_ik_JNT_to_ankle_ik', [
                    ['ankle_root_ik_JNT', [
                        ['heel_sub_ik_JNT', []],
                        ['ball_ik_JNT', [
                            ['toe_ik_JNT', []],
                            ['ball_ik_JNT_orientConstraint1', []],
                        ]],
                        ['ankleTop_ik_JNT', []],
                        ['ankle_root_ik_JNT_orientConstraint1', []],
                    ]],
                ]],
                ['reverseFoot_joint', [
                    ['reverseHeel_JNT_OFF', [
                        ['reverseHeel_JNT', [
                            ['reverseToe_JNT', [
                                ['reverseBall_JNT', [
                                    ['reverseAnkle_JNT', []],
                                    ['reverseBall_JNT_orientConstraint1', []],
                                ]],
                                ['reverseToe_JNT_orientConstraint1', []],
                            ]],
                            ['reverseHeel_JNT_orientConstraint1', []],
                        ]],
                    ]],
                ]],
            ]],
        ]],
    ]

    cmds.rename('ankle_root', 'reverseFoot_Setup_GRP')

    create_node_tree(node_tree()[0])
        
    # cmds.setAttr('ankle_ctrloffB.rotateX', 90)
    cmds.setAttr('ancleConstrain_LOC.rotateZ', -90)
    cmds.setAttr('ankle_bindJNT_OFF.rotateZ', -90)
    cmds.setAttr('ankle_root_ik_JNT_to_ankle_ik.rotateZ', -90)
    cmds.setAttr('reverseHeel_JNT_OFF.rotateZ', -90)

    adjust_tr("ankle_bindJNT", "ankle_ctrloffC")
    adjust_ro("ankle_bindJNT", "ankle_ctrloffC")

    ankle_grp = ["ancleConstrain_LOC"]
    for ctrl in ankle_grp:
        adjust_ro("ankle_bindJNT", ctrl)
        adjust_tr("ankle_bindJNT", ctrl)
            
    adjust_tr("ball_bindJNT", "toe_ctrloffC")        
    adjust_ro("ball_bindJNT", "toe_ctrloffC")        
            
    # adjust_ro("ankle_bindJNT", "reverseFoot_ctrloffB")
    adjust_tr("ankle_bindJNT", "reverseFoot_ctrloffB")
    # cmds.xform("reverseFoot_ctrloffB_L", r=True, ro=[0, 0, 90], os=True)           
    # adjust_ro("heel_sub_bindJNT", "reverseHeel_ctrloffB")
    adjust_tr("heel_sub_bindJNT", "reverseHeel_ctrloffB")
    # cmds.xform("reverseHeel_ctrloffB", r=True, ro=[0, 0 , 90], os=True)           
    adjust_tr("toe_bindJNT", "reverseToe_ctrloffB")
    adjust_tr("ball_bindJNT", "reverseBall_ctrloffB")

    cmds.parentConstraint('reverseBall_ctrl', 'ancleConstrain_LOC', mo=True)
    cmds.pointConstraint('toe_ctrl', 'ball_bindJNT', mo=True)
    cmds.orientConstraint('toe_ctrl', 'ball_bindJNT', mo=True)
    cmds.pointConstraint('ankle_ctrl', 'ankle_bindJNT', mo=True)
    cmds.orientConstraint('ankle_ctrl', 'ankle_bindJNT', mo=True)
    cmds.orientConstraint('reverseToe_JNT', 'ball_ik_JNT', mo=True)
    cmds.orientConstraint('reverseToe_ctrl', 'ball_ik_JNT', mo=True)
    cmds.orientConstraint('reverseBall_ctrl', 'reverseBall_JNT', mo=True)
    cmds.orientConstraint('reverseBall_JNT', 'ankle_root_ik_JNT', mo=True)
    cmds.orientConstraint('reverseToe_ctrl', 'reverseToe_JNT', mo=True)
    cmds.orientConstraint('reverseHeel_ctrl', 'reverseHeel_JNT', mo=True)

sys.path.append(r'Y:\tool\ND_Tools\DCC\ReverseFootTool')
import setup.create_tg_locator as reverse_foot_setup
reload(reverse_foot_setup)
reverse_foot_setup.reverse_foot_setup_main()
                        