import string

def is_pangram(s):
    s = s.lower()
    for i in string.ascii_lowercase:
        if not i in s:
            return False
    return True

print(is_pangram('The quick brown fox jumps over the lazy dog'))
print(is_pangram('test'))
