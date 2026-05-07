class Employee:
    def __init__(self, name, emp_id):
        self.name = name
        self.emp_id = emp_id

    def print_info(self):
        print(f"工号: {self.emp_id}, 姓名: {self.name}")

    def calculate_monthly_pay(self):
        pass # 基类不具体实现薪水计算


class FullTimeEmployee(Employee):
    def __init__(self, name, emp_id, monthly_salary):
        super().__init__(name, emp_id)
        self.monthly_salary = monthly_salary

    def calculate_monthly_pay(self):
        return self.monthly_salary


class PartTimeEmployee(Employee):
    def __init__(self, name, emp_id, daily_salary, work_days):
        super().__init__(name, emp_id)
        self.daily_salary = daily_salary
        self.work_days = work_days

    def calculate_monthly_pay(self):
        return self.daily_salary * self.work_days

if __name__ == "__main__":
    ft_emp = FullTimeEmployee("张全蛋", "F001", 8000)
    pt_emp = PartTimeEmployee("李兼职", "P001", 200, 15)

    print("--- 全职员工 ---")
    ft_emp.print_info()
    print(f"月薪: {ft_emp.calculate_monthly_pay()} 元")

    print("\n--- 兼职员工 ---")
    pt_emp.print_info()
    print(f"月薪: {pt_emp.calculate_monthly_pay()} 元")
