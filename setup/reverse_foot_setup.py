#coding:utf-8
import maya.cmds as cmds

def create_node_tree(node, parent=None):
    s = node[0]
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


def reverse_foot_setup_main(adjust_scale):
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
                        ['ancleConstrain_LOC_pointConstraint1', []],
                        ['ancleConstrain_LOC_orientConstraint1', []],
                    ]],
                ]],
            ]],
            ['reverseFoot_JNT_GRP', [
                ['ankle_bindJNT_OFF', [
                    ['ankle_bindJNT', [
                        ['ankleTop_bindJNT', []],
                        ['heel_sub_bindJNT', []],
                        ['ball_bindJNT', [
                            ['toe_bindJNT', []],
                            ['ball_bindJNT_pointConstraint1', []],
                            ['ball_bindJNT_orientConstraint1', []],
                        ]],
                        ['ankle_bindJNT_pointConstraint1', []],
                        ['ankle_bindJNT_orientConstraint1', []],
                    ]],
                ]],
                ['ankle_root_ik_JNT_to_ankle_ik', [
                    ['ankle_root_ik_JNT', [
                        ['ankleTop_ik_JNT', []],
                        ['heel_sub_ik_JNT', []],
                        ['ball_ik_JNT', [
                            ['toe_ik_JNT', []],
                            ['ball_ik_JNT_orientConstraint1', []],
                        ]],
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
    for jnt in cmds.ls("*", type="joint")[:]:
        if 'ankle_bind' in jnt:
            continue
        if 'ankle_root' in jnt:
            continue
        cmds.makeIdentity(jnt, rotate=True)
        cmds.joint(jnt, e=True, oj='xyz', sao="yup", zso=True)
    create_node_tree(node_tree[0])
    import ReverseFootTool.setup.ctrlshape_cc as ctrlshape_cc
    reload(ctrlshape_cc)
    ctrlshape_cc.ctrlshape_cc_main(adjust_scale)

    cmds.setAttr('ankle_ctrloffB.rotateX', 90)
    adjust_tr("ankle_bindJNT", "ancleConstrain_LOC_OFF")
    cmds.setAttr('ancleConstrain_LOC.rotateZ', -90)
    adjust_tr("ankle_bindJNT", "ankle_ctrloffC")
    adjust_ro("ankle_bindJNT", "ankle_ctrloffC")
    cmds.xform("ankle_ctrloffC", r=True, ro=[-90, 0, 0], os=True)

    adjust_ro('ankle_bindJNT', 'ankle_root_ik_JNT_to_ankle_ik')
    adjust_ro('ankle_bindJNT', 'ankle_root_ik_JNT')
    adjust_ro("ankle_bindJNT", "reverseFoot_ctrloffB")
    adjust_tr("ankle_bindJNT", "reverseFoot_ctrloffB")
    cmds.xform("reverseFoot_ctrloffB", r=True, ro=[0, 0, 90], os=True)
    adjust_tr("heel_sub_bindJNT", "reverseHeel_ctrloffB")
    adjust_tr('heel_sub_bindJNT', 'reverseHeel_JNT_OFF')
    adjust_tr("toe_bindJNT","reverseToe_ctrloffB")
    adjust_tr("ball_bindJNT", "reverseBall_ctrloffB")


    adjust_tr("ankle_bindJNT", "ankle_root_ik_JNT_to_ankle_ik")
    adjust_tr('heel_sub_bindJNT', 'heel_sub_ik_JNT')

    adjust_tr('ball_bindJNT', 'ball_ik_JNT')
    adjust_tr('toe_bindJNT', 'toe_ik_JNT')
    adjust_tr('ankleTop_bindJNT', 'ankleTop_ik_JNT')

    adjust_tr("ball_bindJNT", "toe_ctrloffC")
    adjust_ro("ball_bindJNT", "toe_ctrloffC")
    cmds.xform('toe_ctrloffC', r=True, ro=[-90, 0, 0], os=True)
    adjust_ro('reverseHeel_ctrl', 'reverseHeel_JNT_OFF')
    cmds.xform("reverseHeel_JNT_OFF", r=True, ro=[0, -90, 0], os=True)
    adjust_tr('reverseHeel_ctrl', 'reverseHeel_JNT_OFF')
    adjust_tr('toe_bindJNT', 'reverseToe_JNT')
    adjust_tr('ball_bindJNT', 'reverseBall_JNT')
    adjust_tr('ankle_bindJNT', 'reverseAnkle_JNT')

        # adjust_ro('ball_bindJNT', 'reverseBall_JNT')

    # adjust_ro('ankle_bindJNT', 'reverseAnkle_JNT')
    cmds.reorder('ankleTop_bindJNT', relative=True)


    adjust_ro('ankle_bindJNT', 'ankle_bindJNT_OFF')
    cmds.setAttr

    cmds.setAttr('ankle_bindJNT.jointOrientX', -90)
    cmds.setAttr('ankle_root_ik_JNT.jointOrientY', -0.005)

    cmds.setAttr('ball_bindJNT.jointOrientX', 0.001)
    cmds.setAttr('toe_ik_JNT.jointOrientX', 0)
    cmds.setAttr('toe_ik_JNT.jointOrientZ', 0)

    cmds.setAttr('ball_ik_JNT.jointOrientX', -0.005)
    cmds.connectAttr('ankle_root_ik_JNT.rotateX', 'ankle_ctrloffB.rotateX')
    cmds.connectAttr('ankle_root_ik_JNT.rotateY', 'ankle_ctrloffB.rotateY')
    cmds.connectAttr('ankle_root_ik_JNT.rotateZ', 'ankle_ctrloffB.rotateZ')

    cmds.connectAttr('ball_ik_JNT.rotateX', 'toe_ctrloffA.rotateX')
    cmds.connectAttr('ball_ik_JNT.rotateY', 'toe_ctrloffA.rotateY')
    cmds.connectAttr('ball_ik_JNT.rotateZ', 'toe_ctrloffA.rotateZ')
    cmds.parentConstraint('reverseBall_ctrl', 'ancleConstrain_LOC', mo=True)

    cmds.setAttr('ankle_root_ik_JNT.rotateX', 90)
    cmds.setAttr('ankle_root_ik_JNT.jointOrientX', -90)

    cmds.pointConstraint('toe_ctrl', 'ball_bindJNT', mo=False)
    cmds.orientConstraint('toe_ctrl', 'ball_bindJNT', mo=False)
    cmds.pointConstraint('ankle_ctrl', 'ankle_bindJNT', mo=False)
    cmds.orientConstraint('ankle_ctrl', 'ankle_bindJNT', mo=False)
    cmds.orientConstraint('reverseToe_JNT', 'ball_ik_JNT', mo=True)
    # cmds.orientConstraint('reverseToe_ctrl', 'ball_ik_JNT', mo=True)
    cmds.orientConstraint('reverseBall_ctrl', 'reverseBall_JNT', mo=True)
    cmds.orientConstraint('reverseBall_JNT', 'ankle_root_ik_JNT', mo=True)
    cmds.orientConstraint('reverseToe_ctrl', 'reverseToe_JNT', mo=True)
    cmds.orientConstraint('reverseHeel_ctrl', 'reverseHeel_JNT', mo=True)

    for jnt in cmds.ls(type='joint'):
        if 'ik' in jnt:
            cmds.setAttr("{}.radius".format(jnt), cmds.getAttr("{}.radius".format(jnt))*0.9)

# sys.path.append(r'Y:\tool\ND_Tools\DCC\ReverseFootTool')
# import setup.create_tg_locator as reverse_foot_setup
# reload(reverse_foot_setup)
# reverse_foot_setup.reverse_foot_setup_main()
