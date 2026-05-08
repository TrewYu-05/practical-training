data = [
    {"name": "张三丰", "phone": "13812345678", "email": "zhang@example.com"},
    {"name": "李莫愁", "phone": "13987654321", "email": "li@example.org"}
]
print("原始数据:", data)

masked_data = []
# d 表示的是列表中的每一个字典
for d in data:
    # 处理姓名
    name = d['name']
    masked_name = name[0] + '*' * (len(name) - 1) if len(name) > 1 else name
    # 处理电话号码
    phone = d['phone']
    masked_phone = phone[:3] + '****' + phone[7:] if len(phone) == 11 else phone
    # 处理邮箱地址
    email = d['email']
    # 邮箱格式的简单验证
    if '@' in email:
        local, domain = email.split('@')
        masked_local = local[0] + '***' if len(local) > 1 else local
        masked_email = masked_local + '@' + domain
    else:
        masked_email = email

    # 添加进列表中
    masked_data.append({
        'name': masked_name,
        'phone': masked_phone,
        'email': masked_email
    })

print("脱敏后数据:")
for item in masked_data:
    print(item)
