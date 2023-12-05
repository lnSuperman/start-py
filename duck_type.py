# go 类似鸭子类型
# 什么是鸭子类型 什么是协议


class Company(object):
    def __init__(self, employee_list):
        self.employee_list = employee_list

    def __iter__(self):
        return iter(self.employee_list)


if __name__ == '__main__':
    employee_list = ["zhangsan", "lisi", "wangermazi"]
    c = Company(employee_list)
    for i in c:
        print(i)
