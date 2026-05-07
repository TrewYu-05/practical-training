weights = ["100kg", "200 kg", "50.5kg", "300g", "1.5 t"]
print("原始数据:", weights)

result = []
for w in weights:
    # 解决空格问题
    w = w.replace(' ', '')
    # 单位的转换
    if w.endswith('kg'):
        num = float(w[:-2])
        result.append(num)
    elif w.endswith('g'):
        num = float(w[:-1]) * 0.001
        result.append(num)
    elif w.endswith('t'):
        num = float(w[:-1]) * 1000
        result.append(num)

print("清洗后数据(kg):", result)
