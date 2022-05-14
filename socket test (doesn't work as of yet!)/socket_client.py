import socket

HEADER = 64
PORT = 5050
FORMAT = 'utf-8'
DISCONNECT_MESSAGE = "!DISCONNECT"
SERVER = "192.168.0.114"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)


class RSA:
    def rsa_algo(p: int, q: int, msg: str):
        # n = pq
        n = p * q
        # z = (p-1)(q-1)
        z = (p - 1) * (q - 1)

        # e -> gcd(e,z)==1      ; 1 < e < z
        # d -> ed = 1(mod z)        ; 1 < d < z

        e = RSA.find_e(z)
        d = RSA.find_d(e, z)

        # Convert Plain Text -> Cypher Text
        cypher_text = ''
        # C = (P ^ e) % n
        for ch in msg:
            # convert the Character to ascii (ord)
            ch = ord(ch)
            # encrypt the char and add to cypher text
            # convert the calculated value to Characters(chr)
            cypher_text += chr((ch ** e) % n)

        # Convert Plain Text -> Cypher Text
        plain_text = ''
        # P = (C ^ d) % n
        for ch in cypher_text:
            # convert it to ascii
            ch = ord(ch)
            # decrypt the char and add to plain text
            # convert the calculated value to Characters(chr)
            plain_text += chr((ch ** d) % n)

        return cypher_text, plain_text

    def find_e(z: int):
        # e -> gcd(e,z)==1      ; 1 < e < z
        e = 2
        while e < z:
            # check if this is the required `e` value
            if gcd(e, z) == 1:
                return e
            # else : increment and continue
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

    # main
    def __init__(self):
        print("Hello World")
        # p = sympy.randprime(100, 1000)
        # q = sympy.randprime(100, 1000)

    def encrypt_msg(msg):
        p, q = 59, 53
        RSA.cypher_text, RSA.plain_text = RSA.rsa_algo(p, q, msg)
        #
        # print("Encrypted (Cypher text) : ", cypher_text)
        # print("Decrypted (Plain text) : ", plain_text)



def send(msg):
    encryptor = RSA()

    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    encryptor.rsa_algo()
    client.send(message)
    print(client.recv(2048).decode(FORMAT))


send("Hello World!")
input()
send("Hello Everyone!")
input()
send("Hello Tim!")

send(DISCONNECT_MESSAGE)
