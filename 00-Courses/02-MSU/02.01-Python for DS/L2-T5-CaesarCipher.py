import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

В книге "Жизнь двенадцати цезарей" историк Светоний писал про хитрый метод, который использовал Гай Юлий Цезарь для передачи секретных сообщений.

Позже этот метод, делающий текст понятным только отправителю и получателю, был назван Шифр Цезаря.

Кодирование таким шифром происходит следующим образом:
    1. Каждая буква входного сообщения заменяется на букву, находящуюся в алфавите на 3 позиции вперёд: "A" ->"D", "b"->"e", "c"->"f" и т.д. При этом регистр буквы учитывается: если она была заглавной, сохраняется заглавная, если строчной - буква шифротекста остаётся строчной.
    2. Последние три буквы заворачиваются по кругу на начало алфавита: "X" -> "A", "Y" -> "B", "Z" -> "C" (для маленьких букв - аналогично).
    3. Любые другие символы (пробелы, знаки пунктуации, цифры и др.) остаются без изменений.

Вам предлагается написать программу, которая шифрует сообщение по указанному алгоритму. Сообщение записано на английском языке.
"""
def test_example():
    assert caesarChiperEncode("Veni, vidi, vici") == "Yhql, ylgl, ylfl"


def test_empty_string():
    assert caesarChiperEncode("") == ""


def test_special_characters():
    assert caesarChiperEncode("Hello, World!") == "Khoor, Zruog!"


def test_numbers():
    assert caesarChiperEncode("12345") == "12345"


def test_mixed_case():
    assert caesarChiperEncode("HeLlo, WoRld!") == "KhOor, ZrUog!"


def test_wrap_around():
    assert caesarChiperEncode("XYZxyz") == "ABCabc"


def caesarChiperEncode(text: str)-> str:
    result = ""
    for char in text:
        charCode = ord(char)
        isUppercase = char == char.upper()
        (lower, upper) = ("A", "Z") if isUppercase else ("a", "z")
        codeLower, codeUpper = ord(lower), ord(upper)
        if lower <= char <= upper:
            if (charCode + 3) > codeUpper:
                result = result + chr(((charCode + 3) % codeUpper) + codeLower - 1)
            else:
                result = result + chr(charCode + 3)
        else:
            result = result + char
    
    return result


def main() -> None:
    text = input()
    print(caesarChiperEncode(text))


if __name__ == "__main__":
    main()