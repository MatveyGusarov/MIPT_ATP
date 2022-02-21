from tree_utils_02.tree import Tree
from tree_utils_02.node import FileNode
from tree_utils_02.size_tree import SizeTree
from tree_utils_02.size_node import FileSizeNode
import pytest

def test_construct_filenode(tmpdir):
    assert FileSizeNode(name='test_0', is_dir=True, children=[], size=0) == FileSizeNode(name='test_0', is_dir=True, children=[], size=0) 
    assert SizeTree().construct_filenode(tmpdir, False) == FileSizeNode(name='test_0', is_dir=False, children=[], size=0)
    assert SizeTree().construct_filenode(main, False) == FileSizeNode(name='file.txt', is_dir=False, children=[], size=0)
	

def test_update_file_node(tmpdir):
    assert SizeTree().update_filenode(SizeTree().construct_filenode(tmpdir, False)) == FileSizeNode(name='test_update_file_node0', is_dir=False, children=[], size=4096)
    assert SizeTree().update_filenode(SizeTree().construct_filenode(tmpdir, True)) == FileSizeNode(name='test_update_file_node0', is_dir=True, children=[], size=4096)
    test_node = FileSizeNode(name='test_x', is_dir=False, children=[FileSizeNode(name='subdir', is_dir=False, children=[], size=4096)], size=4096) 
    assert SizeTree().update_filenode(test_node) == FileSizeNode(name='test_x', is_dir=False, children=[FileSizeNode(name='subdir', is_dir=False, children=[], size=4096)], size=8192)
