from com.jqc.map.treeMap import TreeMap
from com.jqc.map.map import Visitor


def visit(key, value):
	print(key, value)
	# return True if key == 'b' else False
	return False


if __name__ == '__main__':
	visitor = Visitor(visit)
	cus_map = TreeMap()
	cus_map.put("c", 2)
	cus_map.put("a", 5)
	cus_map.put("b", 6)
	cus_map.put("a", 8)
	
	# print(cus_map)
	print('-----*****-----')
	cus_map.traversal(visitor)
