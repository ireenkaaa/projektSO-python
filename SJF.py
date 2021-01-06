
def SJFsort( list ):
    for i in range(1, len(list)):
        for j in range(1, len(list)-1):
            if list[j][1] > list[j + 1][1]:
                list[j], list[j + 1] = list[j + 1], list[j]
    return list 