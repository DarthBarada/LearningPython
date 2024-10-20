import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

В этой задаче нужно вывести строку, которая считывается с клавиатуры, без первого и последнего символов.
"""
def test_example():
    assert getShrinkedStr("Hello World!") == "ello World"
    assert getShrinkedStr("Довод") == "ово"


def test_custom():
    assert getShrinkedStr("") == ""
 
   
def getShrinkedStr(text:str)-> str:
    return text[1:-1]

   
def main() -> None:
    text = input()
    print(getShrinkedStr(text))


if __name__ == "__main__":
    main()
