from unittest import TestCase
from secp256k1 import Signature, G, N
from random import randint

import hashlib
import hmac


class PrivateKey:

    def __init__(self, secret):
        self.secret = secret
        self.point = secret * G  # <1>

    def hex(self):
        return '{:x}'.format(self.secret).zfill(64)

    def sign(self, z):
        k = self.deterministic_k(z)  # <1>
        r = (k * G).x.num
        k_inv = pow(k, N - 2, N)
        s = (z + r * self.secret) * k_inv % N
        if s > N / 2:
            s = N - s
        return Signature(r, s)

    def deterministic_k(self, z):
        k = b'\x00' * 32
        v = b'\x01' * 32
        if z > N:
            z -= N
        z_bytes = z.to_bytes(32, 'big')
        secret_bytes = self.secret.to_bytes(32, 'big')
        s256 = hashlib.sha256
        k = hmac.new(k, v + b'\x00' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        k = hmac.new(k, v + b'\x01' + secret_bytes + z_bytes, s256).digest()
        v = hmac.new(k, v, s256).digest()
        while True:
            v = hmac.new(k, v, s256).digest()
            candidate = int.from_bytes(v, 'big')
            # if candidate >= 1 and candidate < N:
            if 1 <= candidate < N:
                return candidate  # <2>
            k = hmac.new(k, v + b'\x00', s256).digest()
            v = hmac.new(k, v, s256).digest()


class PrivateKeyTest(TestCase):

    def test_sign(self):
        pk = PrivateKey(randint(0, N))
        z = randint(0, 2 ** 256)
        sig = pk.sign(z)
        self.assertTrue(pk.point.verify(z, sig))
