from functools import wraps
from typing import get_type_hints
from inspect import getfullargspec


def validate_input(obj, **kwargs):
    hints = get_type_hints(obj)
    for obj_val_name, obj_val_type in hints.items():
        if obj_val_name == "return":
            continue
        if not isinstance(kwargs[obj_val_name], obj_val_type):
            raise TypeError("参数{}类型错误,应该是{}类型".format(obj_val_name, obj_val_type))


def type_check(decorator):
    @wraps(decorator)
    def wrapped_decorator(*args, **kwargs):
        func_args = getfullargspec(decorator)[0]
        kwargs.update(dict(zip(func_args, args)))
        validate_input(decorator, **kwargs)
        return decorator(**kwargs)

    return wrapped_decorator


@type_check
def add(a: int, b: int) -> int:
    return a + b


if __name__ == '__main__':
    # print(add(1, "1"))
    # validate_input(add)

    # print(get_type_hints(add))
    # print(add.__annotations__)
    name = "liu"
    for index,value in enumerate(name):
        print(index,value)

