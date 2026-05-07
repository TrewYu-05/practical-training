text = 'abcdffqdafg'
print("原始字符串:", text)

result = {}
for char in text:
    if char in result:
        result[char] += 1
    else:
        result[char] = 1

print("统计结果:")
for k, v in result.items():
    print(f"{k}: {v}")
