from py_god import god



if __name__ == '__main__':
    headers = god.CreateHeader("a", "b")
    keys = god.SliceStrings(["1", "2", "3"])
    values = god.SliceStrings(["a", "b", "c"])
    headers = god.CreateHeaderS(keys, values)
    god.Download("a", "b", 1, 2, 3, 4,5, True,headers, lambda a : print(a))