def reverse_string(str1):
    if len(str1) % 4 == 0:
       return ''.join(reversed(str1))
    return str1

print("the reverse string is",reverse_string('abcd'))
print("the reverse string is",reverse_string('python'))
