from com.jqc.single.singleLinkList import SingleLinkList
from com.jqc.dynamicArray import DynamicArray
from com.jqc.linkList import LinkList

def test():
	# test_arr = [1, 2, 3, 6, 5, 4, 9, 8, 7]
	test_arr = [1, 2, 3, 6, 5, 4, None, 8, 7]
	link = SingleLinkList()
	for item in test_arr:
		link.add(item)
	print(link)
	print(len(test_arr))
	print(link.size())
	print(link)
	print(link.remove(0))
	print(link)
	print(link.remove(3))
	print(link)
	print(link.index_of(None))
	print(link.contains(None))
	print(link.set(3, 66))
	print(link)
	print(link.remove(link.size() - 1))
	print(link)


def test2():
	array = DynamicArray()
	for i in range(20):
		array.add(i)
	
	print(array)
	print(array.size())
	# array.clear()
	print('*****' * 10)
	# print(array)
	# 	# print(array.remove(0))
	print(array.remove(0))
	print(array.remove(array.size() - 1))
	print('****' * 10)
	print(array.set(0, 66))
	print(array)
	print('****' * 10)
	print(array.get(1))


if __name__ == '__main__':
	# 测试单链表
	# test()
	# 测试封装继承后的动态数组
	# test2()
	double_list = LinkList()
	print(double_list.clear())
