def is_armstrong(n: int) -> bool:
    if n < 0:
        return False
    digits = [int(d) for d in str(n)]
    return n == sum(d ** len(digits) for d in digits)


def is_perfect(n: int) -> bool:
    if n < 0:
        return False
    return n == sum(i for i in range(1, n) if n % i == 0)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n > 2 and n % 2 == 0:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


def get_property(n: int) -> list[str]:
    return_list = ["even" if n % 2 == 0 else "odd"]
    if is_armstrong(n):
        return_list.insert(0, "armstrong")
    return return_list


def digit_sum(n: int) -> int:
    n_string = str(n) if n > 0 else str(n)[1:]
    return sum([int(i) for i in n_string])
