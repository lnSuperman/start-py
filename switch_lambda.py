score = 90
switch = {
    90: lambda: print("a"),
    80: lambda: print("b"),
    70: lambda: print("c"),
    60: lambda: print("d")

}
if __name__ == '__main__':
    switch[score]()
