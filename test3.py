#coding:utf-8
def create_node_tree(node, parent=None):
    s = node[0]
    print s, parent
    if s.split('_')[-1] in ['bindJNT', 'JNT']:
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

x = [
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

create_node_tree(x[0])
                        