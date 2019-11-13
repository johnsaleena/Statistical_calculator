from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.square_root import square_root
from Statistics.mean import mean


def psd(numbers):
    num_values = len(numbers)

    result = mean(numbers)
    total = 0
    for numb in numbers:
        result2 = subtraction(numb, result)
        sq = square(result2)
        total = addition(total, sq)
    return square_root(division(num_values, total))