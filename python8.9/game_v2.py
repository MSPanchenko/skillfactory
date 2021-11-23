"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np

# pep8 гласит: Или же, используйте старое соглашение, добавляя перед именами таких глобальных переменных
# один символ подчеркивания (которым вы можете обозначить те глобальные переменные,
# которые используются только внутри модуля).
#
# Именно поэтому использовал подчеркивание

_min_number = 1
_max_number = 101

def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 1
    predict = np.random.randint(_min_number, _max_number)
    # копируем минимум и максимум для локального редактирования диапазона чисел
    min_number = _min_number
    max_number = _max_number
    while number != predict:
        count += 1

        if number > predict:
            min_number = predict
        elif number < predict:
            max_number = predict

        # каждый раз при новой итерации цикла сокращаем в 2 раза диапазон возможных значений числа
        diff = max_number - min_number
        diff = 1 if diff == 1 else int(diff / 2)

        predict = (min_number + diff if number > predict else max_number - diff)

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
