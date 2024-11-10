import pytest
"""
*-----------------------*-------------------*
|   Ограничение времени |   1 секунда       |
|   Ограничение памяти  |   64Mb            |
|   Ввод                |   the_calls.txt   |
|   Вывод               |   calls.txt       |
*-----------------------*-------------------*

Руководитель хочет узнать, какой из двух его заместителей A или B больше времени тратит на звонки по телефону. Для этого он установил шпионское ПО на их смартфоны и получил файл the_calls.txt, в котором для каждого звонка по телефону указано: дата в формате YYYY.MM.DD, длительность звонка в секундах (целое число), буква A или B, а также номер телефона, на который был совершён звонок (без пробелов, но со значком + и скобками). Поля в строке разделяются знаком табуляции.

Руководителю более подозрительны звонки, длившиеся дольше всего, поэтому строки следует отсортировать в обратном порядке по длительности звонка (сначала самые длительные).

Распределите строки из файла на два упорядоченных указанным образом списка, и запишите их в файл calls.txt: Сначала группу звонков A, затем - группу звонков B.
"""

def test_example():
    data = """\
2021.12.12	3	B	+79090329400
2019.10.03	18	A	+79999995454
2020.05.04	13	B	+72352452532
2020.05.04	4	A	+79023987567\
"""
    expected = """\
2019.10.03	18	A	+79999995454
2020.05.04	4	A	+79023987567
2020.05.04	13	B	+72352452532
2021.12.12	3	B	+79090329400\
"""
    lines = list(map(lambda x: tuple(x.split("\t")), data.splitlines()))
    res = transformation(lines)
    assert "\n".join(["\t".join(line) for line in res]) == expected


def transformation(
    arr: list[tuple[str,str,str,str]]
    ) -> list[tuple[str,str,str,str]]:
    sortedArr =  sorted(
        arr,
        key=lambda x: int(x[1]),
        reverse=True
    )
    dct: dict[str, list[tuple[str,str,str,str]]] = {}
    for elem in sortedArr:
        dct.setdefault(elem[2], []).append(elem)
    
    dct = dict(sorted(dct.items(), key=lambda x: x[0]))
    res = list(dct.values())
    
    return [x for xs in res for x in xs]


def main() -> None:
    with open("the_calls.txt", "r") as dataIn:
        arr = list(map(lambda x: tuple(x.split("\t")), dataIn.read().splitlines()))
        res = transformation(arr)
        with open("calls.txt", "w") as dataOut:
            dataOut.write(
                "\n".join(["\t".join(line) for line in res])
            )


if __name__ == "__main__":
    main()
