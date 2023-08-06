'''
Human-readable, compact binary data encoding/decoding.
'''

import os


# Map hex characters to base16 equivalent
MAP = {
    '0': b'A',
    '1': b'B',
    '2': b'C',
    '3': b'D',
    '4': b'E',
    '5': b'G',
    '6': b'H',
    '7': b'K',
    '8': b'P',
    '9': b'R',
    'a': b'S',
    'b': b'T',
    'c': b'W',
    'd': b'X',
    'e': b'Y',
    'f': b'Z',
}

# Reverse map
UNMAP = {v: k for k, v in MAP.items()}

# Map of invalid characters to similar-looking valid characters
# Gupta, CHFIC 1983. See README.md for more info
FUZZY_MAP = {
    b'0': b'D',
    b'1': b'T',
    b'2': b'Z',
    b'3': b'E',
    b'4': b'A',
    b'5': b'S',
    b'6': b'G',
    b'7': b'T',
    b'8': b'B',
    b'9': b'P',
    b'F': b'E',
    b'I': b'T',
    b'J': b'T',
    b'L': b'E',
    b'M': b'W',
    b'N': b'H',
    b'O': b'D',
    b'Q': b'D',
    b'U': b'W',
    b'V': b'Y',
}


def encode(byte_string):
    '''
    Encode bytes to base16 bytes

    Args:
        byte_string (bytes): Bytes to encode

    Returns:
        bytes: base16-encoded bytes
    '''
    hex_string = byte_string.hex()
    base16_list = [MAP[c] for c in hex_string]
    base16_bytes = b''.join(base16_list)

    return base16_bytes

def decode(b16_bytes, filter_invalid=False, strict=False):
    '''
    Decode base16-encoded bytes to bytes

    Args:
        b16_bytes (bytes): base16 bytes to decode
        filter_invalid (bool): Filter out invalid characters
        strict (bool): Don't map invalid input to valid letters

    Returns:
        str: Decoded string
    '''
    if not strict:
        b16_bytes = b16_bytes.upper()
        b16_bytes = _map_fuzzy(b16_bytes)

    if filter_invalid:
        b16_bytes = _filter_invalid(b16_bytes)

    hex_string = decode_hex(b16_bytes)

    # Hex string must always have even length
    if len(hex_string) % 2 != 0:
        hex_string += '0'

    # Decode hex
    byte_string = bytes.fromhex(hex_string)

    return byte_string

def encode_hex(hex_string):
    '''
    Encode hex string to base16 bytes

    Args:
        hex_string (str): Hex string to encode

    Returns:
        bytes: base16-encoded bytes

    Note:
        Hex string must be lowercase (as in bytes.hex())
    '''
    b16_list = [MAP[c] for c in hex_string]
    b16_bytes = b''.join(b16_list)

    return b16_bytes

def decode_hex(b16_bytes):
    '''
    Decode base16-encoded bytes to hex string

    Args:
        b16_bytes (bytes): base16 bytes to decode

    Returns:
        str: Decoded hex string
    '''
    hex_string = ''

    # Reverse map hex characters
    try:
        for i in range(len(b16_bytes)):
            b = b16_bytes[i:i+1]
            hex_string += UNMAP[b]

    except KeyError as e:
        raise ValueError('Invalid character in input') from e

    return hex_string

def random(length=16):
    '''
    Generate random base16 bytes

    Args:
        length (int): Length of bytes to generate

    Returns:
        bytes: Random base16 bytes
    '''
    byte_length = (length + 1) // 2
    random_bytes = os.urandom(byte_length)
    random_hex = random_bytes.hex()

    random_base16 = encode_hex(random_hex)
    random_base16 = random_base16[:length]

    return random_base16

def _map_fuzzy(byte_string):
    '''
    Map similar-looking characters to their correct values

    Args:
        byte_string (bytes): Bytes to replace with valid letters

    Returns:
        bytes: Mapped bytes
    '''
    for k, v in FUZZY_MAP.items():
        byte_string = byte_string.replace(k, v)

    return byte_string

def _filter_invalid(byte_string):
    '''
    Filter out invalid characters

    Args:
        byte_string (bytes): Bytes to filter

    Returns:
        bytes: Filtered bytes
    '''
    filtered = b''
    for i in range(len(byte_string)):
        b = byte_string[i:i+1]
        if b in UNMAP:
            filtered += b

    return filtered
