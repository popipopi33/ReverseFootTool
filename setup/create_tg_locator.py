#coding:utf-8

import maya.cmds as cmds

def create_node_tree(node, parent=None):
    s = node[0]
    # print s, parent
    if cmds.objExists(s):
        pass
    elif s.split('_')[-1] in ['bindJNT', 'JNT']:
        if parent is not None:
            cmds.select(parent)
            cmds.joint(n=s)
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


def create_tg_locator_main():
    locator_tree = [
        ['ankle_root', [
            ['ankle_bindJoint_GRP', [
                ['ankle_bindJNT_OFF', [
                    ['ankle_bindJNT', [
                        ['heel_sub_bindJNT', []],
                        ['ball_bindJNT', [
                            ['toe_bindJNT', []],
                        ]],
                        ['ankleTop_bindJNT', []],
                    ]],
                ]],
            ]],
        ]],
    ]

    adjust_root_tree = [
        ['adjustRootAnkle', [
            ['ankle_bindJNT_loc_OFF', [
                ['ankle_bindJNT_L_loc', [
                    ['ball_bindJNT_loc_OFF', [
                        ['ball_bindJNT_L_loc', [
                            ['toe_bindJNT_L_loc_OFF', [
                                ['toe_bindJNT_L_loc', []],
                            ]],
                        ]],
                    ]],
                    ['heel_sub_bindJNT_loc_OFF', [
                        ['heel_sub_bindJNT_L_loc', []],
                    ]],
                    ['ankleTop_bindJNT_loc_OFF', [
                        ['ankleTop_bindJNT_L_loc', []],
                    ]],
                ]],
            ]],
        ]],
    ]

    create_node_tree(locator_tree[0])
    create_node_tree(adjust_root_tree[0])


    cmds.setAttr('ankle_bindJNT_OFF.translate', 0, 11, 0)
    cmds.setAttr('ankle_bindJNT_OFF.rotate', 0, 0, -90)

    cmds.setAttr('ankle_bindJNT_loc_OFF.translate', 0, 11, 0)
    cmds.setAttr('ankle_bindJNT_loc_OFF.rotate', 0, 0, -90)

    cmds.setAttr('ball_bindJNT_loc_OFF.translate', 8, 0, 14)
    cmds.setAttr('ball_bindJNT_loc_OFF.rotate', 0, -66.8, 0)

    cmds.setAttr('toe_bindJNT_L_loc_OFF.translate', 7.616, 0, 0)

    cmds.setAttr('heel_sub_bindJNT_loc_OFF.translate', 11, 0, -6)

    cmds.setAttr('ankleTop_bindJNT_loc_OFF.translate', 11, 0, 0)

    cmds.pointConstraint('heel_sub_bindJNT_L_loc','heel_sub_bindJNT')
    cmds.orientConstraint('heel_sub_bindJNT_L_loc','heel_sub_bindJNT')
    
    cmds.pointConstraint('toe_bindJNT_L_loc', 'toe_bindJNT')
    cmds.orientConstraint('toe_bindJNT_L_loc', 'toe_bindJNT')

    cmds.pointConstraint('ball_bindJNT_L_loc', 'ball_bindJNT')
    cmds.orientConstraint('ball_bindJNT_L_loc', 'ball_bindJNT')

    cmds.pointConstraint('ankleTop_bindJNT_L_loc', 'ankleTop_bindJNT')
    cmds.orientConstraint('ankleTop_bindJNT_L_loc', 'ankleTop_bindJNT')

    cmds.pointConstraint('ankle_bindJNT_L_loc', 'ankle_bindJNT')
    cmds.orientConstraint('toe_bindJNT_L_loc', 'toe_bindJNT')

# create_locator()

# sys.path.append(r'Y:\tool\ND_Tools\DCC\ReverseFootTool')
# import setup.create_tg_locator as create_tg_locator
# reload(create_tg_locator)
# create_tg_locator.main()

