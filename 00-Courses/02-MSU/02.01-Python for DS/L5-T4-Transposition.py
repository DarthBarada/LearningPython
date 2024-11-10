import pytest
"""
*-----------------------*----------------------*
|   Ограничение времени |   1 секунда          |
|   Ограничение памяти  |   64Mb               |
|   Ввод                |   med_research.txt   |
|   Вывод               |   output.txt         |
*-----------------------*----------------------*

Биолог провёл исследование устойчивости нескольких видов бактерий стрептококка к нескольким антибиотикам и получил численные оценки, характеризующие эффективность действия каждого препарата. Его данные хранятся в формате текстовой таблицы дробных чисел (с плавающей точкой) med_research.txt, при этом по горизонтали изменяются виды бактерий, а по вертикали — виды антибиотиков. Однако для отчёта требуется, чтобы виды антибиотиков шли по горизонтали, а виды бактерий — по вертикали. Биолог узнал, что эта операция называется в математике транспонированием, но он не знает, как её сделать автоматически. Если вы не поможете, то ему предстоит провести ночь, вручную переставляя числа в огромном листе. В файле хранятся только сами числа. Список видов бактерий и список антибиотиков вас не интересуют, биолог вставит их сам.
"""

def test_example():
    data = """\
1 2 3 4 5
6 7 8 9 10\
"""
    expected = """\
1 6
2 7
3 8
4 9
5 10\
"""
    lines = list(map(lambda x: x.split(), data.splitlines()))
    res = transposition(lines)
    assert "\n".join([" ".join(line) for line in res]) == expected
       

def transposition(
    arr: list[list[str]]
    ) -> list[list[str]]:
    return [
        [line[idx] for line in arr]
        for idx in range(len(arr[0]) if len(arr)> 0 else 0)
    ]
    

def main() -> None:
    with open("med_research.txt", "r") as dataIn:
        arr = list(map(lambda x: x.split(), dataIn.readlines()))
        res = transposition(arr)
        with open("output.txt", "w") as dataOut:
            for line in res:
                print(" ".join(line), file=dataOut)


if __name__ == "__main__":
    main()
