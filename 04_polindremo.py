def es_polindromo(num):
    num_str = str(abs(num))
    return num_str == num_str[::-1]

print(es_polindromo(121))
print(es_polindromo(-121))
print(es_polindromo(123))
