""" 
CPF : 310.639.658.02

Dígito 1                        # Dígito 2
3 * 10 = 30                     # 3 * 11 = 33
1 *  9 = 09                     # 1 * 10 = 10
0 *  8 = 00                     # 0 *  9 = 09
6 *  7 = 42                     # 6 *  8 = 48
3 *  6 = 18                     # 3 *  7 = 21
9 *  5 = 45                     # 9 *  6 = 54
6 *  4 = 24                     # 6 *  5 = 30
5 *  3 = 15                     # 5 *  4 = 20
8 *  2 = 16                     # 8 *  3 = 24
Soma   = 199                    # 0 *  2 = 0
11 - (199 % 11) = 10            # Soma = 249
Se 10 > 9 == dígito 1 = 0       # 11 - (249 % 11) = 4
 """

from random import randint

numero = str(randint(100000000, 999999999))
novo_cpf = numero
reverso = 10                                        #  Contador reverso
total = 0

#  Loop do CPF
for index in range(19):
    if index > 8:                                   #  Primeiro índice
        index -= 9
    
    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)
    
        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)