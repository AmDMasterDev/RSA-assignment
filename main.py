import sympy
import random


def rsa_algo(p: int, q: int, msg: str):
    # n = p x q
    n = p * q
    # z = (p-1) x (q-1)
    z = (p - 1) * (q - 1)

    # e -> gcd(e,z)==1      ; 1 < e < z
    # d -> ed = 1(mod z)    ; 1 < d < z
    e = find_e(z)
    d = find_d(e, z)

    # Convert Plain Text -> Cypher Text
    cypher_text = ''
    # C = (P ^ e) % n
    for ch in msg:
        # ord() converts characters in ASCII
        ch = ord(ch)

        # chr() converts the ASCII back to characters, we first perform the formula
        # in ASCII format then convert back to character
        cypher_text += chr((ch ** e) % n)

    # Convert Plain Text -> Cypher Text
    plain_text = ''
    # P = (C ^ d) % n
    for ch in cypher_text:
        ch = ord(ch)
        plain_text += chr((ch ** d) % n)

    return cypher_text, plain_text


def find_e(z: int):
    # e -> gcd(e,z)==1      ; 1 < e < z
    e = 2
    while e < z:
        if gcd(e, z) == 1:
            return e
        e += 1


def find_d(e: int, z: int):
    # d -> ed = 1(mod z)        ; 1 < d < z
    d = 2
    while d < z:
        # check if this is the required `d` value
        if ((d * e) % z) == 1:
            return d
        # else : increment and continue
        d += 1


def gcd(x: int, y: int):
    # GCD by Euclidean method
    small, large = (x, y) if x < y else (y, x)

    while small != 0:
        temp = large % small
        large = small
        small = temp

    return large


def prime_num():
    a = random.randint(10, 100)

    for i in range(2, a):
        if (a % i) == 0:
            a = prime_num()
            break
    return a


# main
if __name__ == "__main__":
    # p = sympy.randprime(100, 1000)
    # q = sympy.randprime(100, 1000)
    # p, q = 59, 53

    p = prime_num()
    q = prime_num()
    while p == q:
        p = prime_num()
        q = prime_num()

    # print(a, b)

    msg = input("Enter your message: ")

    cypher_text, plain_text = rsa_algo(p, q, msg)

    print("Encrypted (Cypher text) : ", cypher_text)
    print("Decrypted (Plain text) : ", plain_text)
