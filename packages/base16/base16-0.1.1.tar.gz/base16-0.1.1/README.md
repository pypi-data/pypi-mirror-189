# base16

base16 is hexidecimal encoding with a different character set - chosen to minimize ambiguity between letters. It is useful for human-input codes. By default, we map alphanumeric characters outside the base16 character set to ones of closest similarity [1] within it.


# Character set map

| Hexidecimal | base16 |
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
import base16

encoded = base16.encode(b'Hello, World!')
decoded = base16.decode(b'EPHGHWHWHZCWCAKKHZKCHWHECB')
```

## Command Line
```bash
bash16 --encode "Hello, World!"
bash16 --decode "EPHGHWHWHZCWCAKKHZKCHWHECB"
```


# Fuzzy Matching

When decoding characters outside the base16 charset, we substitute a valid character that is most commonly mistaken for it. 

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

Letter mappings above were chosen based on confusion scores in [1].


# References

[1] Gupta, S.M. et al., Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, 1983, 83, 144-149
