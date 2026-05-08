# 数据结构：列表+字典
product = [
    {'id': '001', 'title': 'huawei mate80', 'price': 5899, 'nums': 2},
    {'id': '002', 'title': 'Xiaomi 17', 'price': 4899, 'nums': 1}
]

# 添加商品
def add_goods():
    id_ = input('请输入商品编号:')
    title = input('请输入商品的标题:')
    price = float(input('请输入商品的价格:'))
    nums = int(input('请输入商品的数量:'))
    # 创建商品
    new_goods = {
        'id': id_,
        'title': title,
        'price': price,
        'nums': nums
    }
    # 添加进商品列表
    product.append(new_goods)
    print(f'添加商品成功，商品标题是:{title}')
    print(f'商品列表：{product}')

# 删除商品
def delete_goods(id_):
    for item in product:
        if item['id'] == id_:
            product.remove(item)
            print('删除成功')
            break
    else:
        print('删除的商品不存在')
    print(f'商品列表：{product}')

# 修改商品
def modify_goods(id_, title=None, price=None):
    for item in product:
        if item['id'] == id_:
            if title is not None:
                item['title'] = title
            if price is not None:
                item['price'] = float(price)
            break
    print(f'商品列表：{product}')

print("当前商品列表:", product)
modify_goods('001', '魅族', '2899')
delete_goods('002')
