def merge(left, right, key):
    result = []
    while len(left) > 0 and len(right) > 0:
        if key(left[0]) <= key(right[0]):
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    result.extend(left)
    result.extend(right)
    return result


def merge_sort(elements, key):
    if len(elements) <= 1:
        return elements
    mid = len(elements) // 2
    left = elements[:mid]
    right = elements[mid:]
    left = merge_sort(left, key)
    right = merge_sort(right, key)
    sorted_list = merge(left, right, key)
    return sorted_list


if __name__ == '__main__':
    l = [('Tom', 19, 80), ('John', 20, 90),('Jony', 17, 91),('Jony', 17, 93),('Json', 21, 85)]
    # short by Name
    print("Shorted by The Name")
    sorted_list = merge_sort(l, key=lambda tup: tup[0])
    print(sorted_list)
    # short by age
    print("Shorted by The Age")
    sorted_list = merge_sort(l, key=lambda tup: tup[1])
    print(sorted_list)
    # short by Score
    print("Shorted by The Score")
    sorted_list = merge_sort(l, key=lambda tup: tup[2])
    print(sorted_list)
