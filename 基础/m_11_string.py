str1 = "hello python"
str2 = '外号是"大西瓜"'
print(str2)
for char in str2:
    print(char)

# 判断空白字符
str_space = "  "
print(str_space.isspace())

# 判断是否只有数字
# 都不能判断小数
str_num = "1"
str_num = "1.1"
str_num = "(1)"
str_num = "\u00b2"
print(str_num.isdecimal())
print(str_num.isdigit())
print(str_num.isnumeric())

# 指定字符串
str3 = "hello world"
print(str3.startswith("hello"))
print(str3.endswith("hello"))
print(str3.find("ll0"))
print(str3.index("llo"))

# 替换
# replace会返回一个新的字符串，而不是对原来的字符串修改
str3.replace("hello","goodbye")
print(str3)
str4 = str3.replace("hello","goodbye")
print(str4)

poem = ["\tddddd",
        "dfsffs\n",
        "aasduh",
        "fnjvxbc"
    ]
for poem_str in poem:
    print("|%s|" % poem_str.strip().center(10," "))

str5 = "dsoifou osdifhs\tdgohsdsoighwgi"
# 拆分得到一个列表
str5_list = str5.split()
result = "".join(str5_list)
print(result)

# 切片
str_num = "0123456789"
print(str_num[2:6])
print(str_num[:6])
print(str_num[2:])
print(str_num[:])
# 每隔一位取一个
print(str_num[::2])
# 从索引1开始每隔一位取一个
print(str_num[1::2])
# 倒数第一个字符
print(str_num[-1])
# 从第二位到倒数第二个字符
print(str_num[2:-1])
# 末尾两个字符
print(str_num[-2:])
# 字符串的逆序 从右向左切片
print(str_num[-1::-1])
print(str_num[::-1])

