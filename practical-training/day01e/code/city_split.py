locations = ["北京市-海淀区", "上海市-浦东新区", "广州市-天河区"]
print("原始数据:", locations)

cities = []
districts = []

for loc in locations:
    parts = loc.split('-')
    if len(parts) == 2:
        cities.append(parts[0])
        districts.append(parts[1])

print("cities =", cities)
print("districts =", districts)
