import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   256Mb                               |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

Посередине озера плавает плот, имеющий форму прямоугольника. Стороны плота направлены вдоль параллелей и меридианов. Введём систему координат, в которой ось OX направлена на восток, а ось ОY – на север. Пусть юго-западный угол плота имеет координаты (x_1, y_1), северо-восточный угол – координаты (x_2, y_2).

Пловец находится в точке с координатами (x, y). Определите, к какой стороне плота (северной, южной, западной или восточной) или к какому углу плота (северо-западному, северо-восточному, юго-западному, юго-восточному) пловцу нужно плыть, чтобы как можно скорее добраться до плота.

# Формат ввода
Программа получает на вход шесть чисел в следующем порядке: x1, y1 (координаты юго-западного угла плота), x2, y2 (координаты северо-восточного угла плота), x, y (координаты пловца). Все числа целые и по модулю не превосходят 100. Гарантируется, что x1<x2, y1<y2, x≠x1, x≠x2, y≠y1, y≠y2, координаты пловца находятся вне плота.

# Формат вывода
Если пловцу следует плыть к северной стороне плота, программа должна вывести символ ”N”, к южной — символ ”S”, к западной — символ ”W”, к восточной — символ ”E”. Если пловцу следует плыть к углу плота, нужно вывести одну из следующих строк: ”NW”, ”NE”, ”SW”, ”SE”.
"""
def test_example():
    swimmerPos = (-4,6)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(
        swimmerPos, 
        raftPos
    ) == "NW"
  
  
def test_swimmer_north_of_raft():
    swimmerPos = (0, 10)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "N"


def test_swimmer_south_of_raft():
    swimmerPos = (0, -10)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "S"


def test_swimmer_west_of_raft():
    swimmerPos = (-10, 0)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "W"


def test_swimmer_east_of_raft():
    swimmerPos = (10, 0)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "E"


def test_swimmer_northwest_of_raft():
    swimmerPos = (-10, 10)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "NW"


def test_swimmer_northeast_of_raft():
    swimmerPos = (10, 10)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "NE"


def test_swimmer_southwest_of_raft():
    swimmerPos = (-10, -10)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "SW"


def test_swimmer_southeast_of_raft():
    swimmerPos = (10, -10)
    raftPos = ((-1,-2),(5,3))
    assert getNearestRaftPoint(swimmerPos, raftPos) == "SE"


def test_swimmer_on_raft():
    swimmerPos = (0, 0)
    raftPos = ((-1,-1),(1,1))
    assert getNearestRaftPoint(swimmerPos, raftPos) == ""


def getCoordinates()-> tuple[int,int]:
    return (
        int(input()),
        int(input())
    )


def getNearestRaftPoint(
    swimmerPos: tuple[int,int],
    raftPos: tuple[tuple[int,int],tuple[int,int]]
) -> str:
    (raftPosSW, raftPosNE) = raftPos
    res= ""
    
    if swimmerPos[1] <= raftPosSW[1]:
        res = res + "S"
    elif swimmerPos[1] >= raftPosNE[1]:
        res = res + "N"
    
    if swimmerPos[0] <= raftPosSW[0]:
        res = res +  "W"
    elif swimmerPos[0] >= raftPosNE[0]:
        res = res +  "E"
    
    return res

    
def main() -> None:
    raftPos = (
        getCoordinates(),
        getCoordinates()
    )
    swimmerPos = getCoordinates()
    pos = getNearestRaftPoint(
        swimmerPos,
        raftPos
    )
    print(pos)


if __name__ == "__main__":
    main()
