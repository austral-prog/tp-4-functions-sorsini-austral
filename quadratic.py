# Replace the "ANSWER HERE" for your answer

def roots(a, b, c):
    discriminant = b**2 - (4*a*c)
    if discriminant > 0:
        r1 = (-b + discriminant**0.5) / (2 * a)
        r2 = (-b - discriminant**0.5) / (2 * a)
        return (f"({r1}, {r2})")
    elif discriminant == 0:
        r12 = -b / (2 * a)
        return (f"({r12})")
    else:
        return "( )"
#print(roots (1, -3, 2))

def value_y(a, b, c, x):
    y = (a * (x ** 2)) + (b * x) + c
    return y
#print(value_y(1, -3, 2, 1))

def to_string(a, b, c):
    if a == 0 and b == 0:
        return f"f(x) = {c}"
    elif a == 0:
        return f"f(x) = {b} * X + {c}"
    elif b == 0:
        return f"f(x) = {a} * X^2 + {c}"
    elif c == 0:
        return f"f(x) = {a} * X^2 + {b} * X"
    else:
        return f"f(x) = {a} * X^2 + {b} * X + {c}"
#print(to_string(2, -3, 1))

def derivation(a, b, c):
    if a == 0 and b == 0:
        return "f'(x) = 0"
    elif a == 0:
        return f"f'(x) = {b}"
    elif b == 0:
        return f"f'(x) = {a * 2} * X"
    else:
        return f"f'(x) = {a * 2} * X + {b}"
#print(derivation(2, -3, 1))
