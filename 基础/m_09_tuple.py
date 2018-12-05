info_tuple = ("sss",34,"rfr",56.3)
# 取值
print(info_tuple[3])
# 取索引
print(info_tuple.index("sss"))
# 统计某个值的次数
print(info_tuple.count("sss"))
# 求长度
len(info_tuple)
# 循环遍历
for my_info in info_tuple:
    # 元组中通常保存的数据类型是不同的
    print(my_info)
# 格式化字符串输出
man_tuple = ("小明",18,1.75)
print("%s 年龄是 %d 身高是 %.2f" % man_tuple)
man_str = "%s 年龄是 %d 身高是 %.2f" % man_tuple
print(man_str)