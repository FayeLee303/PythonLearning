# # 打开文件
# file = open("README")
# # 读取文件内容
# # text = file.read()
# while True:
#     text = file.readline()
#     # 判断一下是否读取到内容
#     if not text:
#         break
#     print(text)
# # 关闭文件
# file.close()

# 复制文件
file_read = open("README")
file_write = open("READMECOPY","w")

# text = file_read.read()
# file_write.write(text)

while True:
    text = file_read.readline()
    file_write.write(text)
    if not text:
        break

file_read.close()
file_write.close()