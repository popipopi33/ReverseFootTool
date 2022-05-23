#coding:utf-8
import maya.cmds as cmds

def bind_joint_main():
    zero_threshold = 0.0001
    for jnt in cmds.ls("*_bindJNT_*"):
        if 'Shape' in jnt:
            continue
        if "_loc" in jnt:
            x, y, z = cmds.getAttr("{}.translate".format(jnt))[0]
            _result = []
            for _axis in [x, y, z]:
                if pow(_axis, 2) < zero_threshold:
                    _axis = 0
                _result.append(_axis)
            x, y, z = cmds.getAttr("{}.translate".format(jnt))[0]
            _result = []
            for _axis in [x, y, z]:
                if pow(_axis, 2) < zero_threshold:
                    _axis = 0.0001
                _result.append(_axis)
            cmds.setAttr("{}.translate".format(jnt), _result[0], _result[1], _result[2])
            # Rotate
            x, y, z = cmds.getAttr("{}.rotate".format(jnt))[0]
            _result = []
            for _axis in [x, y, z]:
                if pow(_axis, 2) < zero_threshold:
                    _axis = 0.0001
                _result.append(_axis)
            cmds.setAttr("{}.rotate".format(jnt), _result[0], _result[1], _result[2])
    for const in cmds.ls("*Constraint*"):
        cmds.delete(const)
    cmds.delete("adjustRootAnkle")

    for jnt in ['ankle_bindJNT', 'heel_sub_bindJNT', 'ball_bindJNT', 'toe_bindJNT', 'ankleTop_bindJNT']:
        rot = cmds.xform( jnt, q = 1, worldSpace = 1, rotation = 1 )
        # cmds.setAttr( jnt + '.jointOrient', 0, 0, 0, type = 'double3' )
        cmds.xform( jnt, worldSpace = 1, rotation = rot )
        newRot = cmds.xform( jnt, q = 1, objectSpace = 1, rotation = 1 )
        cmds.setAttr( jnt + '.jointOrient', newRot[0], newRot[1], newRot[2], type = 'double3' )
        try:
            cmds.joint(x, edit=True, oj='y')
        except:
            pass
        cmds.setAttr( jnt + '.rotate', 0, 0, 0, type = 'double3' )
        cmds.setAttr( jnt + '.overrideEnabled', True)
        cmds.setAttr( jnt + '.ovc', 22)
        cmds.setAttr( jnt + '.radius', 2)
# sys.path.append(r'Y:\tool\ND_Tools\DCC\ReverseFootTool')
# import setup.bind_joint as bind_joint
# reload(bind_joint)
# bind_joint.bind_joint_main()