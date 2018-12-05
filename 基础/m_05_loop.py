"""
# while循环
i = 0
while i < 3:
    # todo
    print("Hello python")
    # 计数器处理
    i += 1
"""

"""
# 1～100内的偶数相加
i = 0
s = 0
while i <= 100:
    if i % 2 == 0:
        s += i
    i += 1
print(i)
print(s)
"""

"""
i = 0
while i < 10:
    # break退出整个循环
    # if i == 3:
    #     break
    # continue退出当前循环，进入新循环的条件判断阶段
    if i == 3:
        # 如果没有这一句直接continue就会陷入死循环
        i += 1
        continue
    print(i)
    i += 1
"""

"""
# 连续输出五行* 每行逐渐递增
# *
# **
# ***
# ****
# *****
# 思路1：直接使用*字符拼接，乘行号即可，但是这只是因为这个递增比较有规律
# 思路2：使用循环嵌套
row = 1
while row <= 5:
    # print("*"*row)
    col = 1
    while col <= row:
        # 每行输出列数个，输出时不换行
        print("*",end="")
        col += 1
    # 每行完换行
    print("")
    row += 1
"""

"""
# 打印99乘法表
"""
row = 1
while row <= 9:
    # 列=1写在这里，每行开始都是从第一列开始
    col = 1
    while col <= row:
        print("%d * %d = %d" % (col,row,col*row),end="\t")
        col += 1
    print("")
    row += 1
