def check(string):
    return len(set(string.lower()))

print(check('helo'))

def longest(a1, a2):
    a3 = []
    a4 = []
    a3.extend(a1)
    a3.extend(a2)
    a4.extend(set(a3))
    a4.sort()
    return ''.join(a4)
print(longest('abcc', 'def'))