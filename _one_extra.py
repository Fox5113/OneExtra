#!/bin/python3

from functools import reduce

if __name__ == '__main__':
    arr = list(map(int, input("Input array for task\n >>> ").split()))
    print(reduce((lambda x, y: x ^ y), arr))


    """

    Use  битовые операции 


        extra([1, 1, 2, 3, 2]) => 3
        extra([345, 543, 435, 345, 543]) => 435

        extra([0, 0, 1]) => 1

    """