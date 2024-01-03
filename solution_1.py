def find_roots(a, b, c):
    alpha = b * b - 4 * a * c
    is_complex = 0
    if alpha < 0:
        is_complex = 1
        alpha = -alpha

    sq_alpha = alpha**0.5
    two_a = 2 * a

    if is_complex:
        x1 = complex(-b / two_a, sq_alpha / two_a)
        x2 = complex(-b / two_a, -sq_alpha / two_a)
    else:
        x1 = (-b + sq_alpha) / two_a
        x2 = (-b - sq_alpha) / two_a
    return (x1, x2)
