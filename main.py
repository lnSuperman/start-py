from distutils.util import strtobool

if __name__ == '__main__':
    # my_list = ['tom','test','run']
    # for _, item in enumerate(my_list):
    #     print(item)
    data = "21"
    int_data = int(data, 16)
    print(type(int_data), int_data)
    # 非null 0 "" 均为true "false" 也转换为true
    str_bool = "false"
    bool_res = bool(str_bool)
    print(bool_res, type(bool_res))
    # strtobool
    # 1 true True 均返回1
    # false 0 False 均返回0
    # 其他报错
    res = strtobool("False")
    print(type(res), res)
