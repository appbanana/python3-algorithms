from com.jqc.binaryTree.rbTree import RBTree
import const
def test():
	const.PI = 3.14
	print(const.PI)
	const.PI = 3.1415
	print(const.PI)
	pass


if __name__ == '__main__':
	test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	# test_array = [43, 21, 34, 81, 32, 46, 99, 69, 80, 67, 47]
	rbTree = RBTree()
	for item in test_array:
		rbTree.add(item)
	"""
	41,
	10,81,
	5,R_19,55,86,
	R_3,12,28,R_79,
	R_21,
	"""
	# 自定义输出，使用的是层序遍历
	# 这个要结合MJ老师的这个网站来验证是否正确 参考网址：http://520it.com/binarytrees/
	print(rbTree)
	
	# 第一组测试数据
	# [41, 10, 81, 5, 19, 55, 86, 3, 12, 28, 79, 21]
	# print(rbTree.level_order_tranversal())

	# 第二组数据 测试结果
	# [46, 34, 69, 21, 43, 67, 81, 32, 47, 80, 99]
	# print(rbTree.level_order_tranversal())
	
	# [47, 34, 69, 21, 43, 67, 81, 32, 80, 99]
	# rbTree.remove(46)
	# print(rbTree.level_order_tranversal())
	
	# [46, 34, 80, 21, 43, 67, 81, 32, 47, 99]
	# rbTree.remove(69)
	# print(rbTree.level_order_tranversal())
	
	# [46, 34, 69, 21, 43, 67, 81, 32, 47, 80]
	# rbTree.remove(99)
	# print(rbTree.level_order_tranversal())
