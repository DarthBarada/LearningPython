import pytest
"""
*-----------------------*-----------------*
|   Ограничение времени |   1 секунда     |
|   Ограничение памяти  |   64Mb          |
|   Ввод                |   weights.txt   |
|   Вывод               |   team.txt      |
*-----------------------*-----------------*

Для игры в американский футбол собрались мальчики с разным весом. Их вес (у всех он разный) и их имена (тоже у всех разные) даны в текстовом файле. Требуется создать две команды следующим образом: отсортировать всех ребят по убыванию веса, а затем 1-го, 3-го, 5-го и т.д. игроков отобрать в 1-ю команду, а оставшихся — во 2-ю команду. Вывести список команды №1 в первые строки файла team.txt, а список команды №2 в последние строки файла team.txt. В списках команд указывать и имена, и значения веса.
"""

def test_example():
    data = """\
    A 1
    B 2
    C 3.5
    D 4.5
    E 6.5
    F 7.5
    G 8.5
    H 9.5
    I 10.5
    J 11.5
    K 12.5
    L 13.5
    M 14.5
    N 15.5
    O 16.5
    P 17.5
    Q 18.5
    R 19.5
    S 20.5
    T 21.5
    U 22.5
    V 23.5\
    """
    lines = data.splitlines()
    arr = list(map(lambda x : x.split(), lines))
    commands = transformation(arr)
    assert commands == [ [ [ 'V', '23.5', ], [ 'T', '21.5', ], [ 'R', '19.5', ], [ 'P', '17.5', ], [ 'N', '15.5', ], [ 'L', '13.5', ], [ 'J', '11.5', ], [ 'H', '9.5', ], [ 'F', '7.5', ], [ 'D', '4.5', ], [ 'B', '2', ], ], [ [ 'U', '22.5', ], [ 'S', '20.5', ], [ 'Q', '18.5', ], [ 'O', '16.5', ], [ 'M', '14.5', ], [ 'K', '12.5', ], [ 'I', '10.5', ], [ 'G', '8.5', ], [ 'E', '6.5', ], [ 'C', '3.5', ], [ 'A', '1', ] ] ]
    

def transformation(
    arr: list[tuple[str,str]]
    ) -> list[list[tuple[str,str]]]:
    res = sorted(
        arr,
        key=lambda x: float(x[1]),
        reverse=True
    )
    return [
        [res[idx] for idx in range(0, len(arr), 2) ],
        [res[idx] for idx in range(1, len(arr), 2) ]
    ]
    

def main() -> None:
    with open("weights.txt", "r") as weights:
        arr = list(map(lambda x : tuple(x.split()), weights.readlines()))
        commands = transformation(arr)
        with open("team.txt", "w") as team:
            for command in commands:
                for player in command:
                    print(" ".join(player), file=team)


if __name__ == "__main__":
    main()
