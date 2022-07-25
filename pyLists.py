

lists = [1, [2], [[3]], [[[4]]], [[[[[5]]]]]]
# Try:
# lists = [0, [1, [2, [3, [4, [5]]]]]]
# lists = [0, 1, [3, [[4]]], [[[[5], [6]]]], [[[7, 8]], [9]], [[[[[10]]]]]]
# lists = ["banana",["apple"],[[1,3]],[["juice"],[12]],[[[["PC"],[8]]],["hi"]],[[[[1]]]]]

for v in lists:
    if isinstance(v, list):
        for x in range(0, len(v)):

            if isinstance(v[x], list):
                for y in range(0, len(v[x])):

                    if isinstance(v[x][y], list):
                        for z in range(0, len(v[x][y])):

                            if isinstance(v[x][y][z], list):
                                for a in range(0, len(v[x][y][z])):

                                    if isinstance(v[x][y][z][a], list):
                                        for b in range(0, len(v[x][y][z][a])):

                                            print(v[x][y][z][a][b])
                                    else:
                                        print(v[x][y][z][a])
                            else:
                                print(v[x][y][z])
                    else:
                        print(v[x][y])
            else:
                print(v[x])
    else:
        print(v)
