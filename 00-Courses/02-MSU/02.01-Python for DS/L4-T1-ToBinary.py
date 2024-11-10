import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

В этой задаче вам нужно перевести число из десятичной системы счисления в двоичную.
"""

def test_example():
    assert "".join(map(str,toBinary(2)[::-1])) == "10"
    assert "".join(map(str,toBinary(255)[::-1])) == "11111111"
    assert "".join(map(str,toBinary(0)[::-1])) == "0"


def toBinary(num)-> list[int]:
    res: list[int] = []
    if num == 0: 
        return [0]
    while num > 0:
        res.append(num%2)
        num = num // 2
    return res


def main() -> None:
    number = int(input())
    print(*toBinary(number)[::-1], sep="")


if __name__ == "__main__":
    main()
