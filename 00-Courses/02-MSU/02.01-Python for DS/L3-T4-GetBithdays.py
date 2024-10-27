import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   input.txt                           |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Дан текстовый файл input.txt, содержащий следующую информацию:

в первой строке записано число N,
в следующих N строках содержатся имена студентов,
а в следующих N строках (см. примеры) — их даты рождения.

Выведите построчно информацию из этого файла и запишите в файл output.txt, при этом разделяйте имена и даты рождения при помощи специального символа табуляции '\t'.
"""

def test_example():
    students = getBithdays(
        "3\n"
        "Dania\n"
        "Petya\n"
        "Egor\n"
        "13 oct\n"
        "28 mar\n"
        "26 feb"
    )
    assert "\n".join(
        [
            "\t".join(student) 
            for student in students
        ]
    ) == (
        "Dania	13 oct\n"
        "Petya	28 mar\n"
        "Egor	26 feb"
    )


def getBithdays(text: str)-> list[tuple[str,str]]:
    lines = text.splitlines()
    try:
        amount  = int(lines.pop(0))
    except:
        raise ValueError("Unable to parse amount of bithdays")
    
    if len(lines) < 2 * amount:
        raise ValueError(f"Expected input to have {2 * amount} lines got {len(lines)}")
    
    students = lines[0:amount]
    bithdays = lines[amount:2*amount]
    return list(zip(students, bithdays))


def main() -> None:
    with open("input.txt", mode="r") as file:
        text = file.read()
    
    with open("output.txt", "w") as out:
        for student in getBithdays(text):
            print("\t".join(student), file=out)   


if __name__ == "__main__":
    main()
