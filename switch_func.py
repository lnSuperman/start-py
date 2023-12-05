def print_a():
    print("a")


def print_b():
    print("b")


def print_c():
    print("c")


def print_d():
    print("d")


switch = {
    90: print_a,
    80: print_b,
    70: print_c,
    60: print_d
}
if __name__ == '__main__':
    score = 90
    switch[score]()
