text = " User: JOHN_Smith; RegDate: 2023-05-12; "
print("原始字符串:", text)
print('-' * 50)

# 切片操作
# 切割（split） 把字符串切割成列表，根据指定字符进行切割
# capitalize() 首字母大写
step1 = text.strip()[:-1].split('; ')[0].split(': ')[1].capitalize()
print("用户名处理后:", step1)

# replace() 替换
# join() 前面表示把列表转成字符串后，需要使用什么字符来拼接。参数是列表
step2 = '-'.join(text.strip()[:-1].split('; ')[1].split(': ')[1].replace('-', '/').split('/')[::-1])
print("日期处理后:", step2)

# 输出结果
result = f'User: {step1}; RegDate: {step2}'
print("最终输出:", result)
