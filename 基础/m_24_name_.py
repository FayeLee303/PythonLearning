# 直接执行的代码不是向外界提供的工具
# 文件被导入时，此类代码不应该被执行


def say_hello():
    print("hello")

# 如果直接执行模块，得到__main__
# print(__name__)

if __name__ == "__main__":
    # 测试代码
    # 被导入到其他文件时不希望被执行
    # 自己运行本文件可以被执行
    print("__name__")
    say_hello()