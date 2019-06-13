"""
二叉搜索树
"""

# from typing import Callable, TypeVar, Generic
#
# T = TypeVar('T')

from com.jqc.stack.stack import Stack
from com.jqc.queue.queue import Queue


class Node(object):
	def __init__(self, element, parent) -> None:
		"""
		自定义初始化
		:param element: 元素
		:param parent: 父节点
		"""
		self.element = element
		self.parent = parent
		self.left = None
		self.right = None
	
	def __str__(self):
		parent_string = 'none'
		if self.parent is not None:
			parent_string = str(self.parent.element)
		return str(self.element) + '_p(' + parent_string + ')'
	
	def is_leaf(self) -> bool:
		"""
		判断是否是叶子节点
		:return:
		"""
		return self.left is None and self.right is None
	
	def has_two_children(self) -> bool:
		"""
		判断是否是度为2的节点
		:return:
		"""
		return self.left is not None and self.right is not None


class BinarySearchTree(object):
	
	# def __init__(self, callable: Callable[[], str]):
	# 	self.__fist = None
	# 	self.__callable = callable
	
	def __init__(self):
		self.__size = 0
		self.__root = None
	
	def __str__(self):
		container = []
		self.__to_string(self.__root, container, '')
		string = ''
		for item in container:
			string += item
		return string
	
	def __to_string(self, node: Node, container: list, prefix: str):
		if node is None:
			return
		self.__to_string(node.left, container, prefix + 'L---')
		container.append(prefix)
		container.append(str(node.element))
		container.append('\n')
		self.__to_string(node.right, container, prefix + 'R---')
	
	def size(self) -> int:
		"""
		返回二叉树长度
		:return:
		"""
		return self.__size
	
	def is_empty(self) -> bool:
		"""
		判断二叉树是否为空
		:return:
		"""
		return self.__size == 0
	
	def clear(self) -> None:
		"""
		清空
		:return:
		"""
		self.__size = 0
		self.__root = None
	
	def contains(self, element) -> bool:
		"""
		是否包含某个元素
		:param element:
		:return:
		"""
		print(element)
		return True
	
	def add(self, element) -> None:
		"""
		添加元素
		:param element:
		:return:
		"""
		self.__element_not_none_check(element)
		# 添加第一个节点 第一个节点即为根节点
		if self.__root is None:
			self.__root = Node(element, None)
			self.__size += 1
			return
		
		# 不是第一个节点
		node = self.__root
		while node is not None:
			# 暂时保存上一个节点 上一个节点即为下一个的父节点 下面会用到
			parent = node
			# 记录比较的大小
			cmp = element - node.element
			if cmp > 0:
				# 大于 往右子树找
				node = node.right
			elif cmp < 0:
				# 小于0 往左子树找
				node = node.left
			else:
				return
		new_node = Node(element, parent)
		
		if cmp > 0:
			parent.right = new_node
		else:
			parent.left = new_node
		self.__size += 1
	
	def remove(self, element) -> None:
		"""
		删除元素
		:param element:
		:return:
		"""
		pass
	
	def preorder(self):
		"""
		前序 采用递归来实现
		:return:
		"""
		if self.__root is None:
			return
		container = []
		self.__preorder_recursion(self.__root, container)
		return container
	
	def __preorder_recursion(self, node: Node, array: list):
		"""
		递归实现前序遍历
		:param node:
		:param array:
		:return:
		"""
		if node is None:
			return
		array.append(node.element)
		self.__preorder_recursion(node.left, array)
		self.__preorder_recursion(node.right, array)
	
	def inorder(self):
		"""
		中序递归实现
		:return:
		"""
		if self.__root is None:
			return
		container = []
		self.__inorder_recursion(self.__root, container)
		return container
	
	def __inorder_recursion(self, node: Node, array: list):
		if node is None:
			return
		self.__inorder_recursion(node.left, array)
		array.append(node.element)
		self.__inorder_recursion(node.right, array)
	
	def postorder(self):
		"""
		后序递归实现
		:return:
		"""
		if self.__root is None:
			return
		container = []
		self.__postorder_recursion(self.__root, container)
		return container
	
	def __postorder_recursion(self, node: Node, array: list):
		if node is None:
			return
		self.__postorder_recursion(node.left, array)
		self.__postorder_recursion(node.right, array)
		array.append(node.element)
	
	def preorder_traversal(self):
		"""
		前序
		:return:
		"""
		if self.__root is None:
			return
		
		container = []
		stack = Stack()
		stack.push(self.__root)
		
		while not stack.is_empty():
			node = stack.pop()
			container.append(node.element)
			if node.right is not None:
				stack.push(node.right)
			if node.left is not None:
				stack.push(node.left)
		return container
	
	def inorder_traversal(self):
		"""
		中序遍历
		:return:
		"""
		if self.__root is None:
			return
		
		container = []
		stack = Stack()
		curr = self.__root
		while curr or not stack.is_empty():
			if curr is not None:
				stack.push(curr)
				curr = curr.left
			else:
				node = stack.pop()
				container.append(node.element)
				curr = node.right
		return container
	
	def postorder_traversal(self):
		"""
		后序遍历
		:return:
		"""
		if self.__root is None:
			return
		
		container = []
		stack = Stack()
		stack.push(self.__root)
		prev = None
		while not stack.is_empty():
			# 取出栈最顶端的元素
			node = stack.top()
			if node.is_leaf() or (prev and prev.parent == node):
				prev = stack.pop()
				container.append(prev.element)
			else:
				if node.right is not None:
					stack.push(node.right)
				if node.left is not None:
					stack.push(node.left)
		return container
	
	def level_order_tranversal(self):
		"""
		层序遍历
		:return:
		"""
		if self.__root is None:
			return
		container = []
		queue = Queue()
		queue.en_queue(self.__root)
		# 如果队列不为空 进入循环
		while not queue.is_empty():
			node = queue.de_queue()
			container.append(node.element)
			if node.left is not None:
				queue.en_queue(node.left)
			if node.right is not None:
				queue.en_queue(node.right)
		
		return container
	
	def is_complete(self):
		"""
		是否是完全二叉树
		:return:
		"""
		if self.__root is None:
			return False
		
		queue = Queue()
		queue.en_queue(self.__root)
		is_leaf = False
		while not queue.is_empty():
			node = queue.de_queue()
			if is_leaf and not node.is_leaf():
				return False
			
			if node.left is not None:
				# 左子树不为空 入队
				queue.en_queue(node.left)
			elif node.right is not None:
				# 能走到这里 说左子树为空，右子树不为空， 则不是完全二叉树
				return False
			
			if node.right is not None:
				# 如果右子树不为空，入队
				queue.en_queue(node.right)
			else:
				# 如果右子树为空，则后面的节点必须都是叶子节点
				is_leaf = True
			
		return True
	
	@staticmethod
	def __element_not_none_check(element):
		"""
		校验传入的元素
		:param element:
		:return:
		"""
		if element is None:
			raise NameError('element 不能为None')
