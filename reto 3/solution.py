# solution.py

def problem_1(limit):
    """
    Retorna la suma de todos los múltiplos de 3 o 5 menores que el límite dado.
    """
    return sum(num for num in range(limit) if num % 3 == 0 or num % 5 == 0)

def problem_2(limit):
    """
    Retorna la suma de los términos pares de la secuencia de Fibonacci menores o iguales al límite dado.
    """
    a, b = 1, 2
    total = 0
    while a <= limit:
        if a % 2 == 0:
            total += a
        a, b = b, a + b
    return total

def is_prime(num):
    """
    Retorna True si el número dado es primo, False de lo contrario.
    """
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def problem_3(number):
    """
    Retorna el mayor factor primo del número dado.
    """
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            number //= i
    return number

def problem_4():
    """
    Retorna el mayor palíndromo que es el producto de dos números de 3 dígitos.
    """
    max_palindrome = 0
    for i in range(100, 1000):
        for j in range(i, 1000):
            product = i * j
            if str(product) == str(product)[::-1] and product > max_palindrome:
                max_palindrome = product
    return max_palindrome

def problem_5(limit):
    """
    Retorna el número más pequeño divisible por cada uno de los números del 1 al límite dado.
    """
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    def lcm(a, b):
        return a * b // gcd(a, b)

    result = 1
    for i in range(1, limit + 1):
        result = lcm(result, i)
    return result
