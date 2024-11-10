import pytest
"""
*-----------------------*----------------------------*
|   Ограничение времени |   1 секунда                |
|   Ограничение памяти  |   64Mb                     |
|   Ввод                |   poe_unpublished.txt      |
|   Вывод               |   poe_decode_attempt.txt   |
*-----------------------*----------------------------*

Журналист обнаружил в архиве ранее не публиковавшуюся шифровку Эдгара Алана По poe_unpublished.txt. Чтобы не просто представить её публике, а совершить сенсацию, он хочет расшифровать её и для этого нанял вас. Вы разобрались, что в тексте намеренно перепутаны строки, а в каждой строке перепутаны слова. Для применения алгоритма расшифрования нужно упорядочить строки по возрастанию количества слов в каждой строке (слова разделяются пробелами), а внутри каждой строки слова нужно упорядочить по количеству букв в них. Результат нужно сохранить в файл poe_decode_attempt.txt
"""

def test_example():
    data = """\
I was angry with my friend
I told my wrath my wrath did end
I was angry with my foe
I told it not my wrath did grow\
"""
    expected = """\
I my was with angry friend
I my was foe with angry
I my my did end told wrath wrath
I it my not did told grow wrath\
"""
    lines = data.splitlines()
    res = transformation(lines)
    assert "\n".join(res) == expected
       

def transformation(
    arr: list[str]
    ) -> list[str]:
    return sorted(
        [
            " ".join(sorted(
                line.split(),
                key= lambda x: len(x)
            ))
            for line in arr
        ],
        key= lambda x: len(x.split())
    )
    

def main() -> None:
    with open("poe_unpublished.txt", "r") as dataIn:
        arr = dataIn.readlines()
        res = transformation(arr)
        with open("poe_decode_attempt.txt", "w") as dataOut:
            for line in res:
                print(line, file=dataOut)
                    


if __name__ == "__main__":
    main()
