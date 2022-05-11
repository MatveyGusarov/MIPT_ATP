from tree_utils_02.tree import Tree
from tree_utils_02.node import FileNode
import pytest


def test_all(tmpdir):
    file = tmpdir.join('any_file.txt')
    a_sub_dir = tmpdir.mkdir('subdir')
    another_file = a_sub_dir.join('something_else.txt')
    file.write('write')
    another_file.write('write')
    tree = Tree()
    assert tree.get(tmpdir, True) == FileNode(name='test_all0', is_dir=True, children=[FileNode(name='subdir', is_dir=True, children=[])])
    with pytest.raises(AttributeError) as e_info:
        tree.get("./LevyiFile", False)

    assert tree.get(file, False, False) == FileNode(name='any_file.txt', is_dir=False, children=[])

    with pytest.raises(AttributeError) as e_info:
        tree.get(file, True, False)

    node = FileNode(name='any_file.txt', is_dir=False, children=[])
    tree.filter_empty_nodes(node)

    empty_dir = tmpdir.mkdir('empty')
    node = tree.get(tmpdir, True)
    tree.filter_empty_nodes(node)
    assert FileNode(name='tmpdir', is_dir=False, children=[]) == node

