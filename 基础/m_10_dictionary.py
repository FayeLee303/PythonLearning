xiaoming_dict = {"name":"小米姑娘",
            "age":18,
            "gender":True,
            "height":158}
print(xiaoming_dict)
# 取值
print(xiaoming_dict["name"])
# 修改
xiaoming_dict["age"] = 13
# 删除
xiaoming_dict.pop("age")
# 统计键值对数量
len(xiaoming_dict)
# 合并
temp_dict = {"height":180}
xiaoming_dict.update(temp_dict)
# 循环遍历
for key in xiaoming_dict:
    print("%s - %s" %(key,xiaoming_dict[key]))

# 字典是无序的，列表是有序的
card_list = [
    {"name":"ss",
     "age":13,
     "number":324},
    {"name":"srr",
     "age":12,
     "number":434},
    {"name":"aaf",
     "age":19,
     "number":308}
]
for card_info in card_list:
    print(card_info)