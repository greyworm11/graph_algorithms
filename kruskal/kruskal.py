V = {} # V dictionary: V : parent vertex

def find_set(x): # find parent of x
    while V[x] != x:
        x = V[x]
    return x


def union_set(x,y): # union of x and y, make one parent
    x,y = map(find_set, (x, y))
    V[y] = x


if __name__ == "__main__":
    file = open('input_10.in', 'r')
    E = list()
    try:
        graph_order = file.readline().split()[0]
        graph_order = int(graph_order)
        FinalMatrix = [[0] * graph_order for _ in range(graph_order)]
        # print(graph_order)
        line_number = 1
        for lines in file.readlines():
            i = line_number + 1
            while i <= graph_order:
                listOfWeights = lines.split()
                if int(listOfWeights[i-1]) != 0:
                    edge = [line_number, i, int(listOfWeights[i-1])]
                    V[i] = i
                    V[line_number] = line_number
                    E.append(tuple(edge))
                i += 1
            line_number += 1
        print(E)
        E = sorted(E, key=lambda x: x[-1])
        print(E)
    finally:
        file.close()

    min_tree = []
    min_weight = 0
    for x, y, w in E:
        if (find_set(x) != find_set(y)):
            min_weight += w
            min_tree.append( (x, y, w) )
            union_set(x,y)
    print(min_weight)
    fileOut = open('input_10.out', 'w')
    min_tree_save = min_tree
    min_tree = sorted(min_tree, key=lambda x: int(x[0]))
    print(min_tree)
    row = 1
    col = 1
    fileOut.write(str(min_weight) + '\n')
    for x,y,w in min_tree:
        FinalMatrix[x - 1][y - 1] = 1
        FinalMatrix[y - 1][x - 1] = 1
    for lines in FinalMatrix:
        s = ', '.join(map(str, lines))
        fileOut.write(s + '\n')
    ptr = 0
    for x,y,w in min_tree_save:
        ptr += 1
        if(ptr != len(min_tree_save)):
            fileOut.write('(' + str(x)+', ' + str(y)+')' + ', ')
        else:
            fileOut.write('(' + str(x)+', ' + str(y)+')')
    fileOut.close()
