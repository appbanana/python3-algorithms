# import typing
from com.jqc.binaryTree.binarySearchTree import BinarySearchTree


# 测试闭包
def test(number: int):
	def test_in(num_in: int):
		return number + num_in
	
	return test_in


def test1():
	"""
	测试递归和非递归 前，中，后序遍历
	:return:
	"""
	# 递归来实现
	# 前序遍历
	# [5, 3, 41, 10, 28, 19, 12, 21, 81, 55, 79, 86]
	print(bst.preorder())
	print('*' * 30)
	
	# 中序遍历
	# [3, 5, 10, 12, 19, 21, 28, 41, 55, 79, 81, 86]
	print(bst.inorder())
	print('*' * 30)
	
	# 后序遍历
	# [3, 12, 21, 19, 28, 10, 79, 55, 86, 81, 41, 5]
	print(bst.postorder())
	print('*' * 30)
	
	# 二叉树 非递归实现
	# 前序遍历
	# [5, 3, 41, 10, 28, 19, 12, 21, 81, 55, 79, 86]
	print(bst.preorder_traversal())
	print('*' * 30)
	
	# 中序遍历
	# [3, 5, 10, 12, 19, 21, 28, 41, 55, 79, 81, 86]
	print(bst.inorder_traversal())
	print('*' * 30)
	
	# 后序遍历
	# [3, 12, 21, 19, 28, 10, 79, 55, 86, 81, 41, 5]
	print(bst.postorder_traversal())
	print('*' * 30)
	
	# 层序遍历
	# [5, 3, 41, 10, 81, 28, 55, 86, 19, 79, 12, 21]
	print(bst.level_order_tranversal())


if __name__ == '__main__':
	# result = test("1")
	# print(result)
	# print(result('10'))
	test_array = [5, 41, 81, 86, 55, 10, 28, 19, 79, 12, 3, 21]
	bst = BinarySearchTree()
	for item in test_array:
		bst.add(item)
	
	"""
	L---3
	5
	R---L---10
	R---L---R---L---L---12
	R---L---R---L---19
	R---L---R---L---R---21
	R---L---R---28
	R---41
	R---R---L---55
	R---R---L---R---79
	R---R---81
	R---R---R---86
	"""
	print(bst)
	# 测试递归和非递归 前，中，后序遍历
	# test1()
	print(bst.is_complete())
	