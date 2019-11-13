from Calculator.addition import addition
from Calculator.division import division
from Calculator.square import square
from Calculator.subtraction import subtraction
from Statistics.mean import mean


def vpp(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = square(result2)
        total = addition(total, sq)
    return division(num_values, total)