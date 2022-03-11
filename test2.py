# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from __future__ import print_function
from __future__ import division
from __future__ import absolute_import

from maya.api import OpenMaya as om2


def get_nodes_sort_by_outliner(root_node):
    """アウトライナと同様の順で階層ノードを取得

    :type root_node: om2.MDagPath
    :rtype: list[om2.MDagPath]
    """
    result = []
    not_checked_yet = [root_node]   # アウトライナ順に取得するrootのノード

    while True:
        current_node = not_checked_yet.pop()

        # 判定中のノードの子階層を未確認リストに追加するために取得する
        children_dependencies = [current_node.child(_index)
                                 for _index in range(current_node.childCount())]
        children_dags = [dag_from_dep(_dep) for _dep in children_dependencies]

        # MDagPath.current_node.child(_index)で番号順にDependencyを取得するとoutlinerと逆順で出てくる
        # なので、取得した子階層のノードリストを反転して結合していくとアウトライナと同順でノードの整列が出来る
        # なぜ逆順なのかは知らない
        not_checked_yet += children_dags[::-1]

        # 確認済みのノードを結果リストに追加, 未確認ノードが存在しない場合はループを終了する
        result.append(current_node)
        if not not_checked_yet:
            break

    return result


def dag_from_dep(dependency):
    """dependency から DagPathを取得

    :type dependency: om2.MObject
    :rtype: om2.MDagPath
    """
    temp_mfn_dag = om2.MFnDagNode(dependency)
    return temp_mfn_dag.getPath()


def main():
    """確認用 現在の選択ノードをroot dag pathとして関数を呼び出し"""
    sel = om2.MGlobal.getActiveSelectionList()
    """:type: om2.MSelectionList"""
    dag = sel.getDagPath(0)
    for _n in get_nodes_sort_by_outliner(dag):
        # DagPath.lengthで階層深さを数字で取得できる
        # ちなみにcmds.lsで取得できないworld階層というものがMayaシーンには存在しているので、ノード階層は0基準で開始する
        _hierarchy = _n.length()-1
        print("{space}{node}".format(
            space="    "*_hierarchy, node=_n))

main()