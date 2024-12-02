from functools import reduce

def total_distance(input):
    list1, list2 = parse_input(input)
    list1.sort()
    list2.sort()

    return reduce(lambda sum, tuple: sum + abs(int(tuple[0]) - int(tuple[1])), zip(list1, list2), 0)

def similarity_score(input):
    list1, list2 = parse_input(input)

    frequency_map = {}

    for id in list2:
        if id in frequency_map:
            frequency_map[id] = frequency_map[id] + 1
        else:
            frequency_map[id] = 1

    return reduce(lambda sum, id: sum + int(id)*frequency_map.get(id, 0), list1, 0)


def parse_input(input):
    return map(list, zip(*(ids.split() for ids in input.split("\n"))))
