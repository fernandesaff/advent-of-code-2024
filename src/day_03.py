import re 
from functools import reduce
from operator import add


def part_1(input):
    expressions = re.findall("mul\\(([0-9]{1,3}),([0-9]{1,3})\\)",input)
    return reduce(add, [int(x[0])*int(x[1]) for x in expressions]) if len(expressions) > 0 else 0

def part_2(input):
    enabled = True
    sum = 0

    for expression in re.split("(do\\(\\)|don't\\(\\))", input):
        if expression == "do()":
            enabled = True
        elif expression == "don't()":
            enabled = False
        elif enabled and expression != "":
            sum += part_1(expression)

    return sum