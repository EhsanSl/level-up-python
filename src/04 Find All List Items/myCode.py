def index_all(search_list, item):
    lst = []
    for index, val in enumerate(search_list):
        if val == item:
            lst.append([index])
        elif isinstance(search_list[index], list):
            for i in index_all(search_list[index], item):
                lst.append([index] + i)
    return lst


# commands used in solution video for reference
if __name__ == '__main__':
    example = [[[1, 2, 3], 2, [1, 3]], [1, 2, 3]]
    print(index_all(example, 2))  # [[0, 0, 1], [0, 1], [1, 1]]
    print(index_all(example, [1, 2, 3]))  # [[0, 0], [1]]
