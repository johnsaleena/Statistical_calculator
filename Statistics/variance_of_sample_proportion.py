from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.square_root import square_root
from Statistics.Psd import psd
from Statistics.mean import mean


def var_sample_prop(numbers, size):
    result = 0
    data = dataList(numbers, size)
    num_value = len(data)
    result1 = proportion(numbers)
    result2 = subtraction(1, result1)
    result3 = subtraction(num_value, 1)
    for data2 in data:
        result4 = multiplication(result1, result2)
    return division(result4, result3)