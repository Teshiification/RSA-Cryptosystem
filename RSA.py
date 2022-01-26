#----------IMPORTS----------#

import math
import readline

#----------METHODS----------#

# USE THIS METHOD TO GENERATE e, d and n !!!


def RSA_KeyGenerator(p, q):
    # calc n
    n = p*q
    # calc phi from p and q
    phi = (p-1)*(q-1)
    # calc e, e != euclidic with phi
    e = phi+5
    # calc d
    d = extended_euclid(e, phi)[1]
    print(
        "\nÖffentlicher Schlüssel e:{0} \nPrivater Schlüssel d:{1}".format(e, d))

    print("e {0} : phi {1} : d {2} : n {3}\n".format(e, phi, d, n))

    return e, d, n

# decoding message


def Decode(message, e, n):
    return ((message ** e) % n)

# encoding message


def Encode(message, d, n):
    return ((message ** d) % n)

# return: use the second output in the returned array


def extended_euclid(a, b):
    if b == 0:
        return (a, 1, 0)  # a==1*a+0*b
    else:
        (faktor, rest) = divmod(a, b)  # a==faktor*b+rest
        (ggt, inn_mul_a, inn_mul_b) = extended_euclid(b, rest)  # innere mul
        (mul_a, mul_b) = (inn_mul_b, inn_mul_a-faktor*inn_mul_b)
        return (ggt, mul_a, mul_b)  # ggt==mul_a*a+mul_b*b


#----------MAIN----------#

message = 10

e, d, n = RSA_KeyGenerator(7, 13)

if(n != 0):
    c = Decode(message, e, n)
    print("Decoded Message:", c)
