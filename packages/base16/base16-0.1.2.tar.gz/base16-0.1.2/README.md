# Base16

A human-readable, compact binary data representation. Base16 is the hexidecimal system with a different character set - chosen to minimize ambiguity between letters. It is useful for high entropy inputs like voucher codes and confirmation codes. By default, when an alphanumeric character outside the base16 character set is decoded it is first replaced with the most similar valid character. The main goal is to minimise user frustration around these types of data input.


# Character Set

| Hexidecimal | Base16 |
|:-----------:|:------:|
|      0      |   A    |
|      1      |   B    |
|      2      |   C    |
|      3      |   D    |
|      4      |   E    |
|      5      |   G    |
|      6      |   H    |
|      7      |   K    |
|      8      |   P    |
|      9      |   R    |
|      a      |   S    |
|      b      |   T    |
|      c      |   W    |
|      d      |   X    |
|      e      |   Y    |
|      f      |   Z    |


# Usage

## Install
```bash
pip install base16
```

## Python
```python3
>>> import base16

>>> base16.encode(b'Hello, World!')
b'EPHGHWHWHZCWCAKKHZKCHWHECB'

>>> base16.decode(b'EPHGHWHWHZCWCAKKHZKCHWHECB')
b'Hello, World!'

>>> base16.random(16)
b'BABKXPWCBBPZDGPB'
```

## Command Line
```bash
> bash16 --encode "Hello, World!"
EPHGHWHWHZCWCAKKHZKCHWHECB

> bash16 --decode "EPHGHWHWHZCWCAKKHZKCHWHECB"
Hello, World!

> base16 --random 32
PKCTPECYBZGGXKRATBCCHGWDDECKCWCA

> echo "some piped data" | base16 --encode
KDHZHXHGCAKAHRKAHGHECAHEHBKEHB

> echo "KDHZHXHGCAKAHRKAHGHECAHEHBKEHB" | base16 --decode
some piped data

```


# Decoding Incorrect Characters

If the user tries to decode a character not included in the base16 character set, we first replace it with the most-likely intended valid character. These replacement characters were chosen from a 1983 study [1] of four male university students' transcription errors. When a more representative study is found, these values can be safely changed later.

| Invalid | Valid |
|:-------:|:-----:|
|    0    |   D   |
|    1    |   T   |
|    2    |   Z   |
|    3    |   E   |
|    4    |   A   |
|    5    |   S   |
|    6    |   G   |
|    7    |   T   |
|    8    |   B   |
|    9    |   P   |
|    F    |   E   |
|    I    |   T   |
|    J    |   T   |
|    L    |   E   |
|    M    |   W   |
|    N    |   H   |
|    O    |   D   |
|    Q    |   D   |
|    U    |   W   |
|    V    |   Y   |


# References

[1] Gupta, S.M. et al., Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, 1983, 83, 144-149
