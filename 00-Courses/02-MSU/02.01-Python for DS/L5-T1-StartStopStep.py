from ast import List
import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

В первой строке даны три числа: start, stop, step. Во второй строке даны целые числа через пробел, при этом гарантируется, что их количество не меньше, чем stop. Требуется считать числа из второй строки в список и присвоить его элементам с индексами от start до stop (не включая stop) с шагом step значения арифметической прогрессии range(start, stop, step).

Полученный список вывести на экран стандартным способом: с квадратными скобками и запятыми-разделителями.
"""

def test_example():
    assert transformation(1, 5, 2, [10, 20, 30, 40, 50, 60]) == [10, 1, 30, 3, 50, 60]
    assert transformation(0, 0, 1, [10, 20, 30, 40, 50, 60]) == [10, 20, 30, 40, 50, 60]
    assert transformation(4, 0, -2, [10, 20, 30, 40, 50, 60]) == [10, 20, 2, 40, 4, 60]
    

def transformation(
    start: int,
    stop: int,
    step: int,
    arr: list[int]
    ) -> list[int]:
    res = arr
    for idx in range(start, stop, step):
        res[idx] = idx
    return res

def main() -> None:
    start, stop, step = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    res = transformation(start, stop, step, arr)
    print(
        "[", 
        ", ".join(map(str,res)),
        "]",
        sep=""
    )


if __name__ == "__main__":
    main()
