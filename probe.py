#!/usr/bin/env python3

import re
import collections

elements = []
ids = []
comments = {}
lines = {}
data_by_id = collections.defaultdict(dict)
data_by_element = collections.defaultdict(dict)

with open('./data/data1.txt', 'r') as file:

    for i, line in enumerate(file):
        if i < 3:
            continue

        tokens = re.split(r"\s+", line)
        tokens = list(filter(None, tokens))

        if len(tokens) == 0:
            break

        if i == 3:
            elements = tokens[1:-2]
            continue

        id = tokens[0]
        ids.append(id)

        line = tokens[-2]
        lines[id] = line

        comment = " ".join(tokens[1+len(elements)+1:])
        comments[id] = comment

        values = tokens[1:1+len(elements)]

        for n, value in enumerate(values):
            element = elements[n]
            data_by_id[id][element] = float(value)
            data_by_element[element][id] = float(value)


# example 1

for id in ids:
    comment = comments[id]
    line = lines[id]
    print("{} - {} [{}]".format(id, line, comment))

    values = data_by_id[id].values()
    total = sum(values)
    print("\tSUM: {0:3f}".format(total))

    print()

    for element in elements:
        value = data_by_id[id][element]
        print("\t{0}: {1:.3f}".format(element, value))

    print()

# example 2

for element in elements:
    print(element)

    values = data_by_element[element].values()

    min_value = min(values)
    print("\tMIN: {0:.3f}".format(min_value))

    max_value = max(values)
    print("\tMAX: {0:.3f}".format(max_value))

    avg = float(sum(values))/len(values)
    print("\tAVG: {0:.3f}".format(avg))

    print()
