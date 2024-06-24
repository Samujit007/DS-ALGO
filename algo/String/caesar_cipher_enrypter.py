#Time o(n) space o(n)
def caesarCipherEnrypter(str_in, key):
    out = ""
    first_unicode = ord('a')
    last_unicode = ord('z')
    for idx in range(len(str_in)):
        tmp_code = ord(str_in[idx])
        new_code = tmp_code + key
        if  new_code > last_unicode:
            wrap_code = (first_unicode-1) + (new_code%last_unicode if new_code%last_unicode <=26 else new_code%last_unicode%26)
            out+=chr(wrap_code)
            pass
        else:
            out+=chr(new_code)
        pass

    return out
str_1 = "abc"
key = 26
print(caesarCipherEnrypter(str_1, key))