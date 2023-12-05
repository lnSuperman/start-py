from typing import List, Dict, Tuple

if __name__ == '__main__':
    #  海象运算符 >3.8 可以为我们的表达式赋值
    course_list = ['flask', 'django', 'mysql']
    # if len(course_list) >= 3:
    #     print("课程较多，{}".format(len(course_list)))
    # := 优先级小于 >=
    # if (course_size := len(course_list)) >= 3:
    #     print("课程较多，{}".format(course_size))
    power = [course_size := len(course_list), course_size ** 2, course_size ** 3]
    print(power)

    import re

    desc = "bobby:18"
    if m := re.match("bobby:(.*)", desc):
        age = m.group(1)
        print(age)
    # 不能像go直接复制
    age: int = 18
    print(age)
    money: float = 20.50
    b: bytes = b'test'
    name: str = 'Test Liu'
    # course: list = ['flask', 'django', 'mysql']
    course: List[str] = ['flask', 'django', 'mysql', 'Test']
    # course.append(1)   ide提示错误但不会仍会操作
    print(course)

    user_info: Dict[str, int] = {"Test": 18}
    print(user_info)
    names: Tuple[int, ...] = (1, 2, 3)  # ...指明tuple内部不止一个int，多个int不用... ide会提示
    print(names)
 