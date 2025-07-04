class Point:
    def __init__(self, x, y):  # 魔法方法（Magic Method），
        # 它在创建类的实例（对象）时自动调用，主要用于初始化对象的属性。
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):  # 类属性定义
        return cls(0, 0)

    def draw(self):  # 实例属性定义
        print(f"Point({self.x}, {self.y})")


point = Point.zero()
point.draw()
point.x = 9
