char_list = ['a', 'b', 'c', 'c', 'd', 'd', 'd']
# 有多少个不重复的字符,但是顺序是乱的
print(set(char_list))
print(type(set(char_list)))
unique_char = set(char_list)
unique_char.add("x")
print(unique_char)
# 加重复字符会忽略
unique_char.add("a")
print(unique_char)
# 删除元素，使用remove删除不存在的元素会报错
# 使用discard删除不存在的元素不会报错
unique_char.remove("a")
unique_char.discard("y")
print(unique_char)

sentence = 'Welcome Back to This Tutorial'
print(set(sentence))

#  看两个set之间有什么不同
print(unique_char.difference(set(sentence)))
# 看两个set之间有什么交集
print(unique_char.intersection(set(sentence)))