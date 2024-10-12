import pytest
"""
*-----------------------*---------------------------------------*
|   Ограничение времени |   1 секунда                           |
|   Ограничение памяти  |   64Mb                                |
|   Ввод                |   стандартный ввод или input.txt      |
|   Вывод               |   стандартный вывод или output.txt    |
*-----------------------*---------------------------------------*

В офисе, где работает программист Петр, установили кондиционер нового типа. Этот кондиционер отличается особой простотой в управлении. У кондиционера есть всего лишь два управляемых параметра: желаемая температура и режим работы.

Кондиционер может работать в следующих четырех режимах:
* «freeze» — охлаждение. В этом режиме кондиционер может только уменьшать температуру. Если температура в комнате и так не больше желаемой, то он выключается.
* «heat» — нагрев. В этом режиме кондиционер может только увеличивать температуру. Если температура в комнате и так не меньше желаемой, то он выключается.
* «auto» — автоматический режим. В этом режиме кондиционер может как увеличивать, так и уменьшать температуру в комнате до желаемой.
* «fan» — вентиляция. В этом режиме кондиционер осуществляет только вентиляцию воздуха и не изменяет температуру в комнате.

Кондиционер достаточно мощный, поэтому при настройке на правильный режим работы он за час доводит температуру в комнате до желаемой.
Требуется написать программу, которая по заданной температуре в комнате troom, установленным на кондиционере желаемой температуре tcond и режиму работы определяет температуру, которая установится в комнате через час.
"""

def test_freeze_mode():
    assert run_conditioner((25, 20), "freeze") == 20
    assert run_conditioner((20, 25), "freeze") == 20
    assert run_conditioner((20, 20), "freeze") == 20

def test_heat_mode():
    assert run_conditioner((20, 25), "heat") == 25
    assert run_conditioner((25, 20), "heat") == 25
    assert run_conditioner((20, 20), "heat") == 20


def test_auto_mode():
    assert run_conditioner((25, 20), "auto") == 20
    assert run_conditioner((20, 25), "auto") == 25
    assert run_conditioner((20, 20), "auto") == 20


def test_fan_mode():
    assert run_conditioner((25, 20), "fan") == 25
    assert run_conditioner((20, 25), "fan") == 20
    assert run_conditioner((20, 20), "fan") == 20


def run_conditioner(
    temperature: tuple[int,int],
    mode: str                       # "freeze" | "heat" | "auto" | "fan"
)-> int:
    (t_room, t_cond) = temperature
    if mode == "freeze":
        return t_room if t_room <= t_cond else t_cond
    elif mode == "heat":
        return t_room if t_room >= t_cond else t_cond
    elif mode == "auto":
        return t_cond
    else:
        return t_room
        

def main() -> None:
    temperature = tuple(map(int, input().split()))
    mode = input()
    print(run_conditioner(temperature, mode))


if __name__ == "__main__":
    main()
