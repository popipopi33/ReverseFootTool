import maya.cmds as cmds

def create_tg_locator(jnt):
    for _lr in ["L", "R"]:
        _jnt = "{}_{}".format(jnt, _lr)
        if cmds.objExists(_jnt):
            loc = "_{}_LOC".format(_jnt)
            cmds.createNode("locator", n=loc)
            cmds.parentConstraint(_jnt, loc, name="{}_parentConstraint1".format(loc), mo=False)
            cmds.delete("{}_parentConstraint1".format(loc))


def main(scale=1):
    leg_points = [
    "ankle_bindJNT"]

    for point in leg_points:
        create_tg_locator(point)


def delete_loc(jnt):
    for _lr in ["L", "R"]:
        _jnt = "{}_{}".format(jnt, _lr)
        loc = "_{}_LOC".format(_jnt)
        cmds.delete(loc)

