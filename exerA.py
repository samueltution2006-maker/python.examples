lst = [[1,2,3],[4,5,6],[7,8,9]]

def list_to_tuple(lst):
    result = ()

    i = 0
    while True:
        try:
            item = lst[i]
        except:
            break

        try:
            for _ in item:
                sub = list_to_tuple(item)
                result = result + (sub,)
                break
        except:
            # not a list, add directly
            result = result + (item,)

        i += 1

    return result

list_to_tuple(lst)

