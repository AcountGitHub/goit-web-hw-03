"""Factorize function that takes a list of numbers and returns a list of numbers
into which the numbers from the input list are factored without a remainder"""

from multiprocessing import Pool, cpu_count
from time import time


def factorize_number(number):
    """Factorize for one number"""
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def factorize(*numbers):
    """Sequential factorize"""
    result = []
    for num in numbers:
        result.append(factorize_number(num))
    return result


def multiprocessing_factorize(*numbers):
    """Multiprocessing factorize"""
    result = []
    with Pool(cpu_count()) as pool:
        result = pool.map(factorize_number, numbers)
        pool.close()
        pool.join()
    return result


if __name__ == "__main__":
    test_numbers1 = [128, 255, 99999, 10651060]
    a, b, c, d = factorize(*test_numbers1)
    print("Sequential execution results: ")
    print(a, b, c, d, sep="\n")
    a, b, c, d = multiprocessing_factorize(*test_numbers1)
    print("Multiprocessing execution results: ")
    print(a, b, c, d, sep="\n")
    test_numbers = [10651060] * 30
    begin_time = time()
    factorize(*test_numbers)
    end_time = time()
    print("Sequential execution time:", end_time - begin_time)
    start_time = time()
    multiprocessing_factorize(*test_numbers)
    stop_time = time()
    print("Multiprocessing execution time:", stop_time - start_time)
