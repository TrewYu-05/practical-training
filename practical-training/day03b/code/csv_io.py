import csv
import os

os.makedirs('db', exist_ok=True)

# csv文件写入
with open('db/students.csv', 'w', encoding='utf-8', newline='') as csvfile:
    f = csv.writer(csvfile)
    f.writerow(['编号', '姓名', '年龄'])
    f.writerows([
        ['001', '坤坤', 18],
        ['002', '张三', 20]
    ])
print('CSV写入成功: db/students.csv')

# txt文件写入
with open('db/goods.txt', 'w', encoding='utf-8') as f:
    f.write('商品编号,商品名称,商品价格\n')
    f.write('001,Xiaomi 17,5499\n')
    f.write('002,huawei mate80,5699\n')
    f.write('003,iphone17,5699\n')
print('TXT写入成功: db/goods.txt')

print("--- 读取 students.csv ---")
with open('db/students.csv', 'r', encoding='utf-8') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

print("--- 读取 goods.txt ---")
with open('db/goods.txt', 'r', encoding='utf-8') as txtfile:
    lines = txtfile.readlines()
    for line in lines:
        print(line.strip())
