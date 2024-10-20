import numpy as np
import pytest
"""
Допустим, у нас есть массив из 5 элементов: [1, 2, 3, 4, 5]. 
Укажите, чему будет равно значение a[3], где a - значение исходного массива после выполнения процедуры Standard Scaling, описанной в лекции.
Ответ округлите до 2 знаков после запятой. 
В качестве разделителя целой и дробной части стоит использовать точку.
Например, ответ 1.257 стоит записать так (без кавычек): “1.26”.
"""

def test_example():
    assert np.round(standartScaler([1, 2, 3, 4, 5]), 2)[3] == 0.71


def standartScaler(arr: np.ndarray)-> np.ndarray:
    avg = np.average(arr)
    sigma = np.sqrt(np.sum(np.power(arr - avg, 2))/len(arr))
    return np.round((arr - avg) / sigma, 2)


def main() -> None:
    arr = np.array(list(map(int, input().split())))
    print(standartScaler(arr))


if __name__ == "__main__":
    main()
