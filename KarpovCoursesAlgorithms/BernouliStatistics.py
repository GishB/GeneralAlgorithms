import numpy as np


def get_bernoulli_confidence_interval(values: np.array):
    """Вычисляет доверительный интервал для параметра распределения Бернулли.

    :param values: массив элементов из нулей и единиц.
    :return (left_bound, right_bound): границы доверительного интервала.
    """
    z_score = 1.96
    empiric_p = np.mean(values)
    n = values.shape[-1]
    bound = z_score*(np.sqrt(empiric_p*(1-empiric_p)/n))
    left_bound = float(empiric_p - bound)
    right_bound = float(empiric_p + bound)
    return left_bound if left_bound > 0 else 0, right_bound if right_bound < 1 else 1

if __name__ == "__main__":
    values = np.random.rand(1, 150).round()
    print(get_bernoulli_confidence_interval(values))