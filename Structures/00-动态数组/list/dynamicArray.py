class DynamicArray(object):
    
    def __init__(self, capacity=5):
        """
        初始化函数
        :param capacity: 数组默认容量
        """
        # 动态数组大小初始化为0
        self.__size = 0  # size
        # self.__elements = [None] * (5 if capacity < 5 else capacity)
        # 初始化动态数组
        self.__elements = [None] * max(5, capacity)
    
    def __str__(self):
        """
        自定义字符串的输出, 类似下边这样输出
        size: 20, capacity: 22
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10,]
        :return: 字符串
        """
        return f"size: {self.__size}, capacity: {len(self.__elements)}\n{str(self.__elements[:self.__size])}"
    
    def clear(self):
        """
        清空动态数组
        :return:
        """
        self.__elements = [None for _ in self.__elements]
        self.__size = 0
    
    def size(self):
        """
        返回动态数组大小
        :return: 返回len(self.__elements)
        """
        return self.__size
    
    def is_empty(self):
        """
        判断数组是否为空
        :return: bool 值
        """
        return self.__size == 0
    
    def contains(self, element):
        """
        判断是否包含某个元素
        :param element: 元素
        :return:
        """
        return self.index_of(element) != -1
    
    def add(self, element):
        """
        添加元素
        :param element: 待添加的元素
        :return: None(空)
        """
        self.insert(self.__size, element)
    
    def insert(self, index, element):
        """
        插入元素
        :param index: 待插入索引
        :param element: 待添加的元素
        :return:
        """
        # 添加之前 先检查索引是否会越界
        self.__range_check_add(index)
        # 添加size会增加1,所以直接判断size + 1和capacity比较
        self.__ensure_capacity(self.__size + 1)
        for i in range(self.__size - 1, index - 1, -1):
            self.__elements[i + 1] = self.__elements[i]
        self.__elements[index] = element
        self.__size += 1
    
    def get(self, index=0):
        """
        根据索引获取元素
        :param index: 索引下标
        :return:
        """
        self.__range_check(index)
        
        return self.__elements[index]
    
    def set(self, index, element):
        """
        更新指定位置的值
        :param index:
        :param element:
        :return: 返回原来的值
        """
        self.__range_check(index)
        old_val = self.__elements[index]
        self.__elements[index] = element
        return old_val
    
    def remove(self, index=0):
        """
        删除指定索引位置的元素
        :param index: 索引
        :return: 返回删除的元素
        """
        # 检查是否越界
        self.__range_check(index)
        old_val = self.__elements[index]
        # 当前索引后面的元素往前挪动
        for i in range(index+1, self.__size):
            self.__elements[i-1] = self.__elements[i]
        self.__elements[self.__size - 1] = None
        self.__size -= 1
        return old_val
    
    def index_of(self, element):
        """
        判断element 是否存在
        :param element:
        :return: 如果找到该元素,返回该元素的索引; 没有找到,返回-1
        """
        
        for index, item in enumerate(self.__elements):
            if element == item:
                return index
        return -1
    
    def __ensure_capacity(self, capacity):
        """
        扩容
        :param capacity:
        :return:
        """
        old_len = len(self.__elements)
        if old_len >= capacity:
            return
        new_capacity = old_len + (old_len >> 1)
        print('扩容', old_len, new_capacity)
        new_data = [None] * new_capacity
        new_data[:self.__size] = self.__elements[:self.__size]
        self.__elements = new_data
    
    def __range_check(self, index):
        """
        索引是否越界判断
        :param index:
        :return:
        """
        if index < 0 or index >= self.__size:
            raise NameError('数组越界 Index: %d, Size:%d'.format(index, self.__size))
    
    def __range_check_add(self, index):
        """
        索引是否越界判断
        :param index:
        :return:
        """
        if index < 0 or index > self.__size:
            raise NameError('数组越界 Index: %d, Size:%d'.format(index, self.__size))
