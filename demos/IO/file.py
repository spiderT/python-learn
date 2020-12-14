# 打开一个文件
# fo = open("./a.txt", "w")
fo = open("./a.txt", "r+")
print("文件名: ", fo.name)
print("是否已关闭 : ", fo.closed)
print("访问模式 : ", fo.mode)

# fo.write( "举头望明月!\n低头思故乡!\n")

str = fo.read(10)
print("读取的字符串是 : ", str)

# 关闭打开的文件s
fo.close()
