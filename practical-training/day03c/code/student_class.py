class Student:
    def __init__(self, name, age, student_id, interests):
        self.name = name
        self.age = age
        self.student_id = student_id
        self.interests = interests

    def study(self):
        print(f"学生 {self.name} (学号: {self.student_id}) 正在努力学习。")

    def date(self, partner_name):
        print(f"{self.name} 正在和 {partner_name} 谈恋爱。")

    def fitness(self):
        print(f"{self.name} 去健身房锻炼了！兴趣之一是: {self.interests[0]}")

# 实例化学生对象
stu1 = Student("张三", 20, "S2023001", ["游泳", "打篮球"])
stu2 = Student("李四", 19, "S2023002", ["跑步", "看书"])

# 测试属性和方法
print(f"创建了学生: {stu1.name}, 年龄: {stu1.age}, 学号: {stu1.student_id}, 兴趣: {stu1.interests}")

stu1.study()
stu1.fitness()
stu1.date(stu2.name)
