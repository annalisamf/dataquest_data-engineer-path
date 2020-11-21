## 1. The ASCII Encoding ##

data = "QUEST"
for c in data:
    ascii_c = bin(ord(c))
    print(ascii_c)

## 2. ASCII Limitations ##

text = "The Swedish word for quest is sökande"
encoded = text.encode(encoding='ascii', errors='replace')
print(encoded)
print(type(encoded))

## 3. Bytes ##

bytes1 = bytes.fromhex('02')
bytes2 = bytes.fromhex('5a')
bytes3 = bytes.fromhex('ff')

## 4. Printable Characters ##

# provided inputs
string_1 = 'lowercase'
string_2 = 'UPPERCASE'
def check_uppercase (pstring):
    for letter in pstring:
        if not (ord(letter) >= 65 and ord(letter)<=90):
            return False
    return True

## 5. Multi-byte encodings ##

trad_chinese = "你好嗎?"
encoded = trad_chinese.encode(encoding="BIG5")
print(len(encoded))

## 7. Unicode ##

sentence = "ASCII cannot represent these: 你好嗎"
encoded_utf8 = sentence.encode(encoding='utf-8', errors='replace')
encoded_ascii = sentence.encode(encoding='ascii', errors='replace')

## 8. Decoding Bytes ##

# variable named encoded is accessible
decoded_cp1252 = encoded.decode(encoding="cp1252")
print(decoded_cp1252)

import chardet
encoding = chardet.detect(encoded)['encoding']

decoded = encoded.decode(encoding=encoding)
print(decoded)