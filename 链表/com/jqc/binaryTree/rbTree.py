from .binaryTree import Node
from .bbst import BBST
from enum import Enum
from com.jqc.queue.queue import Queue


class Color(Enum):
	RED = 0
	BLACK = 1


class RBNode(Node):
	def __init__(self, element, parent):
		"""
		自定义初始化
		:param element: 元素
		:param parent: 父节点
		"""
		super().__init__(element, parent)
		self.color = Color.RED
	
	def __str__(self):
		string = ''
		if self.color == Color.RED:
			string = 'R_'
		return string + str(self.element)


class RBTree(BBST):
	def __str__(self):
		string = ''
		queue = Queue()
		queue.en_queue(self._root)
		level_size = 1
		while not queue.is_empty():
			node = queue.de_queue()
			string += str(node)
			level_size -= 1
			string += ','
			if node.left is not None:
				queue.en_queue(node.left)
			if node.right is not None:
				queue.en_queue(node.right)
			if level_size == 0:
				level_size = queue.size()
				string += '\n'
		return string
	
	def create_node(self, element, parent) -> Node:
		"""
		重写父类方法，返回RBNode类型的
		:param element:
		:param parent:
		:return:
		"""
		return RBNode(element, parent)
	
	def after_add(self, node: RBNode) -> None:
		"""
		添加节点之后，修复红黑树的性质
		:param node:
		:return:
		"""
		parent = node.parent
		
		if parent is None:
			# node 是根节点
			self.__black(node)
			return
		
		if self.__is_black(parent):
			# 父节点是黑色 不做任何处理
			return
		# 父节点是红色的
		uncle = parent.sibling()
		grand = parent.parent
		
		if self.__is_red(uncle):
			# 叔父节点是红色，父亲和叔父节点染黑， grand节点染红，向上合并
			self.__black(parent)
			self.__black(uncle)
			
			self.after_add(self.__red(grand))
			return
		
		# 叔父节点是黑色
		if parent.is_left_child():
			# L
			self.__red(grand)
			if node.is_left_child():
				# LL
				# self.__red(grand)
				self.__black(parent)
			# self._rotate_right(grand)
			else:
				# LR
				# self.__red(grand)
				self.__black(node)
				self._rotate_left(parent)
			# self._rotate_right(grand)
			self._rotate_right(grand)
		else:
			# R
			self.__red(grand)
			if node.is_right_child():
				# RR
				# self.__red(grand)
				self.__black(parent)
			# self._rotate_left(grand)
			else:
				# RL
				# self.__red(grand)
				self.__black(node)
				self._rotate_right(parent)
			# self._rotate_left(grand)
			self._rotate_left(grand)
	
	def __red(self, node: Node) -> Node:
		"""
		节点染红
		:param node:
		:return:
		"""
		return self.__color(node, Color.RED)
	
	def __black(self, node: Node) -> Node:
		"""
		节点染黑
		:param node:
		:return:
		"""
		return self.__color(node, Color.BLACK)
	
	@staticmethod
	def __color_of(node: Node) -> Color:
		"""
		返回传入节点的颜色
		:param node:
		:return:
		"""
		return Color.BLACK if node is None else node.color
	
	@staticmethod
	def __color(node: Node, color: Color) -> Node:
		if node is None:
			return None
		node.color = color
		return node
	
	def __is_black(self, node: Node) -> bool:
		"""
		判断节点是否是黑色
		:param node:
		:return:
		"""
		return self.__color_of(node) == Color.BLACK
	
	def __is_red(self, node: Node) -> bool:
		"""
		判断节点是否是红色
		:param node:
		:return:
		"""
		return self.__color_of(node) == Color.RED
