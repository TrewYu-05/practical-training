names = ["张三(Tom)", "李四(Lucy)", "王五(Bob)"]
english_names = []
for name in names:
    if '(' in name and ')' in name:
        start = name.find('(') + 1
        end = name.find(')')
        en_name = name[start:end]
        english_names.append(en_name)
print("原始数据:", names)
print("提取的英文名:", english_names)
