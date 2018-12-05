# 使用元祖返回多个值
def measure():
    """测量温度和湿度"""
    print("测量开始…")
    temp = 39
    wet = 30
    print("测量结束…")
    # 返回元祖类型变量时可以不用小括号
    # return (temp,wet)
    return temp, wet

result = measure()
print(result)
print(result[0])
print(result[1])
# 如果函数的返回值是元祖，同时希望单独的处理元祖里的数据
# 可以使用多个变量，一次接受函数的返回结果
gl_temp,gl_wet = measure()
print(gl_temp)
print(gl_wet)