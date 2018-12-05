name_list =["a","b","c"]
# 取值和取索引
# 取值时不能超出索引范围
print(name_list[2])
# 取索引时值必须存在
print(name_list.index("a"))
# 修改
# 修改时不能超过索引范围
name_list[1] = "sss"
# 增加
# 在末尾追加
name_list.append("c")
# 在指定索引位置插入
name_list.insert(2,"fff")
# 合并两个列表，追加到当前列表的末尾
name_list_2 = ["rrr","ttt"]
name_list.extend(name_list_2)
# 删除指定数据
name_list.remove("c")
# 出栈，默认删除最后一个元素，也可以删除指定位置的元素
name_list.pop()
name_list.pop(3)
# 清空
# name_list.clear()
# del关键字本质上是把一个变量从内存中删除，也可以达到把元素删除的效果
del name_list[1]
# 注意如果使用del关键字把变量删除，后续就不能在使用这个变量了
name = "aaa"
del name
# 列表长度
print(len(name_list))
# 统计某个数据出现的次数，值必须存在
print(name_list.count("a"))
num_list = [7,9,5,4,3]
# 升序
num_list.sort()
print(num_list)
# 降序
num_list.sort(reverse= True)
print(num_list)
# 反转
num_list.reverse()
print(num_list)
# 使用迭代遍历列表
name_list = ["张三","李四","王五"]
# 这里的my_name只在循环体里有效，用来循环取到列表里的每一个元素
for my_name in name_list:
    print("我的名字叫：%s" % my_name)