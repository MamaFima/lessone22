def calculate_remainder(dividend, divisor):
    try:
        remainder = dividend % divisor
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            remainder = remainder - divisor
        return remainder
    except ZeroDivisionError:
        return "Ошибка: Делить на ноль нельзя"
