# from<库名>import<函数名>
# from stocker import Stocker

print("HELLO WORLD!")

'''
pycharm快捷键
ctrl+y 删除一行
'''
i = 1
print(i)

# 用缩进代表代码块
flag = True

if flag:
    print(123)
    print(222)
else:
    if False:
        print(111)

print("shahdoais")

# 用 \ 来进行多行拼接
i1 = 1
i2 = 2
i3 = i1 + \
     i2
print(i3)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)
total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']

# 字符串截取
str1 = 'Runoob'

print(str1)  # 输出字符串
print(str1[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str1[0])  # 输出字符串第一个字符
print(str1[2:5])  # 输出从第三个开始到第五个的字符
print(str1[2:])  # 输出从第三个开始的后的所有字符
print(str1 * 2)  # 输出字符串两次
print(str1 + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

# 等待用户输入
# input("\n\n按下 enter 键后退出。")

if flag:
    print(1)
elif False:
    print(2)
else:
    print(3)

# end = null
# print('结果是：' + end)
end = '123'
print('结果是：' + end)
scc = 123
print('结果是：' + str(scc))

print(str1)

'''
在函数中调用其他函数，不需要定义在前，调用在后
而实际的函数调用执行操作，就一定要先定义后调用
'''
def orderTest():
    str1 = '三生三世'
    print("123")
    orderTest2(str1)


def orderTest2(key):
    print(key)

orderTest()
