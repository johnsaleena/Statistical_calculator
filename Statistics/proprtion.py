from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.square_root import square_root
from Statistics.Psd import psd
from Statistics.mean import mean

def proportion(numbers):
    num_value = len(numbers)
    result = 0
    for num in numbers:
        if result > 64:
            addition(result, result)
    return division(num, num_value)