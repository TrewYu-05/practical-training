url = "https://api.example.com/v1/users?name=Alice&age=30&city=Beijing"
print("原始URL:", url)

if '?' in url:
    query_str = url.split('?')[1]  # name=Alice&age=30&city=Beijing
    # 把字符串转成字典形式
    params = {}
    # 先进行切割处理
    items = query_str.split('&')   # ['name=Alice', 'age=30', 'city=Beijing']
    # 遍历操作
    for it in items:
        # name=Alice
        # age=30
        # city=Beijing
        key, value = it.split('=')
        params[key] = value

    print("提取的参数字典:", params)
