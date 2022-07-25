

list1 = [1, [2], [[3]], [[[4]]], [[[[[5]]]]]]
# Try:
# lists = [0, [1, [2, [3, [4, [5]]]]]]
# lists = [0, 1, [3, [[4]]], [[[[5], [6]]]], [[[7, 8]], [9]], [[[[[10]]]]]]
# lists = ["banana",["apple"],[[1,3]],[["juice"],[12]],[[[["PC"],[8]]],["hi"]],[[[[1]]]]]

for item in list1:
    if isinstance(item, list):
        for x in range(0, len(item)):

            if isinstance(item[x], list):
                for y in range(0, len(item[x])):

                    if isinstance(item[x][y], list):
                        for z in range(0, len(item[x][y])):

                            if isinstance(item[x][y][z], list):
                                for a in range(0, len(item[x][y][z])):

                                    if isinstance(item[x][y][z][a], list):
                                        for b in range(0, len(item[x][y][z][a])):

                                            print(item[x][y][z][a][b])
                                    else:
                                        print(item[x][y][z][a])
                            else:
                                print(item[x][y][z])
                    else:
                        print(item[x][y])
            else:
                print(item[x])
    else:
        print(item)
