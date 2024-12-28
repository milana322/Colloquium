import math


def generate_factorials(n):
    """
    генерирует список первых n факториалов
    n - натуральное число, количество факториалов
    factorials - cписок первых n факториалов
    raises ValueError - если n < 1
    """
    if not isinstance(n, int):
        raise ValueError("Входное значение n должно быть целым числом.")
    if n < 1:
        raise ValueError("n должно быть натуральным числом (n >= 1).")

    factorials = []
    for i in range(1, n + 1):
        factorials.append(math.factorial(i))

    return factorials
