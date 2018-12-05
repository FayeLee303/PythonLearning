class SingleTonTest(object):
    # 记录第一个被创建对象的引用
    instance = None
    # 记录是否执行过初始化方法
    init_flag = False

    def __new__(cls, *args, **kwargs):
        # 创建对象时new方法会自动调用
        # object类里的__new__本来是个静态方法
        # super类里的__new__是个类方法，所以需要传递cls参数
        # super类是object类的子类，相当于它重写了__new__
        # 这里再次重写__new__方法
        # instance = super().__new__(cls)

        # 判断有没有被实例化
        if cls.instance is None:
            # 如果没有就实例化一个对象
            cls.instance = super().__new__(cls)
            print("创建对象分配空间")
        # 返回对象的引用
        return cls.instance

    def __init__(self):
        # 如果已经执行过初始化就直接返回
        if self.init_flag is True:
            return
        else:
            self.init_flag  = True
            print("初始化")

t1 = SingleTonTest()
t2 = SingleTonTest()
print(t1)
print(t2)