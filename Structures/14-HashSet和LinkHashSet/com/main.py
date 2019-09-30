import unittest
from com.jqc.map.map import Visitor
from com.jqc.set.hashSet import HashSet
from com.jqc.set.linkHashSet import LinkHashSet


def visit(key, value):
    print(key, "_", value)
    return False


def test1():
    # 测试HashSet
    array = [37, 21, 31, 41, 97, 95, 52, 42, 83, 21, 31]
    hash_set = HashSet()
    for index, item in enumerate(array):
        hash_set.add(item)
    
    print('***-----****' * 10)
    visitor = Visitor(visit)
    hash_set.traversal(visitor)
    print(hash_set.remove(31))
    print('***-----****' * 10)
    # visitor = Visitor(visit)
    hash_set.traversal(visitor)


if __name__ == '__main__':
    
    # 测试HashSet
    # test1()
    # 测试LinkHashSet
    array = [37, 21, 31, 41, 97, 95, 52, 42, 83, 21, 31]
    hash_set = LinkHashSet()
    for index, item in enumerate(array):
        hash_set.add(item)
    
    print('***-----****' * 10)
    visitor = Visitor(visit)
    hash_set.traversal(visitor)
    print(hash_set.remove(31))
    print('***-----****' * 10)
    # visitor = Visitor(visit)
    hash_set.traversal(visitor)
