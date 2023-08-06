'''
base16 tests
'''

import os
import time
import unittest

from base16 import base16


PLAINTEXT = b'Hello, world!'
ENCODED = b'EPHGHWHWHZCWCAKKHZKCHWHECB'
MISREAD_ENCODED = b'3PH6HWHWHZCWCAKKHZKCHWH3CB'
HEX = '48656c6c6f2c20776f726c6421'


class TestBase16(unittest.TestCase):
    '''base16 tests'''

    def test_encode(self):
        '''Test base16.encode() method'''
        data = PLAINTEXT
        expected = ENCODED

        encoded = base16.encode(data)

        assert encoded == expected

    def test_decode(self):
        '''Test base16.decode() method'''
        data = ENCODED
        expected = PLAINTEXT

        decoded = base16.decode(data)

        assert decoded == expected

    def test_decode_not_strict(self):
        '''Test base16.decode() method with strict=False'''
        data = MISREAD_ENCODED
        expected = PLAINTEXT

        decoded = base16.decode(data, strict=False)

        assert decoded == expected

    def test_decode_filtered(self):
        '''Test base16.decode() method with filter_invalid=True'''
        data = ENCODED + b'234098235908723'
        expected = PLAINTEXT

        decoded = base16.decode(data, strict=True, filter_invalid=True)

        assert decoded == expected

    def test_encode_hex(self):
        '''Test base16.encode_hex() method'''
        data = HEX
        expected = ENCODED

        encoded = base16.encode_hex(data)

        assert encoded == expected

    def test_decode_hex(self):
        '''Test base16.decode_hex() method'''
        data = ENCODED
        expected = HEX

        decoded = base16.decode_hex(data)

        assert decoded == expected

    def test_random(self):
        '''Test base16.random() method'''
        data = base16.random(1024)
        assert len(data) == 1024

        data = base16.random(1023)
        assert len(data) == 1023

    def test_performance(self):
        '''Test base16 performance'''
        # Encode
        start = time.time()

        for _ in range(1000):
            data = os.urandom(1024)
            encoded = base16.encode(data)

        end = time.time()
        duration = end - start

        encode_bytes_per_second = 1024000 / duration
        encode_bytes_per_second = int(encode_bytes_per_second)

        # Decode
        random_base16_list = [base16.random(1024) for _ in range(1000)]

        start = time.time()

        for data in random_base16_list:
            decoded = base16.decode(data, strict=True)

        end = time.time()
        duration = end - start

        decode_bytes_per_second = 1024000 / duration
        decode_bytes_per_second = int(decode_bytes_per_second)

        assert encode_bytes_per_second > 1000000
        assert decode_bytes_per_second > 1000000
