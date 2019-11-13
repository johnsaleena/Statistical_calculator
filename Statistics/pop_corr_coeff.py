from Calculator.addition import addition
from Calculator.subtraction import subtraction
from Calculator.multiplication import multiplication
from Calculator.division import division
from Calculator.square import square
from Calculator.square_root import square_root
from CsvReader.CsvReader import CsvReader
from Statistics.Psd import psd
from Statistics.mean import mean
from Statistics.sample_mean import sample_mean

def pop_corr_coeff(numbers):
    num_value = len(numbers)
    # Calculation of covariance
    result1 = subtraction(numbers, sample_mean)
    result2 = subtraction(numbers, sample_mean)
    result3 = multiplication(result1, result2)
    covariance = division(num_value, sum(result3))

    # denominator
    data1 = CsvReader('Tests/Data/pop_corr_data1').numbers
    data2 = CsvReader('Tests/Data/pop_corr_data2').numbers
    result4 = psd(data1)
    result5 = psd(data2)
    result6 = multiplication(result4, result5)

    population_corr_coeff = division(result6, covariance)
    return population_corr_coeff